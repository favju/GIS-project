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
            slope: { name: 'default', difficulty: 'default', length: 'default' }
        };
    },
    methods: {
    },
    mounted() {
    },
};
</script>
<style scoped>
#detail {
    background-color: #3C6255;
    color: #EDE4E0;
    margin: 20px;
    width: 30vw;
    max-width: 30vw;
    max-height: 60vh;
}

#detail h5 {
    margin-left: 4%;
}

#detail p {
    margin-left: 14%;
}

@media only screen and (max-width: 992px) {
    #detail {
        /* max-width: 80vw;
        max-height: auto; */
        min-width: 80vw;
        min-height: auto;
    }
}
</style>
