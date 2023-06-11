<template>
  <div class="device-container">
    <div class="device-content-container">
      <h4>{{ device.name }}</h4>
      <p>Место установки: {{ device.place }}</p>
      <p>Серийный номер: {{ device.serial_number }}</p>
      <p>Инвентаризационный номер: {{ device.invent_number }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Device',
  props: {
    device: {
      type: Object,
      default() {
        return {}
      }
    }
  }
}
</script>

<style lang="scss">
.device-container {
  background: $color6;
  color:$color8;
  width: 100%;
  max-width: 97%;
  margin-bottom: 10px;
  border-radius: 20px;
  padding-top: 10px;
  padding-bottom: 10px;
  
  &:hover {
    background: $color7;
  }
}


.device-content-container {
  margin-left: 15px;
  
}
</style>