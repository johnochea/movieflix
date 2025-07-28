<template>
    <div class="newly-added-movies">
        <div
            v-if="isFetching"
            class="no-movies"
        >
            <LoadingSpinner class="spinner"/>
        </div>
        <div
            v-else-if="hasMovies && !isFetching" 
            class="movies-list"
        >
            <MovieItem
                v-for="movie in movies"
                :key="movie.id"
                :movie="movie"
                @click="$router.push(`/movies/${movie.id}`)"
            />
        </div>
        <div
            v-else
            class="no-movies"
        >
            <i class="empty mdi mdi-popcorn"/>
            <p>No movies at the moment</p>
            <button
                class="add-movie-button"
                @click="$emit('upload')"
            >
                <i class="mdi mdi-movie"/>
                Upload a movie
            </button>
        </div>
    </div>
</template>

<script>
    import MovieItem from '../../components/MovieItem.vue';
    import LoadingSpinner from '../../components/LoadingSpinner.vue';

    export default {
        name: 'NewlyAddedMovies',

        components: {
            MovieItem,
            LoadingSpinner,
        },

        emits: ['upload'],

        props: {
            movies: {
                type: Array,
                default: [],
            },

            isFetching: {
                type: Boolean,
                default: false,
            },
        },

        computed: {
            hasMovies() {
                return this.movies && this.movies.length > 0;
            },
        },
    }
</script>

<style scoped>
    .newly-added-movies {
        background-color: #383852;
        border-radius: 20px;
        min-height: 200px;
        padding: 20px;


        .movies-list {
            display: flex;
            flex-wrap: space-between;
            gap: 20px;
            justify-content: center;
        }

        .no-movies {
            display: flex;
            flex-direction: column;
            align-items: center;
            align-content: center;
            justify-content: center;

            .empty {
                font-size: 100px;
                margin-bottom: -20px;
                /* color: #BE4039; */
            }

            button {
                height: 40px;
            }
        }
    }
</style>