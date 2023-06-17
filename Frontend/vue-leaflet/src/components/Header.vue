
<template>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <a class="navbar-brand" href="#">Villars-Gryon-Diableret</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="#/PathFinder">Path finder</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="#/WeatherApp">Weather app</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
                </li>

            </ul>

        </div>
    </nav>
</template>

<script>

export default {
    name: "Header",
    components: {},
    data() {
        return {

        }
    },

    async mounted() {

    },

    computed: {

    },
    methods: {

    }
}
</script>
<style>
.navbar {
    background-color: #3C6255;

}

.navbar * {
    color: #EDE4E0 !important;
}

.navbar-brand {
    font-size: 34px;
    font-weight: bold;
}

#navbarSupportedContent {
    /* display: flex;
    justify-content: end;
    align-items: end;
    
    background-color: red; */
}
</style>
