import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    access: localStorage.getItem('access') || null,
  }),
  actions: {
    async login(username, password) {
      const res = await axios.post('http://localhost:8000/api/token/', {
        username,
        password,
      })
      this.access = res.data.access
      localStorage.setItem('access', res.data.access)
    },
    logout() {
      this.access = null
      localStorage.removeItem('access')
    }
  }
})
