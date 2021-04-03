import { BrowserRouter, Route } from "react-router-dom";
import { Player } from "./components/Player";

const Home = () => <h1>WElcome to cS ANalYTics</h1>;

export const App = () => (
  <BrowserRouter>
    <Route exact path="/" component={Home} />
    <Route path="/player/:xuid" component={Player} />
  </BrowserRouter>
);
