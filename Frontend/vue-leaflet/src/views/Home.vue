<template>
    <h1>Explore the resort</h1>
    <myMap />
</template>
<script>
import Map from '../components/Map.vue'
export default {
    name: "Home",
    components: {
        myMap: Map
    }
}

</script>