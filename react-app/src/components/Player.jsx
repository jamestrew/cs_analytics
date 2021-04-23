import { useEffect, useState } from "react";
// import { LargeCard } from "./LargeCard";
import { djangoAPI } from "../utils/API";

export const PlayerSetup = (props) => {
  const [data, setData] = useState();
  const xuid = props.match.params.xuid
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
      {data && <Player data={data} />}
    </div>
  );
};

const Player = ({ data }) => (
  <div>
    <img src={data['player']['avatar']} alt="avatar" />
    <h2>{data["player"]["personname"]}</h2>
  </div>
);
