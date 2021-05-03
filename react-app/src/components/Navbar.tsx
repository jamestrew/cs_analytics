import { FC } from "react";
import "../styles/index.css";

export const Navbar: FC = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark">
      <div className="container-fluid">
        <div className="row">
          <div className="col-2">
            <a className="navbar-brand" href="#">
              CS ANALYTICS

            </a>
          </div>
          <div className="col-10">
            <form className="d-flex">
              <input
                className="form-control me-2 bg-dark text-light"
                type="search"
                aria-label="Search Player"
              />
              <button className="btn btn-outline-success" type="submit">
                Search
              </button>
            </form>
          </div>
        </div>
      </div>
    </nav>
  );
};
