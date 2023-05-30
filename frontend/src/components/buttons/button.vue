<template>
  <div class="button-container" :style="style">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "Button",
  props: ["bgColor", "textColor"],
  computed: {
    style() {
      return "background: " + this.bgColor + "; color: " + this.textColor;
    },
  },
};
</script>

<style lang="scss">
.button-container {
  background: $color6;
  color: $color8;
  padding: 10px;
  padding-left: 50px;
  padding-right: 50px;
  border-radius: 10px;
}
</style>
