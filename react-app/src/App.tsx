import { BrowserRouter, Route } from "react-router-dom";
import { PlayerSetup } from "./components/Player";
import { Navbar } from "./components/Navbar";
import { FC, useEffect } from "react";

const Home: FC = () => {
  return (
    <>
      <Navbar />
    </>
  );
};

export const App: FC = () => {
  useEffect(() => {
    document.title = "CS ANALYSIS";
    document.body.classList.toggle("bg-dark", true);
    document.body.classList.toggle("text-light", true);
  });

  return (
    <>
      <BrowserRouter>
        <Route exact path="/" component={Home} />
        <Route path="/player/:xuid" component={PlayerSetup} />
      </BrowserRouter>
    </>
  );
};
