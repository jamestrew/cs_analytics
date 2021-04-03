import { useState, useEffect } from "react";
import axios from "../utils/API";

export const Player = (props) => {
  const [map, setMap] = useState();
  const xuid = props.match.params.xuid;

  useEffect(() => {
    async function fetchData() {
      const request = await axios.get(xuid);
      console.log(request);
      return request;
    }
    fetchData();
  }, [xuid]);

  return <h1>Hello {xuid}!</h1>;
};
