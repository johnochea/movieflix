<template>
    <div class="form-container">
        <img
            class="logo"
            src="/movieflix-logo.svg"
        />
        <h1>Log in to your account</h1>
        <div class="error-container">
            <ErrorBanner
                v-if="errorMessage"
                :message="errorMessage"
            />
        </div>
        <form
            @submit.prevent="handleLogin"
        >
            <div class="field">
                <p class="label">
                    Email address
                </p>
                <input
                    v-model="accountDetails.email"
                    type="email"
                    placeholder="Enter email address"
                    @focus="errorMessage = ''"
                    required
                />
            </div>
            <div class="field">
                <p class="label">
                    Password
                </p>
                <input
                    v-model="accountDetails.password"
                    type="password"
                    placeholder="Enter password"
                    @focus="errorMessage = ''"
                    required
                />
            </div>
            <button
                class="login-button" 
                type="submit"
                :disabled="isLoading"
            >
                <LoadingSpinner 
                    v-if="isLoading"
                    class="spinner"
                />
                <span v-else>Log in</span>
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
    import { useStore } from '@/store/index.js';

    import LoadingSpinner from '../components/LoadingSpinner.vue';
    import ErrorBanner from '../components/ErrorBanner.vue';

    export default {
        name: 'LoginPage',

        components: {
            LoadingSpinner,
            ErrorBanner,
        },

        data() {
            return {
                store: useStore(),
                accountDetails: {
                    email: '',
                    password: '',
                },
                isLoading: false,
                errorMessage: '',
            }
        },

        methods: {
            async handleLogin() {
                this.isLoading = true;
                this.errorMessage = '';
                try {
                    const payload = {
                        username: this.accountDetails.email,
                        email: this.accountDetails.email,
                        password: this.accountDetails.password,
                    }
                    const response = await this.store.login(payload);
                    if (response.status === 200) {
                        this.$router.push('/home');
                    }
                } catch {
                    this.errorMessage = 'Invalid email or password.';
                }
                this.isLoading = false;
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

    .error-container {
        width: 515px;
        margin-left: -20px;
    }

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
