<template>
  <div class="container">
    <div class="con">
      <img src="../assets/Logo-lighter.svg" >
      <p>КИП Геофизика</p>
      <p>Основана в 2077 году</p>
      <p>Учитываем всё, но в основном приборы</p>
    </div>
  </div>
</template>

<script>
export default {

  name: 'HomeView',
  components: {
  }
}
</script>

<style scoped>

img {
  width: 10rem;
}

.con {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  
  font-family: 'Lora';
  font-size: 4rem;
  color: #FFFFFF;
  
}

.container {
  height: 3rem;
  margin: 0;
  gap: 0px;
  padding: 0px;
}

</style>