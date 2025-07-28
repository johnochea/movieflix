<template>
    <div class="landing-page">
        <div class="header">
            <Header>
                <template #left>
                    <img
                        class="logo"
                        src="/movieflix-logo.svg"
                    />
                </template>
                <template #right>
                    <h3 v-if="firstName">
                        Welcome, {{ firstName }}!
                    </h3>
                    <button
                        class="logout-button"
                        @click="handleLogout"
                    >
                        <i class="mdi mdi-logout"/>
                        Log out
                    </button>
                </template>
            </Header>
        </div>
        <div class="home-body">
            <div class="movie-container">
                <div class="label">
                    <h1>Recently added</h1>
                    <button
                        v-if="newMovies.length"
                        class="add-movie-button"
                        @click="showUploadModal = true"
                    >
                        <i class="mdi mdi-movie"/>
                        Upload a movie
                    </button>
                </div>
                <div class="movie-component">
                    <NewlyAddedMovies
                        :is-fetching="isFetching"
                        :movies="newMovies"
                        @upload="showUploadModal = true"
                    />
                </div>
            </div>
            <div class="movie-container">
                <div class="label">
                    <h1>All movies</h1>
                    <div class="search">
                        <i class="mdi mdi-magnify"/>
                        <input
                            type="text"
                            placeholder="Search movie"
                            @input="store.searchMovies($event.target.value)"
                        />
                    </div>
                </div>
                <div class="movie-component">
                    <MoviesList
                        :movies="allMovies"
                        :isFetching="isFetching"
                        @load-more="fetchAllMovies"
                    />
                </div>
            </div>
        </div>
        <UploadModal
            v-if="showUploadModal"
            :visible="showUploadModal"
            :is-edit="false"
            @close="showUploadModal = false"
        />
    </div>
</template>

<script>
    import axios from 'axios'
    import { useStore } from '@/store/index.js';
    import API from '@/axios';

    import Header from '../components/Header.vue';
    import NewlyAddedMovies from '../pages/movies/NewlyAddedMovies.vue';
    import MoviesList from '../pages/movies/MoviesList.vue';
    import UploadModal from '../components/UploadModal.vue';

    export default {
        name: 'LandingPage',

        components: {
            Header,
            NewlyAddedMovies,
            MoviesList,
            UploadModal
        },

        data() {
            return {
                store: useStore(),
                showUploadModal: false,
                isFetching: false,
                newMovies: [],
                allMovies: [],
                currentPage: 1,
                hasNextPage: true,
            }
        },

        computed: {
            user() {
                return this.store.user;
            },

            firstName() {
                return this.user?.first_name;
            },
        },

        async created() {
            this.isFetching = true;
            await this.fetchUser();
            await this.fetchNewlyAddedMovies();
            await this.fetchAllMovies();
            this.isFetching = false;
        },

        methods: {
            async fetchUser() {
                try {
                    const response = await this.store.getUser();
                } catch (err) {
                    console.error(err)
                }
            },

            async fetchNewlyAddedMovies() {
                this.isFetching = true;
                try {
                    const response = await API.get('/movies/?ordering=-date_added&page_size=6');
                    if (!response.error) {
                        this.newMovies = response.data.results;
                    }
                } catch (err) {
                    console.error(err);
                } finally {
                    this.isFetching = false;
                }
            },

            async fetchAllMovies() {
                if (!this.hasNextPage || this.isFetching) return;

                this.isFetching = true;

                try {
                    const response = await API.get(`/movies/?ordering=title&page=${this.currentPage}`);
                    const results = response.data.results;
                    const next = response.data.next;

                    this.allMovies.push(...results);
                    console.log(this.allMovies)
                    this.currentPage++;
                    this.hasNextPage = !!next;
                } catch (error) {
                    console.error('Error loading more movies:', error);
                } finally {
                    this.isFetching = false;
                }
            },

            handleLogout() {
                this.store.logout();
                this.$router.push('/');
            },
        }
    }
</script>

<style scoped>
    .landing-page {
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100%;
        overflow-y: auto;

        .header {
            display: flex;
            width: 100%;

            .logo {
                height: 70px;
            }

            .logout-button {
                width: fit-content;
                height: 40px;
                font-size: 14px;
            }
        }

        .background-image {
            position: absolute;
            width: 100%;
            height: 100%;
            z-index: -1;
        }
        
        .home-body {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: rgba(31, 49, 59, 0.85);
            min-height: 100%;
            padding: 40px;

            .movie-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-items: center;
                width: 100%;

                .label {
                    display: flex;
                    width: 100%;
                    justify-content: space-between;

                    h1 {
                        justify-self: flex-start;
                    }

                    .search {
                        display: flex;
                        justify-self: flex-end;
                        align-items: center;
                        gap: 10px;

                        input {
                            height: 24px;
                            width: 360px;
                        }

                        i {
                            font-size: 32px;
                        }
                    }

                    button {
                        align-self: center;
                        justify-self: flex-end;
                        height: 40px;
                    }
                }

                .movie-component {
                    width: 100%;
                }
            }
            h2 {
                justify-self: left;
                color: white;
                font-size: 24px;
                font-weight: 500;
                margin-top: 20px;
            }
        }
    }
</style>
