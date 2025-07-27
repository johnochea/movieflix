<template>
    <div class="form-container">
        <img
            class="logo"
            src="/movieflix-logo.svg"
        />
        <h1>Log in to your account</h1>
        <form
            @submit.prevent="handleLogin"
        >
            <div class="field">
                <p class="label">
                    Email address
                </p>
                <input
                    v-model="email"
                    type="email"
                    placeholder="Enter email address"
                    required
                />
            </div>
            <div class="field">
                <p class="label">
                    Password
                </p>
                <input
                    v-model="password"
                    type="password"
                    placeholder="Enter password"
                    required
                />
            </div>
            <button
                class="login-button" 
                type="submit"
            >
                Log in
            </button>
        </form>
        <p>
            New to Movieflix?
            <router-link
                class="hyperlink"
                to="/signup"
            >
                Create an account
            </router-link>
        </p>
    </div>
</template>

<script>
    import axios from 'axios';
    import { mapActions } from 'pinia';

    export default {
        name: 'LoginPage',

        data() {
            return {
                email: '',
                password: '',
            }
        },

        methods: {
            ...mapActions('auth', ['login']),

            async handleLogin() {
                try {
                    const payload = {
                        username: this.email,
                        email: this.email,
                        password: this.password
                    }
                    const response = this.login(payload);
                    if (!response.error) {
                        localStorage.setItem('access', response.data.access);
                        this.$router.push('/dashboard');
                    }
                } catch (error) {
                    alert('Login failed');
                }
            }
        }
    }
</script>

<style scoped>
.form-container {
    display: flex;
    flex-direction: column;
    background-color: #383852;
    border-radius: 20px;
    margin-top: 80px;
    padding: 20px;
    align-items: center;
    text-align: center;

    .logo {
        width: 150px;
        margin-bottom: -5px;
    }

    .label {
        margin-bottom: 5px;
        justify-self: left;
    }

    .field {
        margin: 10px;
    }

    .login-button {
        width: 530px;
        height: 48px;
        margin-top: 15px;
    }
}

</style>
