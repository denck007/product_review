<template>
  <div class="page-create-review">
    <h1>Create a new Review</h1>
    <div class="columns is-multiline is-centered">
      <div class="column is-6 box">
        <div>
          <div class="field">
            <label>Product Name</label>
            <div class="control">
              <input type="text" class="input" v-model="product" />
            </div>
          </div>

          <div class="field">
            <label>Rating</label>
            <div class="control">
              <input
                type="number"
                class="input"
                min="1"
                max="5"
                v-model="rating"
              />
            </div>
          </div>
          <b-field label="Tags">
            <b-taginput
              v-model="tags_selected"
              :data="tags_filtered"
              autocomplete
              :allow-new="true"
              :open-on-focus="false"
              icon="label"
              placeholder="Add a tag"
              @typing="getFilteredTags"
            >
            </b-taginput>
          </b-field>

          <div class="field">
            <label>Store</label>
            <div class="control">
              <input type="text" class="input" v-model="store" />
            </div>
          </div>

          <div class="field">
            <label>Brand</label>
            <div class="control">
              <input type="text" class="input" v-model="brand" />
            </div>
          </div>

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
</template>

<script>
import axios from "axios";
export default {
  name: "ReviewCreate",
  data() {
    return {
      product: "",
      store: "",
      brand: "",
      rating: "",
      price: "",
      product_url: "",
      notes: "",
      tags_all: [],
      tags_filtered: [],
      tags_selected: [],
    };
  },

  mounted() {
    document.title = "Reviewer | Create Review";
    this.getAllTags();
  },

  methods: {
    async submitForm() {
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
          product: this.product,
          store: this.store,
          brand: this.brand,
          rating: this.rating,
          price: this.price,
          product_url: this.product_url,
          notes: this.notes,
          tags: this.tags_selected,
        };

        await axios
          .post("/api/v1/reviews/", data)
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
          const all_tags = [];
          for (let i = 0; i < response.data.length; i++) {
            all_tags.push(response.data[i].name);
          }
          this.all_tags = all_tags;
        })
        .catch((errror) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
    getFilteredTags(text) {
      this.tags_filtered = this.all_tags.filter((option) => {
        return option.toString().toLowerCase().indexOf(text.toLowerCase()) >= 0;
      });
    },
  },
};
</script>
