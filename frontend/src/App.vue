<template>
  <main-wrapper />
  <CookieNotifier/>
</template>

<script>
import MainWrapper from "@/views/main-wrapper";
import {mapActions, mapGetters} from 'vuex'
import CookieNotifier from '@/components/cookie-notifier/cookie-notifier'

export default {
  name: "App",
  components: {
    MainWrapper,
    CookieNotifier
  },
  methods: {
    ...mapActions([
      'SET_COOKIES',
    ]),
  },
  mounted() {
    this.SET_COOKIES()
  }
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Ledger&display=swap");

html {
  // max-width: 1980px;
  margin: 0 auto;
  height: 100%;
  font-family: 'Ledger', serif;
  // font-family: 'Courier New', Courier, monospace;
  font-size: 30px;
  // font-weight: 600;
  background: #074f57;
}

h1,
h2,
h3,
h4 {
  font-weight: normal;
  margin: 0;
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

p {
  margin: 0;
}

#app {
  height: inherit;
  width: inherit;
}
</style>
