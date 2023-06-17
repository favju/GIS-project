<template>
    <div id="detail" class="card">
        <div class="card-body">
            <h3>{{ this.slope.name }}</h3>
            <h5>Difficulty</h5>
            <p>{{ this.slope.difficulty }}</p>
            <h5>Length</h5>
            <p>{{ this.slope.length }}</p>
        </div>
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
    margin: 20px;
    width: 30vw;
    max-width: 30vw;
    max-height: 60vh;
}
</style>
