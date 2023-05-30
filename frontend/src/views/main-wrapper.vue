<template>
  <Navbar />
  <div class="v-main-wrapper">
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from "@/components/navbar/navbar";

export default {
  name: "MainWrapper",
  components: {
    Navbar,
  },
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
