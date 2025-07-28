import { defineStore } from 'pinia';
import axios from 'axios';
import API from '@/axios'

export const useStore = defineStore('auth', {
  state: () => ({
    access_token: localStorage.getItem('access_token') || null,
    user: null,
    apiBaseUrl: 'http://localhost:8000/api'
  }),

  actions: {
    // Creates a new user account
    async register({ first_name, last_name, email, password }) {
      try {
        const response = await axios.post(`${this.apiBaseUrl}/register/`, 
          {
            first_name,
            last_name,
            email,
            password
          }
        );
        return response;
      } catch (error) {
        console.error("Error registering user:", error);
        throw error;
      }
    },

    // Logs in the user and fetches user data
    async login(payload) {
      const response = await axios.post(`${this.apiBaseUrl}/token/`, payload);

      if (response.status === 200) {
        this.access_token = response.data.access;
        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
      }

      return response;
    },
    
    // Logs out the current user
    logout() {
      this.access_token = null;
      this.user = null;
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
    },

    // Fetches the user data
    async getUser() {
      try {
        const response = await API.get('user/');

        if (response.status === 200 && response.data) {
          this.user = response.data;
        }
      } catch (err) {
        console.error('Failed to fetch user:', err)
        this.user = null;
      }
    }
  }
})
