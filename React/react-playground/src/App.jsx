import React from "react";
import ConditionalRender from "./components/ConditionalRender";
import RefExample from "./components/RefExample";
import { StyledH1 } from './components/StyledH1';
import VerticalWriting from "./components/VerticalWriting";

const App = () => (
  <div>
    <StyledH1>React!</StyledH1>
    <RefExample />
    <bdo dir="rtl">React!</bdo>
    <ConditionalRender />
    <VerticalWriting>Here we are</VerticalWriting>
  </div>
);

export default App;
