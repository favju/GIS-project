<template>
    <div class="vueContainer">
        <h1>Explore the resort</h1>
        <p>Click on a slope, a skilift or a restaurant to learn more about it</p>
        <div class="mapAndInfo">
            <Map ref="mapy" />
            <DetailSkilift ref="detailSkilift" v-show="this.detail === 'skilift'" />
            <DetailSlope ref="detailSlope" v-show="this.detail === 'slope'" />
            <DetailRestaurant ref="detailRestaurant" v-show="this.detail === 'restaurant'" />
            <div id="loader" v-if="!loaded">
                <h2>Loading</h2>
                <img src="https://i.gifer.com/origin/34/34338d26023e5515f6cc8969aa027bca_w200.gif" />
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
import restaurantService from '../services/restaurantService.js'

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
            loaded: false
        }
    },
    async mounted() {
        await restaurantService.getRestaurants()
        this.addRestaurant()

        await skiliftService.getSkilifts()
        this.addSkilifts()

        await slopeService.getSlopes()
        this.addSlopes()

        this.loaded = true
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
        addRestaurant() {
            var myStyleYellow = {
                "color": "yellow",
                "weight": 5,
                "opacity": 1
            };

            this.restaurantLayer = L.geoJSON(this.restaurants,
                {
                    style: myStyleYellow,
                    onEachFeature: (feature, layer) => {
                        layer.bindTooltip(feature.properties.name).openTooltip();
                        layer.on('click', (ev) => {
                            this.changeDetailRestaurant(feature.properties) // ev is an event object (MouseEvent in this case)

                        });
                    },

                }).addTo(this.$refs.mapy.mapDiv);

            this.$refs.mapy.layerControl.addOverlay(this.restaurantLayer, "Restaurants")
        },

        addSkilifts() {
            var myStyleGrey = {
                "color": "grey",
                "weight": 5,
                "opacity": 1
            };
            this.skiliftLayer = L.geoJSON(this.skilifts,
                {
                    style: myStyleGrey,
                    onEachFeature: (feature, layer) => {
                        layer.bindTooltip(feature.properties.name).openTooltip();
                        layer.on('click', (ev) => {
                            this.changeDetailSkilift(feature.properties) // ev is an event object (MouseEvent in this case)

                        });

                    },

                }).addTo(this.$refs.mapy.mapDiv);

            this.$refs.mapy.layerControl.addOverlay(this.skiliftLayer, "Skilifts")
        },
        addSlopes() {

            this.slopeLayer = L.geoJSON(this.slopes,
                {
                    onEachFeature: (feature, layer) => {
                        layer.bindTooltip(feature.properties.name).openTooltip();
                        if (feature.properties.name != 'Connector') {

                            layer.on('click', (ev) => {
                                this.changeDetailSlope(feature.properties) // ev is an event object (MouseEvent in this case)

                            })
                        };
                        layer.setStyle({
                            "color": feature.properties.difficulty,
                            "weight": 5,
                            "opacity": 1
                        })

                    }
                }).addTo(this.$refs.mapy.mapDiv);

            this.$refs.mapy.layerControl.addOverlay(this.slopeLayer, "Slopes")


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