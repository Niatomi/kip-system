<template>
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
</template>

<style lang="scss">
.home-page-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 6%;
  gap: 30px;
}
</style>
