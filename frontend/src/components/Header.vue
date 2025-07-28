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
        align-items: center;
        justify-content: space-between;
        background-color: #383852;
        padding: 20px 30px;
        height: 48px;
        position: sticky;
    }

    .left-slot {
        flex: 1;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        gap: 20px;
    }

    .right-slot {
        flex: 1;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 20px;
    }
</style>