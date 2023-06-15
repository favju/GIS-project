<template>
    <div id="detail">
        <h3>{{ this.skilift.name }}</h3>
        <h5>Length</h5>
        <p>{{ this.skilift.length }}</p>
        <h5>Seats</h5>
        <p>{{ this.skilift.maxseat }}</p>
        <h5>Type</h5>
        <p>{{ this.skilift.type }}</p>

    </div>
</template>
<script>
export default {
    name: "DetailSkilift",
    data() {
        return {
            skilift: { "name": "Rasse-Chaux Ronde", "length": "2131.6483", "maxseat": 8, "type": "Télésiège" }
        };
    },
    methods: {
    },
    mounted() {
    },
};
</script>
<style>
#detail {
    background-color: #909090;
}
</style>
