<template>
  <div class="columns is-multiline is-centered" align="center">
    <div class="column" v-for="tag in tags" v-bind:key="tag.id">
      <router-link :to="`/tags/${tag.slug}`" class="button is-primary">
        {{ tag.name }}
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "TagsBox",
  props: {
    tags: Object,
  },
};
</script>
