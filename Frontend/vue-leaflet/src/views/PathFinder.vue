<template>
    <div class="vueContainer">
        <h1>Find a path brother</h1>
        <p>Click on the map and it will show you the nearest point on a slope</p>
        <div class="mapAndInfo">
            <Map ref="mapy" />
            <div>
                This the way
            </div>
        </div>
    </div>
</template>
<script>
import Map from '../components/Map.vue'
import DetailSkilift from '../components/DetailSkilift.vue'
import DetailSlope from '../components/DetailSlope.vue'
import DetailRestaurant from '../components/DetailRestaurant.vue'
import skiliftService from '../services/skiliftService.js'
import slopeService from '../services/slopeService.js'
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
            latlng: null,
            elevation: null,
            marker: null,
            closestMarker: null,
        }
    },

    computed: {
        slopes() {
            return slopeService.slopes.value
        }
    },
    async mounted() {


        await slopeService.getSlopes();
        this.$refs.mapy.mapDiv.on('click', async (event) => {
            // Remove old marker if it exists
            if (this.marker && this.closestMarker) {
                this.$refs.mapy.mapDiv.removeLayer(this.marker)
                this.$refs.mapy.mapDiv.removeLayer(this.closestMarker)

            }
            // Get coordinates of click and add marker to map
            this.latlng = event.latlng;
            let url = 'https://api.open-meteo.com/v1/elevation?latitude='
                + this.latlng.lat
                + '&longitude='
                + this.latlng.lng
            await axios.get(url)
                .then((response) => this.elevation = response.data.elevation[0])
            console.log(this.elevation)
            //console.log(this.latlng)
            this.marker = L.marker(this.latlng).addTo(this.$refs.mapy.mapDiv);

            // Find neareast point on line?
            // returns all the point at the intersections!
            let slopesCopy = slopeService.slopes.value
            var closest = 10000000
            var bestpoint = null

            slopesCopy.features.forEach(feature => {
                feature.geometry.coordinates.forEach(multiligne => {
                    multiligne.forEach(point => {
                        //console.log(point)
                        var distance = turf.distance([this.latlng.lng, this.latlng.lat], point);
                        if (distance < closest) {
                            if (point[2] < this.elevation) {
                                closest = distance
                                bestpoint = point
                            }

                        }
                    })
                })
            });

            this.closestMarker = L.marker([bestpoint[1], bestpoint[0]]).addTo(this.$refs.mapy.mapDiv);
            console.log(this.elevation)
        })

        this.testAddLayer()

    },
    methods: {
        testAddLayer() {
            var myStyleBlue = {
                "color": "blue",
                "weight": 5,
                "opacity": 1
            };
            var myStyleRed = {
                "color": "red",
                "weight": 5,
                "opacity": 1
            };

            this.slopeLayer = L.geoJSON(this.slopes,
                {
                    style: myStyleRed,
                    onEachFeature: (feature, layer) => {
                        layer.bindTooltip(feature.properties.name).openTooltip();
                        //layer.bindPopup(feature.properties.name);


                    }
                }).addTo(this.$refs.mapy.mapDiv);

            this.$refs.mapy.layerControl.addOverlay(this.slopeLayer, "Slopes")

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
</style>