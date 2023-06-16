import api from "@/services/api"
import { ref } from "vue"

let slopes = ref([])

export default {
    slopes,
    getSlopes() {
        console.log("about to call api for slopes")
        return api.get(`slopes/`).then((response) => slopes.value = response.data)
    }
}