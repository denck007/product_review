<template>
  <div class="page-create-review">
    <div class="container">
      <h1 class="title">Create a new Review</h1>
      <div class="columns is-multiline is-centered">
        <div class="column is-9 box">
          <div>
            <ProductAutocompleteField
              v-on:product="(option) => (product = option)"
            />

            <b-rate
              v-model="rating"
              :max="5"
              icon-pack="fas"
              size="is-large"
              :show-score="false"
              :spaced="true"
              :rtl="false"
            ></b-rate>

            <b-field label="Tags">
              <b-taginput
                v-model="tags_selected"
                :data="tags_filtered"
                autocomplete
                :keep-first="true"
                :allow-new="true"
                :open-on-focus="true"
                icon="label"
                placeholder="Add a tag"
                @typing="getFilteredTags"
              >
              </b-taginput>
            </b-field>
            <StoreAutocompleteField v-on:store="(option) => (store = option)" />
            <BrandAutocompleteField v-on:brand="(option) => (brand = option)" />

            <div class="field">
              <label>price</label>
              <div class="control">
                <input type="number" class="input" min="0" v-model="price" />
              </div>
            </div>

            <div class="field">
              <label>Product Website</label>
              <div class="control">
                <input type="text" class="input" v-model="product_url" />
              </div>
            </div>

            <div class="field">
              <label>Additional Notes</label>
              <div class="control">
                <textarea
                  type="text"
                  class="input"
                  maxlength="4096"
                  spellcheck="true"
                  v-model="notes"
                />
              </div>
            </div>
            <div>Upload an image - use the Buefy upload tool</div>
            <button class="button is-dark" @click="submitForm">Create</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductAutocompleteField from "@/components/ProductAutocompleteField.vue";
import BrandAutocompleteField from "@/components/BrandAutocompleteField.vue";
import StoreAutocompleteField from "@/components/StoreAutocompleteField.vue";
export default {
  name: "ReviewCreate",
  data() {
    return {
      product: "",
      store: "",
      brand: "",
      rating: 3,
      price: "",
      product_url: "",
      notes: "",
      tags_all: [],
      tags_filtered: [],
      tags_selected: [],
      products_filtered: [],
    };
  },
  components: {
    ProductAutocompleteField,
    BrandAutocompleteField,
    StoreAutocompleteField,
  },
  mounted() {
    document.title = "Reviewer | Create Review";
    this.getAllTags();
  },

  methods: {
    async submitForm() {
      console.log("product to sumbit: " + this.product);
      this.errors = [];
      if (this.product === "") {
        this.errors.push("Product name required");
      }
      if (this.rating === "") {
        this.errors.push("Rating is required");
      }
      // submit
      if (!this.errors.length) {
        this.$store.commit("setIsLoading", true);

        const data = {
          product: { product: this.product },
          store: { store: this.store },
          brand: { brand: this.brand },
          rating: this.rating,
          price: this.price,
          product_url: this.product_url,
          notes: this.notes,
          tags: [],
        };
        this.tags_selected.forEach((tag) => {
          data.tags.push({ name: tag });
          console.log(tag);
        });

        await axios
          .post("/api/v1/reviews", data)
          .then((response) => {
            this.$router.push("/");
          })
          .catch((error) => {
            this.errors.push(
              "Something went wrong sending data to server, please try again"
            );
            console.log(error);
          });

        this.$store.commit("setIsLoading", false);
      }
    },

    async getAllTags() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get("/api/v1/tags/")
        .then((response) => {
          const tags_all = [];
          for (let i = 0; i < response.data.results.length; i++) {
            tags_all.push(response.data.results[i].name);
          }
          this.tags_all = tags_all;
          this.tags_filtered = tags_all;
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
    getFilteredTags(text) {
      this.tags_filtered = this.tags_all.filter((option) => {
        return option.toString().toLowerCase().indexOf(text.toLowerCase()) >= 0;
      });
    },
  },
};
</script>
