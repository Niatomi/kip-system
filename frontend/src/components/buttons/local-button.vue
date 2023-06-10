<template>
    <div class="local-button-container">
        <div class="btn btn__first" v-if="first">
            <h4><slot></slot></h4>
        </div>
        <div class="btn btn__last" v-if="last">
            <h4><slot></slot></h4>
        </div>
        <div class="btn" v-if="!(first | last)">
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
    },
}
</script>

<style lang="scss">
.local-button-container {
    width: 90%;
    display: flex;

}

.btn { 

    color: $color8;

    background: $color6;
    width: 100%;
    display: flex;
    flex: 1;
    justify-content: center;
    padding-left: 10px;
    padding-right: 10px;
    border-left: solid $color7;


    &__first {
    border-left: none;
    border-radius: 20px 0 0 20px;
    }

    &__last {
    border-radius: 0 20px 20px 0;
    }

    &:hover {
    background: $color7
    }


}
</style>