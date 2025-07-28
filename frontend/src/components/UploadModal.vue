<template>
    <div class="overlay">
        <div class="form-container">
            <h1>{{ isEdit ? 'Edit Movie' : 'Upload Movie' }}</h1>

            <div class="error-container">
                <ErrorBanner
                    v-if="errorMessage"
                    :message="errorMessage"
                />
            </div>

            <form @submit.prevent="handleSubmit">
                <div class="field">
                    <p class="label required">Title</p>
                    <input
                        v-model="movieForm.title"
                        type="text"
                        placeholder="Enter movie title"
                        required
                    />
                </div>

                <div class="field">
                    <p class="label required">Description</p>
                    <textarea
                        v-model="movieForm.description"
                        placeholder="Enter description"
                        required
                    ></textarea>
                </div>

                <div class="field">
                    <p :class="['label', {'required': !isEdit}]">
                        Video File
                    </p>
                    <input
                        type="file"
                        @change="handleVideoUpload"
                        accept="video/*"
                        :required="!isEdit"
                    />
                </div>
                <div class="field">
                    <p class="label">Thumbnail</p>
                    <input
                        type="file"
                        @change="handleThumbnailUpload"
                        accept="image/*"
                    />
                </div>

                <div class="button-container">
                    <button
                        type="submit"
                        class="upload-button"
                        :disabled="isLoading"
                    >
                        <LoadingSpinner
                            v-if="isLoading"
                            class="spinner"
                        />
                        <span v-else>{{ isEdit ? 'Update' : 'Upload' }}</span>
                    </button>
                    <button
                        type="button"
                        class="cancel-button"
                        @click="close"
                    >
                        Cancel
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import API from '@/axios';
import ErrorBanner from '@/components/ErrorBanner.vue';
import LoadingSpinner from '@/components/LoadingSpinner.vue';

export default {
    name: 'MovieModal',

    components: {
        ErrorBanner,
        LoadingSpinner,
    },

    props: {
        isEdit: {
            type: Boolean,
            default: false,
        },

        movieData: {
            type: Object,
            default: null,
        }
    },

    emits: ['close', 'refresh'],

    data() {
        return {
            movieForm: {
                title: '',
                description: '',
                video_file: null,
                thumbnail: null,
            },
            isLoading: false,
            errorMessage: '',
        };
    },
    
    created() {
        if (this.isEdit && this.movieData) {
            this.initializeData();
        }
    },

    methods: {
        initializeData() {
            this.movieForm.title = this.movieData.title;
            this.movieForm.description = this.movieData.description;
        },

        handleVideoUpload(e) {
            this.movieForm.video_file = e.target.files[0];
        },

        handleThumbnailUpload(e) {
            this.movieForm.thumbnail = e.target.files[0];
        },

        async handleSubmit() {
            this.isLoading = true;
            this.errorMessage = '';
            const formData = new FormData();

            formData.append('title', this.movieForm.title);
            formData.append('description', this.movieForm.description);
            if (this.movieForm.video_file) {
                formData.append('video_file', this.movieForm.video_file);
            }
            if (this.movieForm.thumbnail) {
                formData.append('thumbnail', this.movieForm.thumbnail);
            }

            try {
                if (this.isEdit && this.movieData?.id) {
                    await API.put(`movies/${this.movieData.id}/`, formData);
                } else {
                    await API.post('movies/', formData);
                }
                this.$emit('refresh');
                this.close();
            } catch (error) {
                console.error('Failed:', error);
                this.errorMessage = 'Something went wrong. Please try again.';
            }

            this.isLoading = false;
        },

        close() {
            this.movieForm = {
                title: '',
                description: '',
                video_file: null,
                thumbnail: null,
            };
            this.errorMessage = '';
            this.$emit('close');
        },
    }
};
</script>

<style scoped>
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
}

.form-container {
    position: absolute;
    display: flex;
    flex-direction: column;
    align-self: center;
    justify-self: center;
    background-color: #383852;
    border-radius: 20px;
    margin-top: 0px;
    padding: 10px;
    align-items: center;
    text-align: center;
    width: 400px;

    .error-container {
        width: 320px;
        margin-bottom: 15px;
    }

    .field {
        margin: 10px 0;
        width: 100%;
        text-align: left;
    }

    input[type="text"],
    textarea,
    input[type="file"] {
        width: 100%;
        padding: 10px;
        border-radius: 8px;
        border: none;
    }

    textarea {
        resize: vertical;
    }

    .label {
        margin-bottom: 5px;
        font-weight: bold;

        &.required::after {
            content: '*';
            color: red;
            margin-left: 4px;
        }
    }

    .button-container {
        margin-top: 20px;
        display: flex;
        gap: 10px;
        justify-content: flex-end;
        margin-bottom: 10px;
        margin-right: -30px;

        .upload-button,
        .cancel-button {
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            font-weight: bold;
        }

        .cancel-button {
            background-color: #f0f0f0;
            color: #333;
            cursor: pointer;
        }

        .cancel-button:hover {
            background-color: #e0e0e0;
        }
    }
}
</style>
