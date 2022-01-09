<template>
  <div class="page-my-account">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">My Account</h1>
      </div>
      <div class="column is-12">
        <button @click="logout()" class="button is-danger">Log out</button>
      </div>
      <hr />
    </div>
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

          <b-table-column
            field="product"
            label="Product"
            sortable
            v-slot="props"
          >
            <router-link :to="`/reviews/${props.row.id}`">
              <strong>{{ props.row.product }}</strong>
            </router-link>
          </b-table-column>

          <b-table-column field="rating" label="Rating" sortable v-slot="props">
            {{ props.row.rating }}
          </b-table-column>

          <b-table-column label="Tags" centered v-slot="props">
            <TagsBox v-bind:tags="props.row.tags" />
          </b-table-column>

          <b-table-column label="Brand" v-slot="props">
            {{ props.row.brand }}
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
                    <div :v-if="props.row.store">
                      {{ props.row.store }}
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
</template>

<script>
import axios from "axios";
import { TimeAgo } from "vue2-timeago";
import TagsBox from "@/components/TagsBox.vue";

export default {
  name: "MyAccount",
  data() {
    return {
      reviews: [],
      currentPage: 1,
      perPage: 10,
      total: 0,
    };
  },
  components: {
    TimeAgo,
    TagsBox,
  },
  mounted() {
    document.title = "Reviewer | My account";
    this.getMyReviews();
  },
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");

      this.$store.commit("removeToken");

      this.$router.push("/login");
    },
    getMyReviewsPage(newPage) {
      this.currentPage = newPage;
      this.getMyReviews();
    },

    async getMyReviews() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get(
          `/api/v1/reviews?limit=${this.perPage}&offset=${
            this.perPage * (this.currentPage - 1)
          }`
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