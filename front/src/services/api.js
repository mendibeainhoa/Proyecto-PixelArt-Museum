import config from "/config.js";

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
  const settings = {
    method: "POST",
    body: JSON.stringify(canva),
    headers: {
      "Content-Type": "application/json",
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
    },
  };
  let response = await fetch(`${config.API_PATH}/load_canva/${id}`, settings);
  return response;
}
