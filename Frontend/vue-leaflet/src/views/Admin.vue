<template>
  <div class="vueContainer">
    <h1>Admin</h1>
    <p>On this page you can open and close slopes and restaurant</p>
    <div class="mapAndInfo">
      <div id="info">
        <div class="select">
          <div class="info-column">
            <h2>Skilifts</h2>
            <div v-for="skilift in skilifts" :key="skilift.id" class="item">
              <div class="name">{{ skilift.name }}</div>
              <div class="open-status">
                <label>
                  <input
                    type="checkbox"
                    v-model="skilift.open"
                    @click="updateSkilift(skilift)"
                  />
                </label>
              </div>
            </div>
          </div>
          <div class="info-column">
            <h2>Restaurants</h2>
            <div
              v-for="restaurant in restaurants"
              :key="restaurant.id"
              class="item"
            >
              <div class="name">{{ restaurant.name }}</div>
              <div class="open-status">
                <label>
                  <input
                    type="checkbox"
                    v-model="restaurant.open"
                    @click="updateRestaurant(restaurant)"
                  />
                </label>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Map from "../components/Map.vue";
import skiliftService from "../services/skiliftService.js";
import restaurantService from "../services/restaurantService.js";

export default {
  name: "Admin",
  components: {
    Map,
  },
  data() {
    return {
      skilifts: [],
      restaurants: [],
    };
  },
  async mounted() {
    await skiliftService.getSkiliftsOpen();
    this.skilifts = skiliftService.skilifts.value;

    await restaurantService.getRestaurantsOpen();
    this.restaurants = restaurantService.restaurants.value;
  },
  methods: {
    async updateSkilift(skilift) {
      skilift.open = !skilift.open;
      await skiliftService.updateSkilifts(skilift.id, skilift);
    },
    async updateRestaurant(restaurant) {
      restaurant.open = !restaurant.open;
      await restaurantService.updateRestaurants(restaurant.id, restaurant);
    },
  },
};
</script>
<style scoped>
.select {
  display: flex;
  justify-content: space-between;
}

.info-column {
  flex: 1;
  margin-right: 1rem;
}

.item {
  margin-bottom: 1rem;
}

.name {
  font-weight: bold;
}

.open-status {
  margin-top: 0.5rem;
}

.mapAndInfo {
  display: flex;
}

h1 {
  color: #559d84;
  margin-left: 20px;
}

p {
  color: #90e8c9;
  margin-left: 20px;
  margin-bottom: 0px;
}

.vueContainer {
  margin: 20px;
  margin-bottom: 100px;
  overflow-y: auto;
}
.vueContainer::-webkit-scrollbar {
  background-color: transparent;
}

#info {
  display: flex;
  flex-wrap: wrap;
  max-height: 492.15px;
}

.info-column {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  min-width: 80%;
  margin-left: 20px;
}

#info * {
  margin: 0;
}

@media only screen and (max-width: 992px) {
  .mapAndInfo {
    display: flex;
    flex-direction: column;
  }
}

input[type="checkbox"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  width: 30px;
  height: 20px;
  background-color: #ddd;
  border-radius: 10px;
  position: relative;
  cursor: pointer;
  outline: none;
  transition: background-color 0.3s;
}

input[type="checkbox"]:before {
  content: "";
  position: absolute;
  top: 2px;
  left: 2px;
  width: 16px;
  height: 16px;
  background-color: #fff;
  border-radius: 50%;
  transition: left 0.3s;
}

input[type="checkbox"]:checked {
  background-color: #559d84;
}

input[type="checkbox"]:checked:before {
  left: 18px;
}
</style>
