<template ref="product">
  <b-field label="Product">
    <b-autocomplete
      rounded
      v-model="product"
      :data="products_filtered"
      icon="magnify"
      clearable
      :open-on-focus="true"
      :keep-first="false"
      @blur="
        (option) => {
          $emit('product', this.product);
        }
      "
      @select="
        (option) => {
          selected = option;
          $emit('product', option);
        }
      "
      @typing="getProductSearch"
    >
    </b-autocomplete>
  </b-field>
</template>

<script>
import axios from "axios";
export default {
  name: "ProductAutocompleteField",
  props: {
    //product: "",
  },
  data() {
    return {
      product: "",
      products_filtered: [],
    };
  },
  methods: {
    async getProductSearch(text) {
      console.log("Computing getProductSearch");
      await axios
        .get(`/api/v1/products?search=${text}&limit=100`)
        .then((response) => {
          const products = [];
          for (let i = 0; i < response.data.results.length; i++) {
            products.push(response.data.results[i].product);
          }
          console.log("Computing productSearch products: " + products);
          this.products_filtered = products;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
