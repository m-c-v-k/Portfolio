import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { About } from "./Pages/About";
import { Index } from "./Pages/Index";
import { Navigation } from "./Components/Navigation";

function App() {
  return (
    <Router>
      <div>
        <Navigation />
      </div>
      <Routes>
        <Route path="/About">
          <About />
        </Route>
        <Route path="/">
          <Index />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
