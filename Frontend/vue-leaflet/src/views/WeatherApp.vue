<template>
    <h1>Weather</h1>
    <div class="mapAndInfo">
        <myMap />
        <Weather />
    </div>
</template>
<script>
import Map from '../components/Map.vue'
import Weather from '../components/Weather.vue'
export default {
    name: "WeatherApp",
    components: {
        myMap: Map,
        Weather
    }
}

</script>

<style>
.mapAndInfo {
    display: flex;
}
</style>