import React from "react";
import { Link } from "react-router-dom";

export interface NavigationProps {}

export const Navigation: React.FC<NavigationProps> = () => {
  return (
    <nav className="navbar">
      <div className="navbar-group">
        <Link to="/index">Index</Link>
      </div>
    </nav>
  );
};

export default Navigation;
