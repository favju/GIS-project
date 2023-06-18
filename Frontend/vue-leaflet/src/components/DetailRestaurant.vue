<template>
    <div id="detail" class="card">
        <img class="card-img-top"
            src="https://cdn.discordapp.com/attachments/1022573840120946708/1119599160421785600/39.png"
            alt="Card image cap">
        <div class="card-body">
            <h3>{{ this.restaurant.name }}</h3>
            <h5>Length</h5>
            <p>{{ this.restaurant.length }}</p>
            <h5>Seats</h5>
            <p>{{ this.restaurant.maxseat }}</p>
            <h5>Type</h5>
            <p>{{ this.restaurant.type }}</p>
        </div>
    </div>
</template>
<script>
export default {
    name: "DetailRestaurant",
    data() {
        return {
            restaurant: { "name": "Rasse-Chaux Ronde", "length": "2131.6483", "maxseat": 8, "type": "Télésiège" }
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
    background-color: #909090;
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
