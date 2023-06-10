<template>
  <Transition name="fade-slide" appear>
    <div class="home-page-container">
      <img
      :src="require('@/assets/logo/Logo-lighter.svg/')"
      alt="Logo"
      height="300"
      />
      <h2>КИП Геофизика</h2>
      <h2>Основана в 2077 году</h2>
      <h2>Учитываем всё, но в основном приборы</h2>
    </div>
  </Transition>
</template>

<script>
import { Transition } from "vue";
export default {}
</script>

<style lang="scss">
.home-page-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 6%;
  gap: 30px;
}

.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 1s ease, transform 1s ease-in-out;
  transform: translateY(0px);
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-40px);
}
</style>
