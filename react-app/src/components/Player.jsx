import { useEffect, useState } from "react";
import { djangoAPI } from "../utils/API";

export const Player = (props) => {
  const [data, setData] = useState([]);
  const xuid = props.match.params.xuid;
  const fetchUrl = "player/" + xuid;

  useEffect(() => {
    const fetchData = async () => {
      const request = await djangoAPI.get(fetchUrl);
      setData(request.data);
      return request;
    };
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
