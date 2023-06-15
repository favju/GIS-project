import api from "@/services/api"
import axios from "axios"
//import { ref } from "vue"

let chartData = {
    labels: [],
    datasets: [{
        data: [8.4, 8.2, 8.5, 7.4, 7.4, 8.6, 10.7],
        label: 'Filled',
        backgroundColor: 'red',
        borderColor: 'red',
        fill: true,
    }],
}

export default {
    chartData,
    async fetchWeather(latitude, longitude) {
        let searchUrl = 'https://api.open-meteo.com/v1/forecast?latitude='
            + latitude
            + '&longitude='
            + longitude
            + '&hourly=temperature_2m';

        console.log(searchUrl)

        let result = await axios.get(searchUrl)
            .then((response) => chartData.datasets[0].data = response.data.hourly.temperature_2m)
        result = await axios.get(searchUrl)
            .then((response) => chartData.labels = response.data.hourly.time)
        return result;
    }
}