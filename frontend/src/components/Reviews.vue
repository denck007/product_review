<template>
  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>Photo</th>
        <th>Name</th>
        <th>Rating</th>
        <th align="center">Tags</th>
        <th>Price</th>
        <th>Brand</th>
        <th>Store</th>
        <th>Created</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="review in reviews" v-bind:key="review.id">
        <td width="8%">
          <figure class="image m-1">
            <img v-bind:src="review.get_thumbnail" />
          </figure>
        </td>
        <td>
          <router-link :to="`/reviews/${review.id}`">
            <strong>{{ review.product }}</strong>
          </router-link>
        </td>
        <td>{{ review.rating }}/5</td>
        <td width="20%"><TagsBox v-bind:tags="review.tags" /></td>
        <td>
          <div v-if="review.price">${{ review.price }}</div>
        </td>
        <td>
          <div v-if="review.brand">{{ review.brand }}</div>
        </td>
        <td>
          <div v-if="review.product_url">
            <a
              v-bind:href="review.product_url"
              target="_blank"
              rel="noreferrer noopener"
              >{{ review.store }}</a
            >
          </div>
          <div v-else>{{ review.store }}</div>
        </td>
        <td><Timeago :datetime="review.created_at" /></td>
        <td>{{ review.notes }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import { Timeago } from "vue2-timeago";
import TagsBox from "@/components/TagsBox.vue";
export default {
  name: "Reviews",

  props: {
    reviews: [Object],
  },
  components: {
    Timeago,
    TagsBox,
  },
  methods: {
    orderTotalLength(order) {
      return order.items.reduce((acc, curVal) => {
        return (acc += curVal.quantiy);
      }, 0);
    },
  },
};
</script>
