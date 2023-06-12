<template>
  <div class="button-container" :style="style" :class="active ? 'btn__active' : ''">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "Button",
  props: ["bgColor", "textColor", 'active'],
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

  &:hover {
    background: $color7;
  }
}

.btn__active {
  background: $color7;
}
</style>
