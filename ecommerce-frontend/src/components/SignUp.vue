<template>
    <div style="text-align: center;">
        <img class="SignUplogo" alt="Restaurant logo" src="../assets/img/applogo.png" />
    </div>
    <div class="overlay">
        <div class="popup-container">
            <main>
                <div class="form-container">
                    <h1 style="margin-bottom: 10px;">Sign Up</h1>

                    <form id="loginForm" @submit.prevent="handleSignIn">
                        <div class="input-group">
                            <svg-icon class="input-icon" type="mdi" :path="acc" />
                            <input v-model="username" placeholder="Username" required />
                        </div>

                        <div class="input-group">
                            <svg-icon class="input-icon" type="mdi" :path="pass" />
                            <input v-model="password" type="password" placeholder="Password" required />
                        </div>

                        <p v-if="error" class="error">{{ error }}</p>
                        <p v-if="message">{{ message }}</p>

                        <button type="submit" class="signin-btn">Register</button>

                        <p class="login-link">
                            Already have an Account?
                            <a href="#" @click.prevent="goToSignIn">SIGN IN</a>
                        </p>
                    </form>
                </div>
            </main>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import SvgIcon from '@jamescoyle/vue-icon'
import { mdiAccount, mdiFormTextboxPassword } from '@mdi/js'

export default {
    data() {
        return {
            acc: mdiAccount,
            pass: mdiFormTextboxPassword,
            username: '',
            password: '',
            message: '',
            error: ''
        };
    },
    components: { SvgIcon },
    methods: {
        goToSignIn() {
            this.$router.push('/SignIn');
        },
        register() {
            axios.post('http://localhost:8000/api/register/', {
                username: this.username,
                password: this.password
            }).then(() => {
                this.error = '';
                this.message = 'Registration successful! Please log in.';
                this.$router.push('/SignIn');
            }).catch((error) => {
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