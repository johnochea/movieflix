<template>
    <div class="movie-item">
        <img
            class="movie-poster"
            :src="movie.thumbnail"
            :alt="`${movie.title} poster`"
        />
        <div class="movie-details">
            <h2>{{ movie.title }}</h2>
            <p> {{ dateAdded }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Header',

        props: {
            movie: {
                type: Object,
                required: true,
            },
        },

        computed: {
            dateAdded() {
                return new Date(this.movie.date_added).toLocaleDateString();
            },
        }
    }
</script>

<style scoped>
    .movie-item {
        padding: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        background-color: #383852;
        border-radius: 10px;

        .movie-poster {
            width: 180px;
            height: 240px;
        }

        .movie-details {
            text-align: center;
            margin-top: 10px;

            h2 {
                font-size: 16px;
                margin: 0;
            }

            p {
                margin-top: -5px;
                font-size: 14px;
                color: #ccc;
            }
        }
    }

    .movie-item:hover {
        background-color: #4a4862;
        cursor: pointer;
    }
</style>