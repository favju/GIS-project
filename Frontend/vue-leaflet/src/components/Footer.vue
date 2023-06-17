
<template>
    <div id="footer">
        <div id="footerContent">
            <div id="left">
                <p>by Favre Julien & Gianadda David</p>
                <a href="https://github.com/favju/GIS-project">github</a>
            </div>
            <div id="right">
                <img
                    src="https://www.hes-so.ch/fileadmin/documents/HES-SO/Documents_HES-SO/images/hautes-ecoles/hes-so-valais-wallis_01.png" />
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: "Footer",
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
#footer {
    position: absolute;
    bottom: 0;
    min-width: 94vw;
    /* width: 90%; */
    /* height: 5vh; */
    /* Footer height */


}

#footerContent {
    width: 100%;
    border-top: 5px solid #3C6255;

    margin: 2vw;
    display: flex;
}

#footer p {
    margin-top: 10px;
    margin-bottom: 0px;
}

#footer img {
    max-height: 5vh;
    object-fit: contain;
}

#left {
    min-width: 50%;
}

#right {
    display: flex;
    min-width: 50%;
    align-items: flex-end;
    align-content: end;
    align-self: flex-end;
    justify-content: flex-end;
}
</style>
