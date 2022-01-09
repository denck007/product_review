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
        <b-pagination
          :total="reviewsPagination.total"
          v-model="currentPage"
          :per-page="reviewsPagination.perPage"
          order="is-centered"
          range-before="3"
          range-after="3"
          icon-prev="chevron-left"
          icon-next="chevron-right"
          aria-next-label="Next page"
          aria-previous-label="Previous page"
          aria-page-label="Page"
          aria-current-label="Current page"
          iconPack="fa"
          @change="getMyReviews"
        >
        </b-pagination>
        <div>currentPage: {{ currentPage }}</div>
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
    return {
      reviews: [],
      currentPage: 1,
      reviewsPagination: {
        total: 0,
        perPage: 10,
        currentPage: 1,
      },
    };
  },
  components: {
    Reviews,
  },
  mounted() {
    document.title = "Reviewer | My account";
    this.getMyReviews();
  },
  watch: {
    reviewsPagination: function (val) {
      getMyReviews();
    },
  },
  methods: {
    logClick() {
      console.log("clicked");
    },
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
      console.log("this.currentPage: " + this.currentPage);
      await axios
        .get(
          `/api/v1/reviews/?limit=${this.reviewsPagination.perPage}&page=${this.currentPage}`
        )
        .then((response) => {
          this.reviews = response.data.results;
          this.reviewsPagination.total = response.data.count;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>