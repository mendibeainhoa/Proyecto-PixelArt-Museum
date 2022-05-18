import config from "/config.js";
import { v4 as uuidv4 } from "uuid";

export async function get_canva_by_id(id) {
  const settings = {
    method: "GET",
  };
  const response = await fetch(`${config.API_PATH}/canva/${id}`, settings);
  return await response.json();
}
export async function get_canva() {
  const settings = {
    method: "GET",
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
  };
  await fetch(`${config.API_PATH}/canva`, settings);
}
