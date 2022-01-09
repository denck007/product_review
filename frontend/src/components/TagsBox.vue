<template>
  <div class="tags is-centered">
    <router-link
      class="tag is-primary is-medium"
      v-for="tag in tags"
      v-bind:key="tag.id"
      :to="`/reviews?&tags__name=${tag.name}`"
    >
      {{ tag.name }}
    </router-link>
  </div>
</template>

<script>
export default {
  name: "TagsBox",
  props: {
    tags: [],
  },
};
</script>
