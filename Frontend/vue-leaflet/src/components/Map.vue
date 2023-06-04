<template>
    <div id="container">
        <div id="mapContainer"></div>
    </div>
</template>

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";

export default {
    name: "Map",
    data() {
        return {
            center: [46.30942535215705, 7.0930909682770364],
        };
    },
    methods: {
        setupLeafletMap: function () {
            const mapDiv = L.map("mapContainer").setView(this.center, 13);
            L.tileLayer("https://tile.osm.ch/switzerland/{z}/{x}/{y}.png", {
                maxZoom: 18,
                attribution:
                    '&copy; <a href="https://wmts.geo.admin.ch/EPSG/3857/1.0.0/WMTSCapabilities.xml?lang=de">OpenStreetMap</a> contributors',
                bounds: [
                    [45, 5],
                    [48, 11],
                ],
            }).addTo(mapDiv);
        },
    },
    mounted() {
        this.setupLeafletMap();
    },
};
</script>

<style scoped>
#mapContainer {
    width: 60vw;
    height: 50vh;
    margin: 20px;
}
</style>
