import React from "react";
import ConditionalRender from "./components/ConditionalRender";
import RefExample from "./components/RefExample";

const App = () => (
  <div>
    <h1>React!</h1>
    <RefExample />
    <bdo dir="rtl">React!</bdo>
    <ConditionalRender />
  </div>
);

export default App;
