<template>
  <div class="v-main-wrapper">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "MainWrapper",
  components: {},
  props: {},
  data() {
    return {};
  },
  computed: {},
  methods: {},
  watch: {},
};
</script>

<style lang="scss" scoped>
.v-main-wrapper {
  // min-height: max-content;
  max-width: 1600px;
  margin: 0 auto;
}
</style>
