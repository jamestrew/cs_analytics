import { FC, useEffect, useState } from "react";
import { RouteComponentProps } from "react-router";
import { djangoAPI } from "../utils/API";

interface TParams {
  xuid: string;
}
interface Data {
  data: any;
}

export const PlayerSetup: FC<RouteComponentProps<TParams>> = (props) => {
  const [data, setData] = useState<Data>();
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

  return <div>{data && <Player data={data} />}</div>;
};

const Player: FC<Data> = ({ data }) => (
  <div>
    <img src={data["player"]["avatar"]} alt="avatar" />
    <h2>{data["player"]["personname"]}</h2>
  </div>
);
