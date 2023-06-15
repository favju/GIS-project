







<template>
    <div class="container">
        <Bar v-if="loaded" :data="chartData" :options="options" />
    </div>

    <!-- <Bar :data="chartData" :options="chartOptions" /> -->
    <br />
    <button @click="testAxios(48.398099569880216, 6.43563602321872)">test axios</button>
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
        // data() {
        //     console.log("########################")
        //     console.log(weatherService.chartData)
        //     return weatherService.chartData.value

        // },

        // options() {
        //     return {
        //         responsive: true
        //     }
        // }

    },
    methods: {
        async testAxios(lat, lng) {
            localStorage.setItem("lat", lat)
            localStorage.setItem("lng", lng)
            location.reload()
        }
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
        console.log(weatherService.chartData)
        this.loaded = true
    }
}
</script>





<!-- <template>
    <Bar :data="chartData" :options="chartOptions" />
    <br />
    <button @click="testAxios(46.31301210623243, 7.096784711847028)">test axios</button>
</template>

<script>
// DataPage.vue
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import weatherService from '../services/weatherService'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
    name: 'BarChart',
    components: { Bar },
    computed: {
        chartData() {
            console.log(weatherService.chartData)
            return weatherService.chartData.value

        },

        chartOptions() {
            return {
                responsive: true
            }
        }
    },
    methods: {
        testAxios(lat, lng) {
            weatherService.fetchWeather(lat, lng)
        }
    }
}
</script> -->