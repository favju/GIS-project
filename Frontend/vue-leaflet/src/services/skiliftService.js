import api from "@/services/api"
import { ref } from "vue"

let skilifts = ref([])

export default {
    skilifts,
    getSkilifts() {
        console.log("about to call api")
        return api.get(`skilifts/`).then((response) => skilifts.value = response.data)
    }
}