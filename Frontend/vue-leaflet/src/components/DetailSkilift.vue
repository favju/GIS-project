<template>
    <div id="detail" class="card">
        <img class="card-img-top"
            src="https://cdn.discordapp.com/attachments/1022573840120946708/1119599160421785600/39.png"
            alt="Card image cap">

        <div class="card-body">
            <h3>{{ this.skilift.name }}</h3>
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
            skilift: { "name": "Rasse-Chaux Ronde", "length": "2131.6483", "maxseat": 8, "type": "Télésiège" }
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
</style>
