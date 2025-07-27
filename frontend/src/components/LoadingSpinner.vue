<template>
    <div class="loading-spinner">
        <div class="spinner"></div>
    </div>
</template>

<script>
    export default {
        name: 'LoadingSpinner',
    };
</script>

<style scoped>
    .loading-spinner {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 20px;
        height: 20px;
    }

    .spinner {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        position: relative;
        display: inline-block;

        &:after,
        &:before {
            content: '';
            display: block;
            border-radius: 50%;
            width: 20px;
            height: 20px;
        }

        &:before {
            position: absolute;
            top: 0;
            left: 0;
            border-width: 3px;
        }

        &:after {
            position: absolute;
            top: 0;
            left: 0;
            border: 4px solid transparent;
            border-top-color: white;
            border-bottom-color: white;
            animation: spin 1s ease-in-out infinite;
            border-width: 3px;
        }
    }

    @keyframes spin {
        0% {
            transform: rotate(0deg);
        }

        100% {
            transform: rotate(360deg);
        }
    }
</style>
