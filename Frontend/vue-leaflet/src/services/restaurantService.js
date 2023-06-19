import api from "@/services/api"
import { ref } from "vue"

let restaurants = ref([])

export default {
    restaurants,
    getRestaurants() {
        console.log("about to call api for restaurants")
        return api.get(`restaurants/`).then((response) => restaurants.value = response.data)
    },
    getRestaurantsOpen() {
        console.log("about to call api for restaurants")
        return api.get(`restaurantsopen/`).then((response) => restaurants.value = response.data)
    },
    updateRestaurants(restaurantId, payload) {
        console.log("State changed")
        return api.patch(`restaurantsopen/${restaurantId}/`, payload).then((response) => response.data)
    }
}