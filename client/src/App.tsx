import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./Pages/Home";
import About from "./Pages/About";
import Navigation from "./Components/Navigation";

function App() {
  return (
    <Router>
      <div>
        <p>Test</p>
        <Navigation />
      </div>
      <Routes>
        <Route path="/About">
          <About />
        </Route>
        <Route path="/">
          <Home />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
