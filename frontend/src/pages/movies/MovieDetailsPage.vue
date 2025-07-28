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
                        class="logout-button"
                        @click="handleLogout"
                    >
                        <i class="mdi mdi-logout"/>
                        Log out
                    </button>
                </template>
            </Header>
        </div>

    <div class="home-body" v-if="movie">
      <h2>{{ movie.title }}</h2>
      <video
        v-if="movie.video_file"
        controls
        class="video-player"
        :src="movie.video_file"
      ></video>
      <p>{{ movie.description }}</p>

      <div class="actions">
        <button @click="showUploadModal = true">
          <i class="mdi mdi-pencil" />
            Edit
        </button>
        <button @click="deleteMovie">
          <i class="mdi mdi-delete" />
            Delete
        </button>
      </div>
    </div>

    <UploadModal
      v-if="showUploadModal"
      :visible="showUploadModal"
      :is-edit="true"
      :movie-data="movie"
      @close="showUploadModal = false"
      @refresh="fetchMovie"
    />
  </div>
</template>

<script>
import Header from '../../components/Header.vue';
import UploadModal from '../../components/UploadModal.vue';
import { useStore } from '@/store/index.js';
import API from '@/axios.js';

export default {
  name: 'MovieDetailPage',

  components: {
    Header,
    UploadModal,
  },

  data() {
    return {
      store: useStore(),
      movie: null,
      showUploadModal: false,
    };
  },

  created() {
    this.fetchUser();
    this.fetchMovie();
  },

  methods: {
    async fetchUser() {
      try {
        await this.store.getUser();
      } catch (err) {
        console.error(err);
      }
    },

    async fetchMovie() {
      const id = this.$route.params.id;
      try {
        const response = await API.get(`/movies/${id}/`);
        this.movie = response.data;
      } catch (err) {
        console.error('Failed to fetch movie:', err);
      }
    },

    async deleteMovie() {
      const confirmDelete = confirm('Are you sure you want to delete this movie?');
      if (!confirmDelete) return;

      try {
        await API.delete(`/movies/${this.movie.id}/`);
        alert('Movie deleted');
        this.$router.push('/home');
      } catch (err) {
        console.error('Delete failed:', err);
        alert('Failed to delete movie.');
      }
    },

    handleLogout() {
      this.store.logout();
      this.$router.push('/');
    },
  },
};
</script>

<style scoped>
.landing-page {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  overflow-y: auto;
}

.header {
  display: flex;
  width: 100%;
}

.logo {
  height: 70px;
}

.logout-button {
  width: fit-content;
  height: 40px;
  font-size: 14px;
}

.home-body {
  padding: 40px;
  background-color: rgba(31, 49, 59, 0.85);
  display: flex;
  flex-direction: column;
  align-items: center;
  color: white;

  h2 {
    font-size: 24px;
    margin-bottom: 10px;
  }

  .video-player {
    width: 100%;
    max-width: 720px;
    margin-bottom: 20px;
  }

  .actions {
    display: flex;
    gap: 10px;

    button {
      height: 40px;
      display: flex;
      align-items: center;
      gap: 5px;
    }
  }
}
</style>
