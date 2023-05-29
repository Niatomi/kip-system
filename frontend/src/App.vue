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
html {
  max-width: 1980px;
  margin: 0 auto;
  height: 100%;
}

body {
  font-family: Arial sans-serif;
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
  padding: 2px 6px;
  border: 1px solid #787878;
  background: #fff;
  font: inherit;
  color: inherit;
}

#app {
  height: inherit;
  width: inherit;
  background: #074f57;
}
</style>
