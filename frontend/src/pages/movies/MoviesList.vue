<template>
    <div
        class="newly-added-movies"
        ref="scrollContainer"
        @scroll="handleScroll"
    >
        <div
            v-if="isFetching && !hasMovies"
            class="no-movies"
        >
            <LoadingSpinner class="spinner"/>
        </div>

        <div
            v-else-if="hasMovies"
            class="movies-list"
        >
            <MovieItem
                v-for="movie in visibleMovies"
                :key="movie.id"
                :movie="movie"
                @click="$router.push(`/movies/${movie.id}`)"
            />
            <LoadingSpinner
                v-if="isFetching && hasMovies"
                class="spinner"
            />
        </div>

        <div
            v-else
            class="no-movies"
        >
            <i class="empty mdi mdi-popcorn"/>
            <p>No movies found</p>
        </div>
    </div>
</template>

<script>
import MovieItem from '../../components/MovieItem.vue';
import LoadingSpinner from '../../components/LoadingSpinner.vue';

export default {
    name: 'MoviesList',

    components: {
        MovieItem,
        LoadingSpinner,
    },

    emits: ['upload', 'load-more'],

    props: {
        movies: {
            type: Array,
            default: () => [],
        },

        isFetching: {
            type: Boolean,
            default: false,
        },
    },

    data() {
        return {
            pageSize: 12,
            currentPage: 1,
        };
    },

    computed: {
        hasMovies() {
            return this.movies && this.movies.length > 0;
        },

        visibleMovies() {
            return this.movies.slice(0, this.currentPage * this.pageSize);
        },
    },

    watch: {
        movies(newVal, oldVal) {
            if (newVal.length > oldVal.length) {
                this.currentPage++;
            }
        },
    },

    mounted() {
        this.$refs.scrollContainer.addEventListener('scroll', this.handleScroll);
    },

    beforeUnmount() {
        this.$refs.scrollContainer.removeEventListener('scroll', this.handleScroll);
    },

    methods: {
        handleScroll() {
            const container = this.$refs.scrollContainer;
            const nearBottom =
                container.scrollTop + container.clientHeight >= container.scrollHeight - 200;

            if (nearBottom && !this.isFetching) {
                this.$emit('load-more');
            }
        },
    },
};
</script>

<style scoped>
.newly-added-movies {
    background-color: #383852;
    border-radius: 20px;
    min-height: 200px;
    padding: 20px;
    max-height: 80vh;
    overflow-y: auto;

    .movies-list {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: center;
    }

    .no-movies {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;

        .empty {
            font-size: 100px;
            margin-bottom: -20px;
        }

        button {
            height: 40px;
        }
    }

    .spinner {
        margin-top: 20px;
    }
}
</style>
