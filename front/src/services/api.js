import config from "/config.js";
import { v4 as uuidv4 } from "uuid";

export function getUserId() {
  const userJson = localStorage.getItem("auth");
  const user = JSON.parse(userJson);
  console.log(user);
  return user.id;
}
export function getUserName() {
  const userJson = localStorage.getItem("auth");
  const user = JSON.parse(userJson);
  return user.name;
}
export async function get_canva_by_id(id) {
  const settings = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: getUserId(),
    },
  };
  const response = await fetch(`${config.API_PATH}/canva/${id}`, settings);
  return await response.json();
}
export async function get_canva() {
  const settings = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: getUserId(),
    },
  };
  const response = await fetch(`${config.API_PATH}/load_canva`, settings);
  const canvas = await response.json();
  return canvas;
}
export async function canva_post(canva) {
  canva.id = uuidv4();
  const settings = {
    method: "POST",
    body: JSON.stringify(canva),
    headers: {
      "Content-Type": "application/json",
      Authorization: getUserId(),
    },
  };
  let response = await fetch(`${config.API_PATH}/canvas`, settings);
  return response;
}
export async function delete_canva(id) {
  const settings = {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      Authorization: getUserId(),
    },
  };
  let response = await fetch(`${config.API_PATH}/load_canva/${id}`, settings);
  return response;
}

export async function users_post(register) {
  register.id = uuidv4();
  const settings = {
    method: "POST",
    body: JSON.stringify(register),
    headers: {
      "Content-Type": "application/json",
      Authorization: getUserId(),
    },
  };
  let response = await fetch(`${config.API_PATH}/users`, settings);
  return response;
}
