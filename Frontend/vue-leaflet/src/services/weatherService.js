import api from "@/services/api"
import axios from "axios"
//import { ref } from "vue"

let chartData = {
    labels: [],
    datasets: [{
        data: [8.4, 8.2, 8.5, 7.4, 7.4, 8.6, 10.7],
        label: 'Temperatures in ºC',
        backgroundColor: 'red',
        //borderColor: 'red',
    },
    {
        data: [8.4, 8.2, 8.5, 7.4, 7.4, 8.6, 10.7],
        label: 'Precipitation in mm',
        backgroundColor: 'blue',
        //borderColor: 'blue',

    },
    {
        data: [8.4, 8.2, 8.5, 7.4, 7.4, 8.6, 10.7],
        label: 'Wind in km/h',
        backgroundColor: 'green',
        //borderColor: 'green',

    }

    ],
}

export default {
    chartData,
    async fetchWeather(latitude, longitude) {
        let searchUrl = 'https://api.open-meteo.com/v1/forecast?latitude='
            + latitude
            + '&longitude='
            + longitude
            + '&hourly=temperature_2m,precipitation,windspeed_10m';

        console.log(searchUrl)

        let result = await axios.get(searchUrl)
            .then((response) => chartData.datasets[0].data = response.data.hourly.temperature_2m)
        result = await axios.get(searchUrl)
            .then((response) => chartData.datasets[1].data = response.data.hourly.precipitation)
        result = await axios.get(searchUrl)
            .then((response) => chartData.datasets[2].data = response.data.hourly.windspeed_10m)
        result = await axios.get(searchUrl)
            .then((response) => chartData.labels = response.data.hourly.time)
        return result;
    }
}