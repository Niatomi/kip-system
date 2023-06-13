<template>
  <div class="device-pool-item-container">
    <div class="device-pool-item-content">
      <p>{{ device.name }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DevicePoolItem',
  props: {
    device: {
      typeof: Object,
      default() {
        return {}
      }
    }
  }
}
</script>

<style lang="scss" scoped>

.device-pool-item-container {
  background: $color6;
  color: $color8;
  width: 100%;
  border-radius: 20px;
  
  &:hover {
    background: $color7;
  }
}

.device-pool-item-content {
  padding: 10px;
}

</style>