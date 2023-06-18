import api from "@/services/api"
import { ref } from "vue"

let slopes = ref([])
let slopesSection = ref([])

export default {
    slopes,
    slopesSection,
    getSlopes() {
        console.log("about to call api for slopes")
        return api.get(`unionslopes/`).then((response) => slopes.value = response.data)
    },
    getSlopesSections() {
        console.log("about to call api for slopes")
        return api.get(`slopes/`).then((response) => slopesSection.value = response.data)
    }
}