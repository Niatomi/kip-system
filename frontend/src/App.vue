<template>
  <main-wrapper />
</template>

<script>
import MainWrapper from "@/components/main-wrapper";
export default {
  name: "App",
  components: {
    MainWrapper,
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Playfair&display=swap");

html {
  max-width: 1980px;
  margin: 0 auto;
  height: 100%;
  font-family: Playfair;
  font-size: 30px;
}

a {
  color: inherit;
  text-decoration: none;
}

body {
  color: $textcolor;
  margin: 0;
  padding: 0;
  width: 100%;
  max-width: 1980px;
  min-height: 100%;
  display: flex;
  justify-content: stretch;
  align-items: stretch;
}

input[type="text"],
input[type="password"],
input[type="email"],
input[type="tel"],
input[type="number"],
input[type="search"] {
  font: inherit;
  color: inherit;
}

#app {
  height: inherit;
  width: inherit;
  background: #074f57;
}
</style>
