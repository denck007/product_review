<template>
  <div class="page-review">
    <div class="container">
      <div align="center" justify="center">
        <h1 class="title">
          {{ review.product.product }}
        </h1>
        <b-rate
          v-model="review.rating"
          :max="5"
          icon-pack="fas"
          size="is-medium"
          :show-score="false"
          :spaced="true"
          :disabled="true"
        ></b-rate>
        <h3>
          Reviewed
          <TimeAgo :datetime="review.created_at" />
        </h3>
      </div>
      <hr />

      <TagsBox v-bind:tags="review.tags" />

      <div v-if="review.brand">Brand: {{ review.brand.brand }}</div>
      <div v-if="review.store">
        <div v-if="review.product_url">
          Store:
          <a
            v-bind:href="review.product_url"
            target="_blank"
            rel="noreferrer noopener"
            >{{ review.store }}</a
          >
        </div>
        <div v-else>Store: {{ review.store.store }}</div>
      </div>
      <div v-else></div>
      <div v-if="review.price">
        <p>Price: ${{ review.price }}</p>
      </div>

      <div v-if="review.notes">
        Notes:
        <div class="box">{{ review.notes }}</div>
      </div>

      <div class="field has-addons mt-6">
        <div class="control">
          <a class="button is-dark" @click="addToCart">Add to cart</a>
        </div>
      </div>

      <figure class="image mb-6">
        <img v-bind:src="review.get_image" />
      </figure>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { TimeAgo } from "vue2-timeago";
import TagsBox from "@/components/TagsBox.vue";
export default {
  name: "ReviewDetail",
  data() {
    return {
      review: {},
    };
  },
  components: {
    TimeAgo,
    TagsBox,
  },
  mounted() {
    this.getReview();
  },
  methods: {
    async getReview() {
      this.$store.commit("setIsLoading", true);
      const review_id = this.$route.params.review_id;
      await axios
        .get(`/api/v1/reviews/${review_id}`)
        .then((response) => {
          this.review = response.data;
          document.title = "Review | " + this.review.name;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
    addToCart() {},
  },
};
</script>
