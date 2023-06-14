<template>
    <h1>Explore the resort</h1>
    <div class="mapAndInfo">
        <Map ref="mapy" />
        <DetailSkilift ref="detailSkilift" v-if="this.detail === 'skilift'" />
        <DetailSlope ref="detailSlope" v-if="this.detail === 'slope'" />
        <DetailSlope ref="detailRestaurant" v-if="this.detail === 'restaurant'" />
    </div>
    <button @click="testMakeTransparent()">makeTransparent</button>
    <button @click="testAddLayer()">hello</button>
</template>
<script>
import Map from '../components/Map.vue'
import DetailSkilift from '../components/DetailSkilift.vue'
import DetailSlope from '../components/DetailSlope.vue'
import DetailRestaurant from '../components/DetailRestaurant.vue'
import skiliftService from '../services/skiliftService.js'
import slopeService from '../services/slopeService.js'

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
        slopeService.getSlopes();
        skiliftService.getSkilifts();

    },

    computed: {
        skilifts() {
            return skiliftService.skilifts.value
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
                "opacity": 0.65
            };
            var myStyleRed = {
                "color": "red",
                "weight": 5,
                "opacity": 0.65
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
                        //layer.bindPopup(feature.properties.name);
                        layer.bindTooltip(feature.properties.name).openTooltip();
                        layer.on('click', (ev) => {
                            this.changeDetailSlope(feature.properties) // ev is an event object (MouseEvent in this case)

                        });

                    }
                });
            //}).addTo(this.$refs.mapy.mapDiv);
            //this.slopeLayer.addTo(this.$refs.mapy.mapDiv);
            //let layerControl = L.control.layers(this.slopeLayer).addTo(this.$refs.mapy.mapDiv);
            this.$refs.mapy.layerControl.addOverlay(this.slopeLayer, "Slopes")
            this.$refs.mapy.layerControl.addOverlay(this.skiliftLayer, "Skilifts")

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
            this.$refs.detailRestaurant.restaurent = content
        },

        testMakeTransparent() {
            this.slopeLayer.setStyle({ fillColor: 'black' })
        }

    }
}

</script>

<style>
.mapAndInfo {
    display: flex;
}
</style>