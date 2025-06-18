<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Username" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Register</button>
    </form>
    <p v-if="message">{{ message }}</p>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      message: '',
      error: ''
    };
  },
  methods: {
    register() {
      axios
        .post('http://localhost:8000/api/register/', {
          username: this.username,
          password: this.password
        })
        .then(() => {
          this.error = '';
          this.message = 'Registration successful! Please log in.';
          // Optionally, redirect to the login view or clear fields.
        })
        .catch((error) => {
          console.error('Registration error:', error);
          this.error = 'Registration failed. Try a different username.';
        });
    }
  }
};
</script>

<style scoped>
/* Basic styling */
</style>