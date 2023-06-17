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
            mapDiv: null,
            test: 12,
            layerControl: null
        };
    },
    methods: {
        setupLeafletMap: function () {

            let osm = L.tileLayer("https://tile.osm.ch/switzerland/{z}/{x}/{y}.png", {

                maxZoom: 18,
                attribution: '&copy; <a href="https://wmts.geo.admin.ch/EPSG/3857/1.0.0/WMTSCapabilities.xml?lang=de">OpenStreetMap</a> contributors',
                bounds: [
                    [45, 5],
                    [48, 11],
                ],
            });
            let osmSwiss = L.tileLayer("https://tile.osm.ch/osm-swiss-style/{z}/{x}/{y}.png", {

                maxZoom: 18,
                attribution: '&copy; <a href="https://wmts.geo.admin.ch/EPSG/3857/1.0.0/WMTSCapabilities.xml?lang=de">OpenStreetMap</a> contributors',
                bounds: [
                    [45, 5],
                    [48, 11],
                ],
            });
            let satSwiss = L.tileLayer("https:wmts.geo.admin.ch/1.0.0/ch.swisstopo.swissimage/default/current/3857/{z}/{x}/{y}.jpeg", {

                maxZoom: 18,
                attribution: '&copy; <a href="https://wmts.geo.admin.ch/EPSG/3857/1.0.0/WMTSCapabilities.xml?lang=de">OpenStreetMap</a> contributors',
                bounds: [
                    [45, 5],
                    [48, 11],
                ],
            });

            // var satelliteLayer = L.tileLayer.swiss({
            //     layer: 'ch.swisstopo.swissimage',
            //     maxNativeZoom: 28
            // });


            this.mapDiv = L.map('mapContainer', {
                center: [46.319086, 7.072506],
                zoom: 13,
                layers: [osm]
            });

            this.mapDiv.on('click', function (event) {
                var latlng = event.latlng;
                console.log(latlng);
            })

            var baseMaps = {
                "OpenStreetMap": osm,
                "OpenStreetMap.HOT": osmSwiss,
                "Sat": satSwiss
                //"Satellite": satelliteLayer
            };

            var overlayMaps = {
                //"Cities": cities
            };

            this.layerControl = L.control.layers(baseMaps, overlayMaps).addTo(this.mapDiv);

            // L.tileLayer("https://tile.osm.ch/switzerland/{z}/{x}/{y}.png", {
            //     //L.tileLayer("https://tile.osm.ch/osm-swiss-style/{z}/{x}/{y}.png", {
            //     maxZoom: 18,
            //     attribution:
            //         '&copy; <a href="https://wmts.geo.admin.ch/EPSG/3857/1.0.0/WMTSCapabilities.xml?lang=de">OpenStreetMap</a> contributors',
            //     bounds: [
            //         [45, 5],
            //         [48, 11],
            //     ],
            // }).addTo(this.mapDiv);
        },
        testMethode() {
            console.log("hello from the mapityMap")
        }
    },
    mounted() {
        //this.mapDiv = L.map("mapContainer").setView(this.center, 13)
        //L.tileLayer.swiss().addTo(this.mapDiv);

        this.setupLeafletMap();
    },
};
</script>


<style scoped>
#mapContainer {
    width: 45vw;
    height: 60vh;
    margin: 20px;
    border-radius: 4px;
}
</style>
