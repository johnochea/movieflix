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
                    <p> Welcome, {{ firstName }}!</p>
                    <button
                        class="logout-button"
                        @click="handleLogout"
                    >
                        <i class="mdi mdi-account-circle-outline"/>
                        Log out
                    </button>
                </template>
            </Header>
        </div>
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
    import { mapActions } from 'pinia';
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

        computed: {
            firstName() {
                return this.user?.first_name;
            },
        },

        mounted() {
            this.validateAuth();
            this.fetchUser();
        },

        methods: {
            ...mapActions('auth', ['logout']),

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
                    router.push('/login')
                }
            },

            handleLogout() {
                this.logout();
                this.$router.push('/login');
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
                height: 40px;
                margin-bottom: 164px;
            }
        }
    }
</style>
