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
        this.loaded = true
    }
}
</script>
<style></style>
