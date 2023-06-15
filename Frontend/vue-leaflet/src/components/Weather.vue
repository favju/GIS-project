<template>
    <div class="container">
        <Bar v-if="loaded" :data="chartData" :options="options" />
    </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import weatherService from '../services/weatherService'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)


export default {
    name: 'BarChart',
    components: { Bar },
    data: () => ({
        loaded: false,
        chartData: null,
        options: {
            scales: {
                y: {
                    min: 0,
                    max: 25
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
