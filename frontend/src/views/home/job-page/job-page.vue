<template>
  <Transition name="fade-slide" appear>
  
    <div class="job-page-container">
      <div class="job-block">
        <h2>Сатанист второго разряда</h2>
        <h3>Зарплата: 15 000</h3>
        <h4>
          Описание: Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit
          nisi autem ipsa, nemo minima sed praesentium voluptatem vitae in
          reiciendis nihil possimus corrupti? Aperiam autem accusamus laborum
          voluptatum nam. Nesciunt incidunt accusamus soluta porro. Veniam
          provident harum autem saepe minima nihil dolore quam, quos hic explicabo
          obcaecati distinctio, tempore reprehenderit rem odit animi iure dolorum
          velit eum eligendi ipsa nisi. Sed fuga quos facere ipsum vel facilis
          esse omnis molestias ipsa ex consequatur praesentium odit qui corrupti
          distinctio quisquam odio dolore magnam fugit natus unde, ullam non
          assumenda. Commodi quas at debitis optio temporibus, et ut explicabo
          placeat officia illum!
        </h4>
      </div>
      <div class="job-block">
        <h2>Пажилой лётчик истребитель</h2>
        <h3>Зарплата: 54 000</h3>
        <h4>
          Описание: Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit
          nisi autem ipsa, nemo minima sed praesentium voluptatem vitae in
          reiciendis nihil possimus corrupti? Aperiam autem accusamus laborum
          voluptatum nam. Nesciunt incidunt accusamus soluta porro. Veniam
          provident harum autem saepe minima nihil dolore quam, quos hic explicabo
          obcaecati distinctio, tempore reprehenderit rem odit animi iure dolorum
          velit eum eligendi ipsa nisi. Sed fuga quos facere ipsum vel facilis
          esse omnis molestias ipsa ex consequatur praesentium odit qui corrupti
          distinctio quisquam odio dolore magnam fugit natus unde, ullam non
          assumenda. Commodi quas at debitis optio temporibus, et ut explicabo
          placeat officia illum!
        </h4>
      </div>
      <div class="job-block">
        <h2>КИП Инженер</h2>
        <h3>Зарплата: 50 000 </h3>
        <h4>
          Описание: Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit
          nisi autem ipsa, nemo minima sed praesentium voluptatem vitae in
          reiciendis nihil possimus corrupti? Aperiam autem accusamus laborum
          voluptatum nam. Nesciunt incidunt accusamus soluta porro. Veniam
          provident harum autem saepe minima nihil dolore quam, quos hic explicabo
          obcaecati distinctio, tempore reprehenderit rem odit animi iure dolorum
          velit eum eligendi ipsa nisi. Sed fuga quos facere ipsum vel facilis
          esse omnis molestias ipsa ex consequatur praesentium odit qui corrupti
          distinctio quisquam odio dolore magnam fugit natus unde, ullam non
          assumenda. Commodi quas at debitis optio temporibus, et ut explicabo
          placeat officia illum!
        </h4>
      </div>
    </div>
  </Transition>
</template>

<script>
export default {
  name: "JobPage",
};
</script>

<style lang="scss" scoped>
.job-block {
  background: $color6;
  color: $color8;
  width: 96%;
  display: flex;
  padding-top: 15px;
  border-radius: 20px;
  padding-bottom: 15px;
  padding-left: 20px;
  justify-content: flex-start;
  gap: 20px;
  flex-direction: column;
}

.job-page-container {
  margin-top: 30px;
  border-radius: 20px;
  height: fit-content;
  background: $color2;
  display: flex;
  padding-top: 30px;
  padding-bottom: 30px;
  justify-content: center;
  align-items: center;
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
