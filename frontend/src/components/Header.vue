<template>
    <div class="header">
        <div class="left-slot">
            <slot name="left" />
        </div>
        <div class="right-slot">
            <slot name="right" />
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Header',
    }
</script>

<style scoped>
    .header {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        align-items: center;
        background-color: #383852;
        padding: 20px 30px;
        height: 48px;
        /* width: 100%; */
    }

    .left-slot {
        flex: 1;
        display: flex;
        justify-content: flex-start;
    }

    .right-slot {
        flex: 1;
        display: flex;
        justify-content: flex-end;
    }
</style>