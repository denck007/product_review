<template ref="brand">
  <b-field label="Brand">
    <b-autocomplete
      rounded
      v-model="brand"
      :data="brands_filtered"
      icon="magnify"
      clearable
      :open-on-focus="true"
      :keep-first="false"
      @blur="
        (option) => {
          $emit('brand', this.brand);
        }
      "
      @select="
        (option) => {
          selected = option;
          $emit('brand', option);
        }
      "
      @typing="getBrandSearch"
    >
    </b-autocomplete>
  </b-field>
</template>

<script>
import axios from "axios";
export default {
  name: "BrandAutocompleteField",
  data() {
    return {
      brand: "",
      brands_filtered: [],
    };
  },
  methods: {
    async getBrandSearch(text) {
      await axios
        .get(`/api/v1/brands?search=${text}&limit=100`)
        .then((response) => {
          const brands = [];
          for (let i = 0; i < response.data.results.length; i++) {
            brands.push(response.data.results[i].brand);
          }
          this.brands_filtered = brands;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
