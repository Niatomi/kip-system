<template>
  <nav>
    <div class="company-ident">
      <div class="logo">
        <img src="./assets/Logo-darker.svg" alt="Kip Logo" class="logo-img">
        <div class="name">
          <p>КИП Геофизика</p>
        </div>
      </div>
      <div class="btns">
        <router-link to="/about">Вакансии</router-link>
        <router-link to="/about">О компании</router-link>
        <Button name="Вход" style="color: #262626;"></Button>
      </div>
    </div>
    <!-- <router-link to="/">Home</router-link>
     -->
  </nav>
  <div class="content">
    <router-view/>
  </div>
</template>

<script>
import Button from '@/components/Button.vue'
export default {
  name: 'Main',
  components: {
    Button
  }
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
  text-rendering: optimizeSpeed;
  background: #074F57;
  font-family: 'Lora';
}

a {
  text-decoration: none;
}

a:visited {
  color: #FFFFFF;
}

nav {
  display: flex;
  flex-direction: row;
  align-items: center;
  
  position: fixed;
  width: 100%;
  height: 6vh;
  
  padding: 1rem;
  

  
  color: #FFFFFF; 
  background: #077187;
}

.logo-img {
  height: 8vh;
}

.logo {
  display: flex;
  gap: 1rem;
  align-items: center;
  font-size: 2rem;
}

.company-ident {
  display: flex;
  width: 100%;
  padding-right: 2rem;
  flex-direction: row;
  align-items: center;
  font-size: 1.8rem;
  justify-content: space-between;
}

.content {
  padding-top: 4%;
}

.btns {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.colored-btns {
  display: flex;
  gap: 1rem;
  background-color: #74A57F;
}

a:hover,
.company-ident:hover {
  color: #CACACA;
}
</style>
