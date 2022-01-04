<template>
  <div class="page-reviews-by-tag">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title"></h1>
      </div>
      <div class="column is-12"></div>
      <hr />
      <div class="column is-12">
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
  name: "ReviewsByTag",
  data() {
    return {
      reviews: [],
    };
  },
  components: {
    Reviews,
  },
  watch: {
    $route(to, from) {
      if (to.name === "ReviewsByTag") {
        this.getReviews();
      }
    },
  },
  mounted() {
    this.getReviews();
  },
  methods: {
    async getReviews() {
      const tag_slug = this.$route.params.tag_slug;
      console.log(tag_slug);
      await axios
        .get(`/api/v1/reviews/tag/${tag_slug}`)
        .then((response) => {
          this.reviews = response.data;
          document.title = "Review | " + tag_slug;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
