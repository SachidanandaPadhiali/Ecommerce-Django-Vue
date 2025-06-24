<template>
  <div id="app">
    <router-view />
  </div>
</template>


<script>
export default {
  name: 'App'
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body {
  font-family: "Varela Round", sans-serif;
}

:root {
  --box-bg: #666B85;
  --hover-bg: #5e5e5e;
  --text-dark: #1B1E24;
  --text-light: #c7c7c7;
  --primary: #703d13;
  --accent: #a79a27;
  --black: #111111;
  --hover: #faa560;
  --dark-text: #111827;
  --light-text: #6B7280;
  --white-text: #FFFFFF;
  --bg: #F9FAFB;
  --bg-grey: #D2D1D2;
  --bg-dark: #393f45;
  --bg-btn: #cca161;
  --card-bg: #FFFFFF;
  --border: #D1D5DB;
  --success: #10B981;
  --warning: #F59E0B;
  --error: #EF4444;
  --info: #3B82F6;
  --transparent-accent: rgba(33, 169, 173, 0.25);
  --transparent: rgba(255, 255, 255, 0.5);

  /*===== Font and typography =====*/
  --text: 'Poppins', sans-serif;
  --font-family: "Poppins", sans-serif;
  --biggest-font-size: 2.5rem;
  --h1-font-size: 1.5rem;
  --h2-font-size: 1.25rem;
  --h3-font-size: 1.125rem;
  --normal-font-size: 1rem;
  --small-font-size: 0.8rem;
  --smaller-font-size: 0.7rem;

  /*===== Font weight =====*/
  --font-slim: 100;
  --font-medium: 400;
  --font-semi-bold: 550;
  --font-bold: 700;

  /*===== Margins =====*/
  --mb-0: 0.1rem;
  --mb-1: 0.5rem;
  --mb-2: 1rem;
  --mb-3: 1.5rem;
  --mb-4: 2rem;
  --mb-5: 2.5rem;
  --mb-6: 3rem;

  /* Effects */
  --glow: 0 0 10px var(--primary-glow);
  --glass: saturate(180%) blur(10px);
  --gradient: linear-gradient(135deg, var(--surface), rgba(40, 40, 60, 0.95));

  /* Timing */
  --transition-fast: 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-medium: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}
.product-list {
    padding: 2rem;
}

.product-list.loading {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

.loader-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    width: 100%;
}

.loading {
    position: relative;
    background: currentcolor;
    width: 0.25em;
    height: 0.5em;
    margin: 0 0.5em;
    animation: loading 1s ease-in-out infinite;
    animation-delay: 0.4s;
}

.loading:after,
.loading:before {
    content: "";
    position: absolute;
    width: inherit;
    height: inherit;
    background: inherit;
    -webkit-animation: inherit;
    animation: inherit;
}

.loading:before {
    right: 0.5em;
    -webkit-animation-delay: 0.2s;
    animation-delay: 0.2s;
}

.loading:after {
    left: 0.5em;
    -webkit-animation-delay: 0.6s;
    animation-delay: 0.6s;
}

@-webkit-keyframes loading {

    0%,
    100% {
        box-shadow: 0 0 0 currentcolor, 0 0 0 currentcolor;
    }

    50% {
        box-shadow: 0 -0.25em 0 currentcolor, 0 0.25em 0 currentcolor;
    }
}

@keyframes loading {

    0%,
    100% {
        box-shadow: 0 0 0 currentcolor, 0 0 0 currentcolor;
    }

    50% {
        box-shadow: 0 -0.25em 0 currentcolor, 0 0.25em 0 currentcolor;
    }
}

h2 {
    text-align: center;
    margin-bottom: 1rem;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
}

.product img {
    width: auto;
    max-width: 220px;
    height: auto;
    max-height: 140px;
    object-fit: cover;
}

.prod_detail {
    margin-top: 10px;
    position: absolute;
    bottom: 0;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.star-rating {
    display: flex;
    gap: 4px;
}

.star {
    width: 24px;
    height: 24px;
}

.error {
    color: var(--error);
    text-align: center;
    margin-top: 1rem;
}

.badge {
    position: absolute;
    top: 10px;
    right: 10px;
    background: linear-gradient(to right,
            rgba(169, 3, 41, 1) 0%,
            rgba(196, 72, 72, 1) 44%,
            rgba(170, 34, 56, 1) 100%);
    color: #fff;
    padding: 5px 10px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    border-radius: 10px;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
    z-index: 10;
}

.product {
    position: relative;
    height: 300px;
    text-align: center;
    background-color: var(--bg);
    min-width: 250px;
    margin: 15px;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
    cursor: pointer;
    padding-top: 10px;
}

.product:hover {
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15), 0 3px 6px rgba(0, 0, 0, 0.24);
    transform: translateY(-3px);

    img {
        transform: scale(1.05);
    }

    .myBtn {
        background-color: var(--hover);
    }
}

.logout-btn {
  margin: 10px;
  float: right;
  padding: 10px 30px;
  border: none;
  border-radius: 50px;
  font-size: var(--normal-font-size);
  font-weight: var(--font-semi-bold);
  background-color: var(--bg-dark);
  color: white;
  cursor: pointer;
}

</style>