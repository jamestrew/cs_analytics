import axios from "axios";
import { steamKey } from "./keys";

export const djangoAPI = axios.create({
  baseURL: "http://127.0.0.1:8000/",
});

const steamURL =
  "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" +
  steamKey +
  "&steamids=";
export const steamAPI = axios.create({
  baseURL: steamURL,
});
