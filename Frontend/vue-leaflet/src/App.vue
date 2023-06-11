<template>
  <my-header />
  <router-view />
  <my-footer />
</template>
<script>
import Home from './views/Home.vue'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue';

export default {
  name: "app",
  components: {
    myHeader: Header,
    myVue: Home,
    myFooter: Footer
  }
}
</script>
<style>
#app {
  background-color: #222;
  width: 100vw;
  min-width: 100vw;
  height: 100vh;
  padding: 0;
  display: flex;
  flex-direction: column;
}
</style>

