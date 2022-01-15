<template>
  <div class="columns is-centered">
    <div class="column is-9 box">
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

        <b-table-column field="product" label="Product" sortable v-slot="props">
          <router-link :to="`/reviews/${props.row.id}`">
            <strong>{{ props.row.product.product }}</strong>
          </router-link>
        </b-table-column>

        <b-table-column field="rating" label="Rating" sortable v-slot="props">
          {{ props.row.rating }}
        </b-table-column>

        <b-table-column label="Tags" centered v-slot="props">
          <TagsBox v-bind:tags="props.row.tags" />
        </b-table-column>

        <b-table-column label="Brand" v-slot="props">
          {{ props.row.brand.brand }}
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
                    <strong>{{ props.row.product }}</strong>
                  </router-link>
                  <div :v-if="props.row.price">${{ props.row.price }}</div>
                  <div :v-if="props.row.store.store">
                    {{ props.row.store.store }}
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
</template>

<script>
import axios from "axios";
import { TimeAgo } from "vue2-timeago";
import TagsBox from "@/components/TagsBox.vue";
export default {
  name: "Reviews",
  data() {
    return {
      reviews: [],
      currentPage: 1,
      perPage: 10,
      total: 0,
    };
  },

  props: {
    filters: {
      tag: "",
      search: "",
    },
  },
  components: {
    TimeAgo,
    TagsBox,
  },
  mounted() {
    this.getMyReviews();
  },
  methods: {
    getMyReviewsPage(newPage) {
      this.currentPage = newPage;
      this.getMyReviews();
    },

    async getMyReviews() {
      this.$store.commit("setIsLoading", true);

      let query_params = "";
      if (this.filters.tag != "") {
        query_params += `&tags__name=${this.filters.tag}`;
      }
      if (this.filters.search != "") {
        query_params += `&search=${this.filters.search}`;
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
};
</script>
