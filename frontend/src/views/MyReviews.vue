<template>
  <div class="page-my-reviews">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-12 box">
          <h2 class="subtitle">My reviews</h2>
          <b-table
            :backend-pagination="true"
            @page-change="getMyReviewsPage"
            :data="reviews"
            :total="total"
            :paginated="true"
            :per-page="perPage"
            :pagination-simple="false"
            detailed
            detail-key="id"
            detail-transition="fade"
            :show-detail-icon="true"
            pagination-position="bottom"
            default-sort-direction="asc"
            :pagination-rounded="false"
            sort-icon="arrow-up"
            sort-icon-size="sortIconSize"
            default-sort="created_at"
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page"
            icon-pack="fas"
          >
            <b-table-column
              field="id"
              label="ID"
              width="40"
              sortable
              numeric
              v-slot="props"
            >
              <a @click="props.toggleDetails(props.row)">
                {{ props.row.id }}
              </a>
            </b-table-column>

            <b-table-column
              field="product"
              label="Product"
              sortable
              v-slot="props"
            >
              <router-link :to="`/reviews/${props.row.id}`">
                <strong>{{ props.row.product.product }}</strong>
              </router-link>
            </b-table-column>

            <b-table-column
              field="rating"
              label="Rating"
              sortable
              v-slot="props"
            >
              <b-rate
                v-model="props.row.rating"
                :max="5"
                icon-pack="fas"
                size="is-medium"
                :show-score="false"
                :spaced="true"
                :disabled="true"
              ></b-rate>
            </b-table-column>

            <b-table-column label="Tags" centered v-slot="props">
              <TagsBox v-bind:tags="props.row.tags" />
            </b-table-column>

            <b-table-column label="Brand" v-slot="props">
              <div v-if="props.row.brand">
                {{ props.row.brand.brand }}
              </div>
              <div v-else></div>
            </b-table-column>

            <b-table-column label="Store" v-slot="props">
              <div v-if="props.row.store">
                {{ props.row.store.store }}
              </div>
              <div v-else></div>
            </b-table-column>

            <b-table-column label="Created" v-slot="props">
              <TimeAgo :datetime="props.row.created_at" />
            </b-table-column>

            <template #detail="props">
              <article class="media">
                <figure class="media-left">
                  <p class="image is-128x128">
                    <img v-bind:src="props.row.get_thumbnail" />
                  </p>
                </figure>
                <div class="media-content">
                  <div class="content">
                    <div>
                      <router-link :to="`/reviews/${props.row.id}`">
                        <strong>{{ props.row.product.product }}</strong>
                      </router-link>
                      <div v-if="props.row.price">${{ props.row.price }}</div>
                      <div v-if="props.row.store">
                        {{ props.row.store.store }}
                      </div>
                      <div v-if="props.row.brand">
                        {{ props.row.brand.brand }}
                      </div>
                      <div>
                        {{ props.row.notes }}
                      </div>
                    </div>
                  </div>
                </div>
              </article>
            </template>
          </b-table>
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
  name: "MyReviews",
  data() {
    return {
      reviews: [],
      currentPage: 1,
      perPage: 10,
      total: 0,
      search: "",
      search_tag: "",
    };
  },

  components: {
    TimeAgo,
    TagsBox,
  },
  mounted() {
    document.title = "Reviewer | My Reviews";
    this.getMyReviews();
  },
  methods: {
    getMyReviewsPage(newPage) {
      this.currentPage = newPage;
      this.getMyReviews();
    },

    updateSearchParams() {
      if (this.$route.query.search) {
        this.search = this.$route.query.search;
      }

      if (this.$route.query.search_tag) {
        this.search_tag = this.$route.query.search_tag;
      }
    },

    async getMyReviews() {
      this.$store.commit("setIsLoading", true);
      this.updateSearchParams();

      let query_params = "";
      if (this.search_tag != "") {
        query_params += `&tags__slug=${this.search_tag}`;
      }
      if (this.search != "") {
        query_params += `&search=${this.search}`;
      }
      console.log("query params: " + query_params);
      await axios
        .get(
          `/api/v1/reviews?limit=${this.perPage}&offset=${
            this.perPage * (this.currentPage - 1)
          }${query_params}`
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
  watch: {
    $route(to, from) {
      console.log("to.name" + to.name);
      if (to.name === "MyReviews") {
        console.log("Updating to.name" + to.name);
        this.getMyReviews();
      }
    },
  },
};
</script>
