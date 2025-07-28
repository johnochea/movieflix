<template>
    <div class="banner">
        <i class="mdi mdi-alert-circle-outline" />
        <span>{{ message }}</span>
    </div>
</template>

<script>
    export default {
        name: 'ErrorBanner',

        props: {
            message: {
                type: String,
                required: true,
            },
        },
    };
</script>

<style scoped>
    .banner {
        display: flex;
        align-items: center;
        width: 100%;
        gap: 12px;
        min-height: 40px;
        padding: 4px 8px;
        border: 1px solid #BE4039;
        color: white;
        border-radius: 4px;
        background: #784259;
        /* background: #B94E56; */

        i {
            color: #BE4039;
        }
    }
</style>
