<template>
  <Transition name="fade-slide" appear>
    <div class="about-page-container">
      <h1>КИП Геофизика</h1>
      <p>
        Это система предназначенная для ведения учёта приборов в геофизике (но на самом деле довольно универсальная, её можно использовать в любых сферах, подобных по объектным областям)
      </p>
      <p>
        Created by Niatomi
      </p>
    </div>
  </Transition>
</template>

<script>
export default {
  name: "AboutPage",
};
</script>

<style lang="scss" scoped>
p {
  font-size: 40px;
}
.about-page-container {
  margin-top: 40px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 1s ease, transform 1s ease-in-out;
  transform: translateY(0px);
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(40px);
}
</style>
