<template>
    <h1>Explore the resort</h1>
    <div class="mapAndInfo">
        <Map ref="mapy" />
        <DetailSkilift ref="detailSkilift" v-if="this.detail === 'skilift'" />
        <DetailSlope ref="detailSlope" v-if="this.detail === 'slope'" />
    </div>

    <button @click="testAddLayer()">hello</button>
</template>
<script>
import Map from '../components/Map.vue'
import DetailSkilift from '../components/DetailSkilift.vue'
import DetailSlope from '../components/DetailSlope.vue'
import skiliftService from '../services/skiliftService.js'
import slopeService from '../services/slopeService.js'

export default {
    name: "Home",
    components: {
        Map,
        DetailSkilift,
        DetailSlope
    },
    data() {
        return {
            detail: ""
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

            L.geoJSON(this.skilifts,
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

            L.geoJSON(this.slopes,
                {
                    style: myStyleRed,
                    onEachFeature: (feature, layer) => {
                        //layer.bindPopup(feature.properties.name);
                        layer.bindTooltip(feature.properties.name).openTooltip();
                        layer.on('click', (ev) => {
                            this.changeDetailSlope(feature.properties) // ev is an event object (MouseEvent in this case)

                        });

                    }
                }).addTo(this.$refs.mapy.mapDiv);

        },

        changeDetailSkilift(content) {
            this.detail = "skilift"
            this.$refs.detailSkilift.skilift = content
        },

        changeDetailSlope(content) {
            this.detail = "slope"
            this.$refs.detailSlope.slope = content
        },


    }
}

</script>

<style>
.mapAndInfo {
    display: flex;
}
</style>