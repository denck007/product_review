<template>
  <div class="page-my-account">
    <div class="section">
      <div class="container">
        <h1 class="title">My Account</h1>
        <button @click="logout()" class="button is-danger is-medium" is-medium>
          Log out
        </button>
        <hr />
        <div>
          <router-link
            class="button is-primary is-medium px-6"
            :to="`/reviews`"
          >
            My Reviews
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { TimeAgo } from "vue2-timeago";
import TagsBox from "@/components/TagsBox.vue";

export default {
  name: "MyAccount",
  data() {
    return {
      reviews: [],
      currentPage: 1,
      perPage: 10,
      total: 0,
    };
  },
  components: {
    TimeAgo,
    TagsBox,
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
    getMyReviewsPage(newPage) {
      this.currentPage = newPage;
      this.getMyReviews();
    },

    async getMyReviews() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get(
          `/api/v1/reviews?limit=${this.perPage}&offset=${
            this.perPage * (this.currentPage - 1)
          }`
        )
        .then((response) => {
          this.reviews = [];
          response.data.results.forEach((item) => {
            this.reviews.push(item);
          });
          this.total = response.data.count;
        })
        .catch((error) => {
          this.reviews = [];
          this.total = 0;
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>