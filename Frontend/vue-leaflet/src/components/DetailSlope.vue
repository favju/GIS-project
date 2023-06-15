<template>
    <div id="detail">
        <h3>{{ this.slope.name }}</h3>
        <h5>Difficulty</h5>
        <p>{{ this.slope.difficulty }}</p>
        <h5>Length</h5>
        <p>{{ this.slope.length }}</p>

    </div>
</template>
<script>
export default {
    name: "DetailSlope",
    data() {
        return {
            slope: { name: 'Rasse', difficulty: 'Red', length: '1659.9414' }
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
