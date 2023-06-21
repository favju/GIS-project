<template>
    <div class="vueContainer">
        <h1>Find a path</h1>
        <p>Click on the map and it will show you the nearest point on a slope and the nearest restaurant at a lesser
            elevation</p>
        <div class="mapAndInfo">
            <Map ref="mapy" />
            <div id="loader" v-if="!loaded">
                <h2>Loading</h2>
                <img src="https://i.gifer.com/origin/34/34338d26023e5515f6cc8969aa027bca_w200.gif" />
            </div>
            <div v-else>
                <button @click="getLocation()">Use your location</button>
            </div>
        </div>
    </div>
</template>
<script>
import Map from '../components/Map.vue'
import slopeService from '../services/slopeService.js'
import restaurantService from '../services/restaurantService.js'

import * as turf from '@turf/turf'


import axios from "axios"

export default {
    name: "PathFinder",
    components: {
        Map
    },
    data() {
        return {
            detail: "",
            slopeLayer: null,
            latlng: { lat: '', lng: '' },
            elevation: null,
            marker: null,
            closestMarker: null,
            closestRestaurant: null,
            restaurantsCenter: [],
            loaded: false,
            hull: null
        }
    },

    computed: {
        restaurants() {
            return restaurantService.restaurants.value
        },
        slopes() {
            return slopeService.slopesSection.value
        }
    },
    async mounted() {

        // Fetches slopes and restaurant data from the django API
        await slopeService.getSlopesSections();
        await restaurantService.getRestaurants();

        // Prepares central point and elevation for all restaurants
        this.restaurants.features.forEach(feature => {
            let center = turf.center(feature)
            this.restaurantsCenter.push({ 'center': center, 'elevation': feature.properties.height })
        })


        // Add "find closest" fonctionality on map click
        this.$refs.mapy.mapDiv.on('click', async (event) => this.findClosest(event.latlng))

        this.testAddLayer()
        this.loaded = true

        this.hull = turf.convex(this.slopes);
        this.hull = turf.buffer(this.hull, 0.5)
        L.geoJSON(this.hull).addTo(this.$refs.mapy.mapDiv);


    },
    methods: {
        getLocation() {
            // Check if geolocation is supported by the browser
            if ("geolocation" in navigator) {
                // Prompt user for permission to access their location
                navigator.geolocation.getCurrentPosition(
                    // Success callback function
                    (position) => {
                        // Get the user's latitude and longitude coordinates
                        this.latlng.lat = position.coords.latitude;
                        this.latlng.lng = position.coords.longitude;
                        this.findClosest(this.latlng);
                    },
                    // Error callback function
                    (error) => {
                        // Handle errors, e.g. user denied location sharing permissions
                        console.error("Error getting user location:", error);
                    }


                );

            } else {
                // Geolocation is not supported by the browser
                console.error("Geolocation is not supported by this browser.");
            }
        },
        async findClosest(latlng) {

            // Remove old marker if it exists
            if (this.marker && this.closestMarker) {
                this.$refs.mapy.mapDiv.removeLayer(this.marker)
                this.$refs.mapy.mapDiv.removeLayer(this.closestMarker)
            }

            if (this.closestRestaurant) {
                this.$refs.mapy.mapDiv.removeLayer(this.closestRestaurant)
            }

            // Get coordinates of click and add marker to map
            this.latlng = latlng;

            if (!turf.booleanPointInPolygon([this.latlng.lng, this.latlng.lat], this.hull)) {
                alert("You are not in the resort")
            }
            // Fetch elevation for coordinates of click
            let url = 'https://api.open-meteo.com/v1/elevation?latitude='
                + this.latlng.lat
                + '&longitude='
                + this.latlng.lng
            await axios.get(url)
                .then((response) => this.elevation = response.data.elevation[0])

            // Place marker on clicked point
            this.marker = L.marker(this.latlng).addTo(this.$refs.mapy.mapDiv);

            // Find neareast point on slope
            let slopesCopy = slopeService.slopesSection.value
            var closest = 10000000
            var bestpoint = null

            slopesCopy.features.forEach(feature => {
                feature.geometry.coordinates.forEach(multiligne => {
                    multiligne.forEach(point => {
                        let distance = turf.distance([this.latlng.lng, this.latlng.lat], point);
                        if (distance < closest) {
                            if (point[2] < this.elevation) {
                                closest = distance
                                bestpoint = point
                            }

                        }
                    })
                })
            });

            if (bestpoint != null) {
                this.closestMarker = L.marker([bestpoint[1], bestpoint[0]]).addTo(this.$refs.mapy.mapDiv)
                    .bindPopup('Closest slope')
            }

            console.log(this.elevation)

            // Find nearest restaurant
            var closest = 10000000
            var bestpoint = null
            this.restaurantsCenter.forEach(restaurant => {
                let distance = turf.distance([this.latlng.lng, this.latlng.lat], restaurant.center);
                if (distance < closest) {
                    if (restaurant.elevation < this.elevation) {
                        closest = distance
                        bestpoint = restaurant.center.geometry.coordinates
                    }

                }
            })

            // Make sure that there is not a mountain on the way to the restaurant
            let midpointCheck = turf.midpoint([this.latlng.lng, this.latlng.lat], bestpoint).geometry.coordinates
            console.log(turf.midpoint([this.latlng.lng, this.latlng.lat], bestpoint).geometry.coordinates)
            let midpointCheckElevation = 0
            // Fetch elevation for coordinates of click
            let urlElevationCheck = 'https://api.open-meteo.com/v1/elevation?latitude='
                + midpointCheck[1]
                + '&longitude='
                + midpointCheck[0]
            await axios.get(urlElevationCheck)
                .then((response) => midpointCheckElevation = response.data.elevation[0])
            console.log("mid point elevation" + midpointCheckElevation)
            if (midpointCheckElevation > this.elevation) {
                bestpoint = null
                console.log("mountain in the way")

            }

            if (bestpoint != null) {

                this.closestRestaurant = L.marker([bestpoint[1], bestpoint[0]]).addTo(this.$refs.mapy.mapDiv)
                    .bindPopup('Closest restaurant')
            }

        },


        testAddLayer() {
            let myStyleYellow = {
                "color": "yellow",
                "weight": 2,
                "opacity": 1
            };

            this.slopeLayer = L.geoJSON(this.slopes,
                {

                    onEachFeature: (feature, layer) => {
                        layer.bindTooltip(feature.properties.name).openTooltip();
                        layer.setStyle({
                            "color": feature.properties.difficulty,
                            "weight": 5,
                            "opacity": 1
                        })
                    }
                }).addTo(this.$refs.mapy.mapDiv);
            this.restaurantLayer = L.geoJSON(this.restaurants,
                {
                    style: myStyleYellow,
                    onEachFeature: (feature, layer) => {
                        //layer.bindPopup(feature.properties.name);
                        layer.bindTooltip(feature.properties.name).openTooltip();
                        layer.on('click', (ev) => {
                            this.changeDetailRestaurant(feature.properties) // ev is an event object (MouseEvent in this case)

                        });
                    },

                }).addTo(this.$refs.mapy.mapDiv);

            this.$refs.mapy.layerControl.addOverlay(this.slopeLayer, "Slopes")
            this.$refs.mapy.layerControl.addOverlay(this.restaurantLayer, "Restaurants")


        },


    }
}

</script>

<style scoped>
.mapAndInfo {
    display: flex;
}

.vueContainer {
    margin: 20px;
}

h1 {
    color: #559d84;
    margin-left: 20px;
}

p {
    color: #90e8c9;
    margin-left: 20px;
    margin-bottom: 0px;
}

#loader {
    display: flex;
    flex-direction: column;
    align-items: center;
    align-self: center;
    justify-content: center;
    width: 100%;
    max-width: 100%;
}

#loader * {
    display: flex;
    align-self: center;
    align-items: center;
    justify-self: center;
    text-align: center;
}

@media only screen and (max-width: 992px) {
    .mapAndInfo {
        display: flex;
        flex-direction: column;
    }
}
</style>