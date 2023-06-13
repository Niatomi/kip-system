<template>
  <div class="specification-container">
    <h4><slot></slot></h4>
    <button class="search_btn" @click="deleteSpecification()">
      <i class="material-icons">close</i>
    </button>
  </div>
</template>

<script>
export default {
  name: 'Specification',
  methods: {
    deleteSpecification() {
      this.$emit('delete')
    }
  }
}
</script>

<style lang="scss" scoped>
.specification-container {
  display: flex;
  align-items: center;
  background: $color6;
  width: fit-content;
  border-radius: 30px;
  padding: 5px;
  
  gap: 10px;
}

h4 {
  color: $color8;
  padding-left: 10px;
}

.search_btn {
  width: fit-content;
  padding-left: 10px;
  padding-right: 10px;
  border-radius: 100%;
  background: $color7;
}
</style>