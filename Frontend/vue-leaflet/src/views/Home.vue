<template>
    <h1>Explore the resort</h1>
    <div class="mapAndInfo">
        <Map ref="mapy" />
        <div>
            {{ detail }}
        </div>
    </div>

    <button @click="testAddLayer()">hello</button>
</template>
<script>
import Map from '../components/Map.vue'
import skiliftService from '../services/skiliftService.js'

export default {
    name: "Home",
    components: {
        Map
    },
    data() {
        return {
            detail: "lorem ipsum"
        }
    },
    async mounted() {
        //L.geoJSON(this.skilift.features).addTo(this.$refs.mapy.mapDiv);
        await skiliftService.getSkilifts();
        console.log(skiliftService.skilifts.value)
        console.log(this.skilifts)
    },

    computed: {
        skilifts() {
            return skiliftService.skilifts.value
        }
    },

    methods: {
        testAddLayer() {
            console.log("coucou")
            //L.geoJSON(this.skilift.features).addTo(this.$refs.mapy.mapDiv);


            var myStyle = {
                "color": "blue",
                "weight": 5,
                "opacity": 0.65
            };

            L.geoJSON(this.skilifts,
                {
                    onEachFeature: (feature, layer) => {
                        layer.bindPopup(feature.properties.name);
                        layer.bindTooltip(feature.properties.name).openTooltip();
                        layer.on('click', (ev) => {
                            this.changeDetail(feature.properties) // ev is an event object (MouseEvent in this case)

                        });

                    }
                }).addTo(this.$refs.mapy.mapDiv);
        },

        changeDetail(content) {
            this.detail = content
        },

    }
}

</script>

<style>
.mapAndInfo {
    display: flex;
}
</style>