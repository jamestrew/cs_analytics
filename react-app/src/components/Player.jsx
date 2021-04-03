import { useEffect, useState } from "react";
import axios from "../utils/API";

export const Player = (props) => {
  const [data, setData] = useState([]);
  const xuid = props.match.params.xuid;
  const fetchUrl = "player/" + xuid;

  useEffect(() => {
    async function fetchData() {
      const request = await axios.get(fetchUrl);
      setData(request.data);
      return request;
    }
    fetchData();
  }, [fetchUrl]);

  return (
    <div>
      <h1>Hello {xuid}!</h1>
      <p>Kills: {data.kills}</p>
      <p>Deaths: {data.deaths}</p>
      <p>K/D: {data.kd_ratio}</p>
    </div>
  );
};
