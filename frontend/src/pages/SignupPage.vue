<template>
    <div class="form-container">
        <img
            class="logo"
            src="/movieflix-logo.svg"
        />
        <h1>Create your account</h1>
        <div class="error-container">
            <ErrorBanner
                v-if="errorMessage"
                :message="errorMessage"
            />
        </div>
        <form
            @submit.prevent="handleSignup"
        >
            <div class="name-container">
                <div class="field">
                    <p class="label required">
                        First Name
                    </p>
                    <input
                        v-model="accountDetails.firstName"
                        class="name-input"
                        type="text"
                        placeholder="Enter first name"
                        required
                    />
                </div>
                <div class="field">
                    <p class="label required">
                        Last Name
                    </p>
                    <input
                        v-model="accountDetails.lastName"
                        class="name-input"
                        type="text"
                        placeholder="Enter last name"
                        required
                    />
                </div>
            </div>
            <div class="field">
                <p class="label required">
                    Email address
                </p>
                <input
                    v-model="accountDetails.email"
                    type="email"
                    placeholder="Enter email address"
                    required
                />
            </div>
            <div class="field">
                <p class="label required">
                    Password
                </p>
                <input
                    v-model="accountDetails.password"
                    type="password"
                    placeholder="Enter password"
                    required
                />
            </div>
            <div class="button-container">
                <button
                    class="signup-button" 
                    type="submit"
                    :disabled="isLoading"
                >
                    <LoadingSpinner 
                        v-if="isLoading"
                        class="spinner"
                    />
                    <span v-else>Sign up</span>
                </button>
            </div>
        </form>
        <p>
            Already have an account?
            <router-link
                class="hyperlink"
                to="/login"
            >
                Log in
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
        name: 'SignupPage',

        components: {
            LoadingSpinner,
            ErrorBanner,
        },

        data() {
            return {
                store: useStore(),
                accountDetails: {
                    firstName: '',
                    lastName: '',
                    email: '',
                    password: '',
                },
                isLoading: false,
                errorMessage: '',
            }
        },

        methods: {
            async handleSignup() {
                this.isLoading = true;
                try {
                    const payload = {
                        first_name: this.accountDetails.firstName,
                        last_name: this.accountDetails.lastName,
                        email: this.accountDetails.email,
                        password: this.accountDetails.password,
                    };
                    const response = await this.store.register(payload);
                    if (response.error) {
                        this.errorMessage = 'Email address already registered. Try logging in instead.';
                    } else {
                        this.$router.push('/login');
                    }
                } catch (error) {
                    console.error('Error during signup:', error);
                }
                this.isLoading = false;
            }
        }
    }
</script>

<style>
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

    .name-container {
        display: flex;
        flex-direction: row;
        margin-bottom: -5px;

        .name-input {
            width: 240px;
        }
    }

    .label {
        margin-bottom: 5px;
        justify-self: left;

        &.required::after {
            content: '*';
            color: red;
            padding-left: 3px;
        }
    }

    .field {
        margin: 10px;
    }

    .signup-button {
        width: 530px;
        height: 48px;
        margin-top: 15px;
    }
}

</style>
