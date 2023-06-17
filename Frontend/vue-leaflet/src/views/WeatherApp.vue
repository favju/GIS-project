<template>
    <div class="vueContainer">
        <h1>Weather</h1>
        <div class="mapAndInfo">
            <Map ref="mapy" />
            <Weather />
        </div>
    </div>
</template>
<script>
import Map from '../components/Map.vue'
import Weather from '../components/Weather.vue'
import weatherService from '../services/weatherService.js'

export default {
    name: "WeatherApp",
    components: {
        Map,
        Weather
    },
    data() {
        return {
            marker: ''
        }
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
            this.marker = L.marker([localStorage.getItem("lat"), localStorage.getItem("lng")]).addTo(this.$refs.mapy.mapDiv);
            console.log("pose le marker")
        }
        else {
            this.marker = L.marker([46.319086, 7.072506],).addTo(this.$refs.mapy.mapDiv);

        }
        console.log(weatherService.current_weather)
    }
}

</script>

<style>
.mapAndInfo {
    display: flex;
}
</style>