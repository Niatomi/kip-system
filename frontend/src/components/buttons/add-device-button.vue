<template>
    <div class="local-button-container">
        <div class="btn">
            <h4><slot></slot></h4>
        </div>
    </div>
</template>

<script>
export default {
    name: "LocalButton",
    props: {
        first: {
            type: Boolean,
            default: false
        },
        last: {
            type: Boolean,
            default: false
        },
        active: {
          type: Boolean,
          default: false
        }
    },
}
</script>

<style lang="scss" scoped>
.local-button-container {
    width: 100%;
    display: flex;

}

.btn { 

    color: $color8;
    border: none;
    background: $color4;
    display: flex;
    flex: 1;
    justify-content: center;
    padding-left: 10px;
    padding-right: 10px;
    border-radius: 20px;
    margin: 0;
    width: 100%;
    padding: 0;

}

</style>