import { BrowserRouter, Route } from "react-router-dom";
import { PlayerSetup } from "./components/Player";
import { useEffect } from "react";

const Home = () => <h1>WElcome to cS ANalYTics</h1>;

export const App = () => {
  useEffect(() => {
    document.title = "CS ANALYSIS";
    document.body.classList.toggle("bg-dark", true);
    document.body.classList.toggle("text-light", true);
  });

  return (
    <div className="container-fluid">
      <BrowserRouter>
        <Route exact path="/" component={Home} />
        <Route path="/player/:xuid" component={PlayerSetup} />
      </BrowserRouter>
    </div>
  );
};
