import api from "@/services/api"
import { ref } from "vue"

let restaurants = ref([])

export default {
    restaurants,
    getRestaurants() {
        console.log("about to call api for restaurants")
        return api.get(`restaurants/`).then((response) => restaurants.value = response.data)
    }
}