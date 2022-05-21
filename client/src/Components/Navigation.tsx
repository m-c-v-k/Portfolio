import React from "react";
import { Link } from "react-router-dom";

export interface NavigationProps {}

export const Navigation: React.FC<NavigationProps> = () => {
  return (
    <nav className="navbar">
      <div className="navbar-group">
        <Link to="/Home" type="button" className="navigation-btn">
          Home
        </Link>
        <Link to="/About" type="button" className="navigation-btn">
          About
        </Link>
        <p>hmmm</p>
      </div>
    </nav>
  );
};

export default Navigation;
