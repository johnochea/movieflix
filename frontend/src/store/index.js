import { defineStore } from 'pinia';
import axios from 'axios';

export const useStore = defineStore('auth', {
  state: () => ({
    access_token: localStorage.getItem('access_token') || null,
    user: null,
    apiBaseUrl: 'http://localhost:8000/api'
  }),

  actions: {
    // Creates a new user account
    async register({ first_name, last_name, email, password }) {
      console.log("registering user")
      console.log(first_name)
      try {
        const response = await axios.post(`${this.apiBaseUrl}/register/`, 
          {
            first_name,
            last_name,
            email,
            password
          }
        );
        if (response.status === 201) {
          const userAccount = {
            email: response.data.email,
            username: response.data.username,
            password: password
          };

          const loginResponse = await this.login(userAccount);
          return loginResponse
        }
      } catch (error) {
        console.error("Error registering user:", error);
        throw error;
      }
    },

    // Logs in the user and fetches user data
    async login(payload) {
      console.log("logging in")
      const response = await axios.post(`${this.apiBaseUrl}/token/`, payload);

      if (response.status === 200) {
        this.access_token = response.data.access;
        localStorage.setItem('access_token', response.data.access);
      }

      return response;
    },
    
    // Logs out the current user
    logout() {
      console.log("logging out")
      this.access_token = null;
      this.user = null;
      localStorage.removeItem('access_token');
    },

    // Fetches the user data
    async getUser() {
      console.log("getting user")
      try {
        const res = await axios.get(`${this.apiBaseUrl}/user/`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`
          }
        })
        console.log("user data:", res.data)
        this.user = res.data;
      } catch (err) {
        console.error('Failed to fetch user:', err)
        this.user = null;
      }
    }
  }
})
