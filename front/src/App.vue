<template>
  <header>
    <h1>Pixel Art Museum</h1>
  </header>
  <router-link to="/">Home</router-link>
  <router-link to="/edit_pixel/new"> | Edit</router-link>
  <router-link to="/load_canva"> | Your canvas</router-link>
  <router-view />
</template>

<script>
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");
* {
  font-family: "Press Start 2P", cursive;
}
</style>
