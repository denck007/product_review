<template>
  <div class="page-my-reviews">
    <div class="container">
      <h2 class="subtitle">My reviews</h2>
      <Reviews />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Reviews from "@/components/Reviews.vue";

export default {
  name: "MyReviews",
  data() {
    return {};
  },

  components: {
    Reviews,
  },
  mounted() {
    document.title = "Reviewer | My Reviews";
  },
  methods: {},
  watch: {},
};
</script>
