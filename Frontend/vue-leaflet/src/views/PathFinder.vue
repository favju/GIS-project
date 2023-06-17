<template>
    <div class="vueContainer">
        <h1>Find a path brother</h1>
        <div class="mapAndInfo">
            <myMap />
            <div>
                This the way
            </div>
        </div>
    </div>
</template>
<script>
import Map from '../components/Map.vue'
export default {
    name: "PathFinder",
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