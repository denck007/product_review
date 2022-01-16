<template>
  <div class="page-product">
    <div class="container">
      <h2 class="subtitle">Overview page for {{ product.product }}</h2>
      <Reviews />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Reviews from "@/components/Reviews.vue";

export default {
  name: "ProductDetail",
  data() {
    return {
      product: {},
    };
  },

  components: {
    Reviews,
  },
  mounted() {
    document.title = "Reviewer | Product";
    this.getProduct();
  },
  methods: {
    async getProduct() {
      this.$store.commit("setIsLoading", true);
      const product_slug = this.$route.query.product;
      console.log(`product_slug: ${product_slug}`);
      await axios
        .get(`/api/v1/products?slug=${product_slug}&limit=1`)
        .then((response) => {
          this.product = response.data.results[0];
          document.title = "Review | " + this.product.product;
        })
        .catch((error) => {
          console.log(error);
        });
      console.log(`this.product: ${this.product.product}`);
      this.$store.commit("setIsLoading", false);
    },
  },
  watch: {},
};
</script>
