import React from "react";
import ConditionalRender from "./components/ConditionalRender";
import RefExample from "./components/RefExample";
import { StyledH1 } from './components/StyledH1';

const App = () => (
  <div>
    <StyledH1>React!</StyledH1>
    <RefExample />
    <bdo dir="rtl">React!</bdo>
    <ConditionalRender />
  </div>
);

export default App;
