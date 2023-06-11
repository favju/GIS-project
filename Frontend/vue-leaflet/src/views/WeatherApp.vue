<template>
    <h1>Weather</h1>
    <div class="mapAndInfo">
        <myMap />
        <div>
            Everything is better with a weather app
        </div>
    </div>
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

<style>
.mapAndInfo {
    display: flex;
}
</style>