<template>
    <h1>Weather</h1>
    <div class="mapAndInfo">
        <Map ref="mapy" />
        <Weather />
    </div>
</template>
<script>
import Map from '../components/Map.vue'
import Weather from '../components/Weather.vue'
export default {
    name: "WeatherApp",
    components: {
        Map,
        Weather
    },
    mounted() {
        this.$refs.mapy.mapDiv.on('click', function (event) {
            var latlng = event.latlng;
            localStorage.setItem("lat", latlng.lat)
            localStorage.setItem("lng", latlng.lng)
            location.reload()
        })

        if (localStorage.getItem("lat") && localStorage.getItem("lng")) {
            console.log("pose le marker")
            L.marker([localStorage.getItem("lat"), localStorage.getItem("lng")]).addTo(this.$refs.mapy.mapDiv);
            console.log("pose le marker")
        }
        else {
            L.marker([46.319086, 7.072506]).addTo(this.$refs.mapy.mapDiv);

        }
    }
}

</script>

<style>
.mapAndInfo {
    display: flex;
}
</style>