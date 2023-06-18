<template>
    <div class="container">
        <Line v-if="loaded" :data="chartData" :options="options" />
    </div>
</template>

<script>
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, PointElement, LineElement, CategoryScale, LinearScale } from 'chart.js'
import weatherService from '../services/weatherService'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, PointElement, LineElement)


export default {
    name: 'BarChart',
    components: { Line },
    data: () => ({
        loaded: false,
        chartData: null,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    }),
    computed: {


    },
    methods: {

    },
    async mounted() {
        this.loaded = false
        if (localStorage.getItem("lat") && localStorage.getItem("lng")) {
            await weatherService.fetchWeather(localStorage.getItem("lat"), localStorage.getItem("lng"))
        }
        else {
            await weatherService.fetchWeather(46.31301210623243, 7.096784711847028)
        }

        this.chartData = weatherService.chartData
        localStorage.removeItem("lat")
        localStorage.removeItem("lng")
        console.log(weatherService.chartData)
        console.log(weatherService.current_weather)
        this.$parent.marker.bindPopup(
            "Temperature " +
            String(weatherService.current_weather.current_weather.temperature) +
            "ºC | Wind " +
            String(weatherService.current_weather.current_weather.windspeed) +
            "km/h"
        ).openPopup();
        this.loaded = true
    }
}
</script>
<style scoped>
.container {
    margin: 20px;
}

@media only screen and (max-width: 992px) {
    .container {
        /* max-width: 80vw;
        max-height: auto; */
        min-width: 80vw;
        min-height: 600px;
    }
}
</style>
