<template>
  <header>
    <h1>Pixel Art Museum</h1>
    <router-link to="/">Home</router-link>
    <router-link to="/edit_pixel/new"> | Edit</router-link>
  </header>
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
