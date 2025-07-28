<template>
    <div class="landing-page">
        <div class="header">
            <Header>
                <template #left>
                    <img
                        class="logo"
                        src="/movieflix-logo.svg"
                    />
                    <router-link to="/">
                        FAQs
                    </router-link>
                    <router-link to="/">
                        About
                    </router-link>
                    <router-link to="/">
                        Contact us
                    </router-link>
                </template>
                <template #right>
                    <button
                        v-if="!isLoggedIn"
                        class="login-button"
                        @click="navigate('/login')"
                    >
                        <i class="mdi mdi-account-circle-outline"/>
                        Log in
                    </button>
                    <button
                        v-else
                        class="login-button"
                        @click="navigate('/home')"
                    >
                        <i class="mdi mdi-home-outline"/>
                        Go to home
                    </button>
                </template>
            </Header>
        </div>
        <img
            class="background-image"
            src="/src/assets/backgrounds/landing-page-cover.jpg"
        />
        <div class="landing-body">
            
            <p class="landing-welcome">
                Welcome to
            </p>
            <img
                class="logo-text"
                src="/movieflix-text.svg"
            />
            <p class="landing-text">
                Discover and enjoy tons of movies.
                <br/>
                Experience a whole new world of cinema with Movieflix.
            </p>
            <p>
                Ready to start watching?
            </p>
            <button
                v-if="!isLoggedIn"
                class="signup-button"
                @click="navigate('/signup')"
            >
                <i class="mdi mdi-account-box-outline"/>
                Sign up now
            </button>
            <button
                v-else
                class="signup-button"
                @click="navigate('/movies')"
            >
                <i class="mdi mdi-compass-outline"/>
                Explore movies
            </button>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import Header from '../components/Header.vue'

    export default {
        name: 'LandingPage',

        components: {
            Header,
        },

        data() {
            return {
                isLoggedIn: false,
            }
        },

        created() {
            this.validateAuth();
        },

        methods: {
            navigate(path) {
                this.$router.push(path);
            },

            validateAuth() {
                const token = localStorage.getItem('access_token');
                if (token) {
                    this.isLoggedIn = true;
                }
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

        .header {
            display: flex;
            width: 100%;

            .logo {
                height: 70px;
            }

            .login-button {
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
        
        .landing-body {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: rgba(31, 49, 59, 0.85);
            min-height: 100%;

            .landing-welcome {
                margin-top: 148px;
                font-size: 36px;
                font-weight: bold;
            }

            .logo-text {
                width: 600px;
                margin-top: -250px;
            }

            .landing-text {
                font-size: 24px;
                margin-top: -100px;
                text-align: center;
            }

            .signup-button {
                width: fit-content;
                height: 48px;
                margin-bottom: 164px;
                font-size: 14px;
            }
        }
    }
</style>
