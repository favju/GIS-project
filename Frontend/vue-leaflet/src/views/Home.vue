<template>
    <div class="vueContainer">


        <h1>Explore the resort</h1>
        <p>Click on a slope, a skilift or a restaurant to learn more about it</p>
        <div class="mapAndInfo">
            <Map ref="mapy" />
            <DetailSkilift ref="detailSkilift" v-show="this.detail === 'skilift'" />
            <DetailSlope ref="detailSlope" v-show="this.detail === 'slope'" />
            <DetailRestaurant ref="detailRestaurant" v-show="this.detail === 'restaurant'" />
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
import restaurantService from '../services/restaurantService.js'

import * as turf from '@turf/turf'

export default {
    name: "Home",
    components: {
        Map,
        DetailSkilift,
        DetailSlope,
        DetailRestaurant
    },
    data() {
        return {
            detail: "",
            slopeLayer: null,
            skiliftLayer: null,
        }
    },
    async mounted() {
        //L.geoJSON(this.skilift.features).addTo(this.$refs.mapy.mapDiv);
        await slopeService.getSlopes();
        await skiliftService.getSkilifts();
        await restaurantService.getRestaurants();
        this.testAddLayer();
    },

    computed: {
        skilifts() {
            return skiliftService.skilifts.value
        },
        restaurants() {
            return restaurantService.restaurants.value
        },
        slopes() {
            return slopeService.slopes.value
        }
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
            var myStyleYellow = {
                "color": "yellow",
                "weight": 2,
                "opacity": 1
            };

            this.skiliftLayer = L.geoJSON(this.skilifts,
                {
                    style: myStyleBlue,
                    onEachFeature: (feature, layer) => {
                        //layer.bindPopup(feature.properties.name);
                        layer.bindTooltip(feature.properties.name).openTooltip();
                        layer.on('click', (ev) => {
                            this.changeDetailSkilift(feature.properties) // ev is an event object (MouseEvent in this case)

                        });
                    },

                }).addTo(this.$refs.mapy.mapDiv);

            this.slopeLayer = L.geoJSON(this.slopes,
                {
                    style: myStyleRed,
                    onEachFeature: (feature, layer) => {
                        layer.bindTooltip(feature.properties.name).openTooltip();
                        //layer.bindPopup(feature.properties.name);
                        if (feature.properties.name != 'Connector') {

                            layer.on('click', (ev) => {
                                this.changeDetailSlope(feature.properties) // ev is an event object (MouseEvent in this case)

                            })
                        }
                        ;

                    }
                }).addTo(this.$refs.mapy.mapDiv);
            //}).addTo(this.$refs.mapy.mapDiv);
            //this.slopeLayer.addTo(this.$refs.mapy.mapDiv);
            //let layerControl = L.control.layers(this.slopeLayer).addTo(this.$refs.mapy.mapDiv);

            this.restaurantLayer = L.geoJSON(this.restaurants,
                {
                    style: myStyleYellow,
                    onEachFeature: (feature, layer) => {
                        //layer.bindPopup(feature.properties.name);
                        layer.bindTooltip(feature.properties.name).openTooltip();
                        layer.on('click', (ev) => {
                            this.changeDetailRestaurant(feature.properties) // ev is an event object (MouseEvent in this case)
                            console.log(feature)
                        });
                    },

                }).addTo(this.$refs.mapy.mapDiv);

            this.$refs.mapy.layerControl.addOverlay(this.skiliftLayer, "Skilifts")
            this.$refs.mapy.layerControl.addOverlay(this.slopeLayer, "Slopes")
            this.$refs.mapy.layerControl.addOverlay(this.restaurantLayer, "Restaurants")


            // // TEST
            // let lifts = skiliftService.skilifts.value

            // // Filter to keep all the sections of the same slope

            // let rasse = lifts.features.filter((f) => f.properties.name == 'Rasse-Chaux Ronde')
            // console.log(rasse)
            // console.log(turf.length(rasse[0]))

        },

        changeDetailSkilift(content) {
            this.detail = "skilift"
            this.$refs.detailSkilift.skilift = content
        },

        changeDetailSlope(content) {
            this.detail = "slope"
            this.$refs.detailSlope.slope = content
        },

        changeDetailRestaurant(content) {
            this.detail = "restaurant"
            this.$refs.detailRestaurant.restaurant = content
        },

        testMakeTransparent() {
            this.slopeLayer.setStyle({ fillColor: 'black' })
        }

    }
}

</script>

<style scoped>
.mapAndInfo {
    display: flex;
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

.vueContainer {
    margin: 20px;
}


@media only screen and (max-width: 992px) {
    .mapAndInfo {
        display: flex;
        flex-direction: column;
    }
}
</style>