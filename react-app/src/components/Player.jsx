import { useEffect, useState } from "react";
import { LargeCard } from "./LargeCard"
import { djangoAPI } from "../utils/API";

export const Player = (props) => {
  const [data, setData] = useState([]);
  const xuid = props.match.params.xuid;
  const fetchUrl = "player/" + xuid;

  useEffect(() => {
    const fetchDatt = async () => {
      const request = await djangoAPI.get(fetchUrl);
      setData(request.data);
      console.log(request.data)
      return request;
    };
    fetchData();
  }, [fetchUrl]);

  return (
    <div>
      <h1>Hello {xuid}!</h1>
      <LargeCard header="Kills/Death" mainStat={data.kd_ratio}/>
      <p>Kills: {data.kills}</p>
      <p>Deaths: {data.deaths}</p>
      <p>K/D: {data.kd_ratio}</p>
    </div>
  );
};
