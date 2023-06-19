import api from "@/services/api"
import axios from "axios"
//import { ref } from "vue"

let current_weather = { current_weather: {} }
let chartData = {
    labels: [],
    datasets: [{
        data: [8.4, 8.2, 8.5, 7.4, 7.4, 8.6, 10.7],
        label: 'Temperatures in ºC',
        backgroundColor: 'red'
    },
    {
        data: [8.4, 8.2, 8.5, 7.4, 7.4, 8.6, 10.7],
        label: 'Precipitation in mm',
        backgroundColor: 'blue'

    },
    {
        data: [8.4, 8.2, 8.5, 7.4, 7.4, 8.6, 10.7],
        label: 'Wind in km/h',
        backgroundColor: 'green'

    }

    ],
}

export default {
    chartData,
    current_weather,
    async fetchWeather(latitude, longitude) {
        let searchUrl = 'https://api.open-meteo.com/v1/forecast?latitude='
            + latitude
            + '&longitude='
            + longitude
            + '&hourly=temperature_2m,precipitation,windspeed_10m&timezone=auto&current_weather=true';

        console.log(searchUrl)

        let result = await axios.get(searchUrl)
            .then((response) => chartData.datasets[0].data = response.data.hourly.temperature_2m)
        result = await axios.get(searchUrl)
            .then((response) => chartData.datasets[1].data = response.data.hourly.precipitation)
        result = await axios.get(searchUrl)
            .then((response) => chartData.datasets[2].data = response.data.hourly.windspeed_10m)
        result = await axios.get(searchUrl)
            .then((response) => chartData.labels = response.data.hourly.time)
        result = await axios.get(searchUrl)
            .then((response) => current_weather.current_weather = response.data.current_weather)

        return result;
    }
}