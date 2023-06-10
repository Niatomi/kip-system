<template>
    <div class="feed-content-container">
        <slot></slot>
    </div>
</template>

<script>
export default {
    name: 'InfoFeed'
}
</script>

<style lang="scss">

.feed-content-container {
    display: flex;
    background: $color2;
    flex-direction: column;
    align-items: center;
    gap: 1%;
    border-radius: 20px;
    padding-top: 10px;
    padding-bottom: 10px;
    height: fit-content;
    width: 100% - 5;
}

</style>