<template>
  <div class="page-my-account">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">My Account</h1>
      </div>
      <div class="column is-12">
        <button @click="logout()" class="button is-danger">Log out</button>
      </div>
      <hr />
    </div>
    <div class="columns is-centered">
      <div class="column is-9 box">
        <h2 class="subtitle">My reviews</h2>
        <Reviews v-bind:reviews="reviews" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Reviews from "@/components/Reviews.vue";

export default {
  name: "MyAccount",
  data() {
    return { reviews: [] };
  },
  components: {
    Reviews,
  },
  mounted() {
    document.title = "Reviewer | My account";

    this.getMyReviews();
  },
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");

      this.$store.commit("removeToken");

      this.$router.push("/login");
    },

    async getMyReviews() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get("/api/v1/reviews/")
        .then((response) => {
          this.reviews = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>