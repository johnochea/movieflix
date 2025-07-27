import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    access_token: localStorage.getItem('access_token') || null,
    user: null,
  }),

  mutations: {
    setUser(state, user) {
      state.user = user
    },
    clearUser(state) {
      state.user = null
    }
  },

  actions: {
    // Creates a new user account
    async register(payload) {
      console.log("registering user")
      try {
        const response = await axios.post(`${this.$apiBaseUrl}/register/`, payload);
        console.log("User registered successfully:", res.data);
        return res.data;
      } catch (error) {
        console.error("Error registering user:", error);
        throw error;
      }
    },

    // Logs in the user and fetches user data
    async login(payload) {
      console.log("logging in")
      const response = await axios.post(`${this.$apiBaseUrl}/token/`, payload);
      this.access_token = response.data.access;
      localStorage.setItem('access_token', response.data.access);

      commit('getUser')
    },
    
    // Logs out the current user
    logout() {
      console.log("logging out")
      this.access_token = null;
      localStorage.removeItem('access_token');
    },

    // Fetches the user data
    async getUser() {
      console.log("getting user")
      try {
        const res = await axios.get(`${this.$apiBaseUrl}/user/`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`
          }
        })
        commit('setUser', res.data)
      } catch (err) {
        console.error('Failed to fetch user:', err)
        commit('clearUser')
      }
    }
  }
})
