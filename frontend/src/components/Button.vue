<template>
    <button type="button">
        {{ name }}
    </button>
</template>

<script>
export default {
    name: "Button",
    props: ['name']
}
</script>

<style scoped>

button {
  border: none;
  color: white;
  text-align: center;
  padding: 0.5rem 1rem;
  text-decoration: none;
  display: inline-block;
  border-radius: 1rem;
  font-size: inherit;
  font-family: inherit;
  width: 14rem;
}

button:hover {
    background-color: #777777;
}



</style>