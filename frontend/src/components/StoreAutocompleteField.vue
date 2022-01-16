<template ref="store">
  <b-field label="Store">
    <b-autocomplete
      rounded
      v-model="store"
      :data="stores_filtered"
      icon="magnify"
      clearable
      :open-on-focus="true"
      :keep-first="false"
      @blur="
        (option) => {
          $emit('store', this.store);
        }
      "
      @select="
        (option) => {
          selected = option;
          $emit('store', option);
        }
      "
      @typing="getStoreSearch"
    >
    </b-autocomplete>
  </b-field>
</template>

<script>
import axios from "axios";
export default {
  name: "StoreAutocompleteField",
  data() {
    return {
      store: "",
      stores_filtered: [],
    };
  },
  methods: {
    async getStoreSearch(text) {
      await axios
        .get(`/api/v1/stores?search=${text}&limit=100`)
        .then((response) => {
          const stores = [];
          for (let i = 0; i < response.data.results.length; i++) {
            stores.push(response.data.results[i].store);
          }
          this.stores_filtered = stores;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
