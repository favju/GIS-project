<template>
    <h1>Weather</h1>
    <myMap />
</template>
<script>
import Map from '../components/Map.vue'
export default {
    name: "WeatherApp",
    components: {
        myMap: Map
    }
}

</script>