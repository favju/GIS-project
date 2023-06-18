<template>
    <div class="vueContainer">
        <h1>Weather</h1>
        <p>Click on the map to get detailed weather data about this specific point</p>
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

<style scoped>
.mapAndInfo {
    display: flex;
}

.vueContainer {
    margin: 20px;
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

@media only screen and (max-width: 992px) {
    .mapAndInfo {
        display: flex;
        flex-direction: column;
    }
}
</style>