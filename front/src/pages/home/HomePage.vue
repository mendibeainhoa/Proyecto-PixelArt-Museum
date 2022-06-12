<template>
  <section>
    <router-link to="/users" class="register"> Register</router-link>
    <h1 class="main-title">Welcome to PixelArt Museum</h1>
  </section>
  <link
    href="https://unpkg.com/nes.css@2.3.0/css/nes.min.css"
    rel="stylesheet"
  />
  <section class="login">
    <h2 class="access-title">Sing in</h2>
    <label> Usuario </label>
    <input type="text" v-model="name" />
    <label> Password </label>
    <input type="password" v-model="password" />
    <button class="access-button" @click="onAccessButton">Acceder</button>
  </section>
  <canvas id="snow"></canvas>
</template>

<script>
import { login } from "@/services/auth.js";

export default {
  name: "Home",
  data() {
    return {
      name: "",
      password: "",
    };
  },
  methods: {
    isNotAllowedAccessEmptyInputs() {
      if (this.name === "" || this.password === "") {
        return false;
      } else {
        return true;
      }
    },
    async onAccessButton() {
      if (!this.isNotAllowedAccessEmptyInputs()) {
        alert(" Acceso denegado: los campos estan vacios ");
        return;
      }
      let response = await login(this.name, this.password);
      console.log(response);
      let statusLogin = response.status;

      if (statusLogin === 200) {
        this.$router.push("/load_canva");
      } else {
        alert("Acceso denegado");
      }
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");
* {
  font-family: "Press Start 2P", cursive;
  padding: 0;
  margin: 0;
}

.main-title {
  font-size: 20px;
  margin-top: 4em;
  margin-bottom: 2em;
}
.access-title {
  font-size: 30px;
}
.login {
  border: solid black 1px;
  display: grid;
  place-content: center;
  margin: 25em;
}
.login,
label {
  padding: 1em;
}
.login,
input {
  background-color: #eee;
  padding: 12px 15px;
}
.login,
.access-button {
  margin-top: 1em;
  border-radius: 20px;
  border: 1px solid #24232362;
  background-color: #3a333262;
  color: #ffffff;
  font-size: 12px;
  font-weight: bold;
  padding: 12px 45px;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  outline: none;
  box-shadow: 0 9px #999;
}
.access-button:hover {
  background-color: #242221ce;
}
</style>