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
                    <button
                        class="login-button"
                        @click="$router.push('/login')"
                    >
                        Log in
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
                Discover and enjoy over {{ movieCount }} movies.
                <br/>
                Experience a whole new world of cinema with Movieflix.
            </p>
            <p>
                Ready to start your cinematic journey?
            </p>
            <button
                class="signup-button"
                @click="$router.push('/signup')"
            >
                Sign up now
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
                user: null,
            }
        },

        mounted() {
            this.validateAuth();
            this.fetchUser();
        },

        methods: {
            validateAuth() {
                const token = localStorage.getItem('access');
                if (!token) {
                    this.$router.push('/login');
                    return;
                }
            },

            async fetchUser() {
                try {
                const res = await axios.get('http://localhost:8000/api/user/', {
                headers: {
                    Authorization: `Bearer ${token}`
                }
                })
                user.value = res.data
            } catch (err) {
                console.error(err)
                router.push('/login') // Token may be invalid/expired
            }
            }
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
                width: 80px;
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
