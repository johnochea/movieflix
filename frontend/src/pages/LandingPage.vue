<template>
    <div class="landing-page">
        <div class="header">
            <Header>
                <template #left>
                    <img
                        class="logo"
                        src="/movieflix-logo.svg"
                    />
                    <router-link
                        to="/login"
                    >
                        FAQs
                    </router-link>
                    <router-link
                        to="/login"
                    >
                        About
                    </router-link>
                </template>
                <template #right>
                    <button
                        v-if="!isLoggedIn"
                        class="login-button"
                        @click="navigate('/login')"
                    >
                        Log in
                    </button>
                    <button
                        v-else
                        class="login-button"
                        @click="navigate('/home')"
                    >
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
                Sign up now
            </button>
            <button
                v-else
                class="signup-button"
                @click="navigate('/movies')"
            >
                View movies
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

        mounted() {
            this.validateAuth();
        },

        methods: {
            async handleSignup() {
                try {
                    const payload = {
                        first_name: this.firstName,
                        last_name: this.lastName,
                        email: this.email,
                        password: this.password,
                    };
                    await axios.post('http://localhost:8000/api/register/', payload);
                    alert('Account created! Please log in.');
                    this.$router.push('/login')
                } catch (error) {
                    console.log(error)
                    alert('Signup failed');
                }
            },

            navigate(path) {
                this.$router.push(path);
            },

            validateAuth() {
                const token = localStorage.getItem('access');
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
                height: 80px;
            }

            .login-button {
                width: fit-content;
                height: 40px;
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
                width: 120px;
                height: 48px;
                margin-bottom: 164px;
            }
        }
    }
</style>
