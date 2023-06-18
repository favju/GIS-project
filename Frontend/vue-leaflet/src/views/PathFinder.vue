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
            marker: null,
            closestMarker: null,
        }
    },

    computed: {
        slopes() {
            return slopeService.slopesSection.value
        }
    },
    async mounted() {


        await slopeService.getSlopesSections();
        this.$refs.mapy.mapDiv.on('click', (event) => {
            // Remove old marker if it exists
            if (this.marker && this.closestMarker) {
                this.$refs.mapy.mapDiv.removeLayer(this.marker)
                this.$refs.mapy.mapDiv.removeLayer(this.closestMarker)

            }
            // Get coordinates of click and add marker to map
            this.latlng = event.latlng;
            //console.log(this.latlng)
            this.marker = L.marker(this.latlng).addTo(this.$refs.mapy.mapDiv);

            // Find neareast point on line?
            // returns all the point at the intersections!
            let slopesCopy = slopeService.slopesSection.value
            //console.log(slopesCopy)

            // Find neareast point on line?
            // returns all the point at the intersections!
            // slopesCopy.features.forEach(feature => {
            //     var snapped = turf.nearestPointOnLine(feature, [this.latlng.lat, this.latlng.lng]);
            //     //console.log(snapped)
            //     L.geoJSON(snapped).addTo(this.$refs.mapy.mapDiv);
            // });
            var closest = 10000000
            var bestpoint = null

            // one to many for loop
            slopesCopy.features.forEach(feature => {
                //console.log(feature)
                //console.log("level 1")
                feature.geometry.coordinates.forEach(multiligne => {
                    //console.log("level 2")
                    multiligne.forEach(point => {
                        //console.log("level 3")
                        var distance = turf.distance([this.latlng.lng, this.latlng.lat], point);
                        if (distance < closest) {
                            closest = distance
                            bestpoint = point
                        }
                    })
                    //console.log(closest)
                })
            });

            this.closestMarker = L.marker([bestpoint[1], bestpoint[0]]).addTo(this.$refs.mapy.mapDiv);
        })

        this.testAddLayer()
        // let slopesCopy = slopeService.slopes.value

        // // Filter to keep all the sections of the same slope
        // slopesCopy = slopesCopy.features.filter((f) => f.properties.name == 'Grand chamossaire')

        // // Combine the section of the slope
        // var combined = turf.combine(slopesCopy); // Does not work
        // //console.log(combined)

        // L.geoJSON(combined, {
        //     onEachFeature: (feature, layer) => {
        //         layer.bindTooltip(feature.properties.name).openTooltip();
        //     }
        // }).addTo(this.$refs.mapy.mapDiv);



        // var center = turf.center(slopeService.slopes.value);
        // console.log(center)
        // var centerOfMass = turf.centerOfMass(slopeService.slopes.value);
        // console.log(centerOfMass)

        // var enveloped = turf.envelope(slopeService.slopes.value);
        // console.log(enveloped)
        // //L.geoJSON(enveloped).addTo(this.$refs.mapy.mapDiv);
        // //enveloped.feature.addTo(this.$refs.mapy.mapDiv);
        // var length = turf.length(slopeService.slopes.value);
        // console.log("Total length of the slopes in km : " + length)

        // var hull = turf.convex(slopeService.slopes.value);
        // L.geoJSON(hull).addTo(this.$refs.mapy.mapDiv);
        // console.log("Area in m2 of the polygon that all slopes fit in" + turf.area(hull))

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