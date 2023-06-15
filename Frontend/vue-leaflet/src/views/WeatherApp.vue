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
    }
}

</script>

<style>
.mapAndInfo {
    display: flex;
}
</style>