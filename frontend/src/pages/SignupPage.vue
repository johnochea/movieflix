<template>
    <div class="form-container">
        <img
            class="logo"
            src="/movieflix-logo.svg"
        />
        <h1>Create your account</h1>
        <form
            @submit.prevent="handleSignup"
        >
            <div class="name-container">
                <div class="field">
                    <p class="label required">
                        First Name
                    </p>
                    <input
                        v-model="firstName"
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
                        v-model="lastName"
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
                    v-model="email"
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
                    v-model="password"
                    type="password"
                    placeholder="Enter password"
                    required
                />
            </div>
            <div class="button-container">
                <button
                    class="signup-button" 
                    type="submit"
                >
                    Sign Up
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
    import { mapActions } from 'pinia';

    export default {
        name: 'SignupPage',

        data() {
            return {
                firstName: '',
                lastName: '',
                email: '',
                password: '',
            }
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
                    await axios.post(`${this.$apiBaseUrl}/register/`, payload);
                    alert('Account created! Please log in.');
                    this.$router.push('/login')
                } catch (error) {
                    console.log(error)
                    alert('Signup failed');
                }
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

    .logo {
        width: 150px;
        margin-bottom: -5px;
    }

    .name-container {
        display: flex;
        flex-direction: row;
        margin-bottom: -5px;

        .name-input {
            min-width: 240px;
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
