<template>
    <div id="detail" class="card">
        <img class="card-img-top" :src="skilift.image" alt="Card image cap">

        <div class="card-body">
            <div id="name-status">
                <h3>{{ this.skilift.name }}</h3>
                <div v-if="skilift.open">
                    <h5 style="color: rgb(8, 235, 8);">Open</h5>
                </div>
                <div v-else>
                    <h5 style="color: red;">Closed</h5>
                </div>
            </div>
            <h5>Length</h5>
            <p>{{ this.skilift.length }}</p>
            <h5>Seats</h5>
            <p>{{ this.skilift.maxseat }}</p>
            <h5>Type</h5>
            <p>{{ this.skilift.type }}</p>

        </div>
    </div>
</template>
<script>
export default {
    name: "DetailSkilift",
    data() {
        return {
            skilift: { "name": "default", "length": "default", "maxseat": 0, "type": "default" }
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

img {
    max-height: 40%;
    object-fit: cover;

}

#name-status {
    display: flex;
    flex-direction: row;
}

#name-status h5 {
    margin-bottom: 0;
    margin-left: 16px;
    width: 100%;
    height: 100%;
}


@media only screen and (max-width: 992px) {
    #detail {
        /* max-width: 80vw;
        max-height: auto; */
        min-width: 80vw;
        min-height: 800px;
    }

    #detail img {
        max-height: 60vw;
        object-fit: cover;

    }

}
</style>
