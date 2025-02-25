import React, { useState, useRef } from "react";
import ConditionalRender from "./components/ConditionalRender";
import RefExample from "./components/RefExample";
import { StyledH1 } from './components/StyledH1';
import VerticalWriting from "./components/VerticalWriting";
import ReverseWriting from "./components/ReverseWriting";
import { AppContext } from "./context/AppContext";
import ContextComponent from "./components/ContextComponent";

const App = () => {
  const [contextState,  setContextState] = useState("poached eggs");

  return <AppContext.Provider value={{contextState, setContextState}}>
    <StyledH1>React!</StyledH1>
    <RefExample />
    <ReverseWriting/>
    <ConditionalRender />
    <VerticalWriting>Here we are</VerticalWriting>
    <ContextComponent/>
  </AppContext.Provider>
};

export default App;
