<template>
  <header>
    <h1>Pixel Art Museum</h1>

    <link
      href="https://unpkg.com/nes.css@2.3.0/css/nes.min.css"
      rel="stylesheet"
    />
  </header>
  <router-link to="/">Home</router-link>
  <router-link to="/edit_pixel/new"> Edit</router-link>
  <!-- <router-link to="/load_canva"> Your canvas</router-link> -->
  <router-link to="/users"> New register</router-link>
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
