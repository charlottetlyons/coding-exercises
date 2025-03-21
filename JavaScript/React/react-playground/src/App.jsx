import React, { useState } from "react";
import ConditionalRender from "./components/ConditionalRender";
import RefExample from "./components/RefExample";
import { StyledH1 } from "./components/StyledH1";
import VerticalWriting from "./components/VerticalWriting";
import ReverseWriting from "./components/ReverseWriting";
import { AppContext } from "./context/AppContext";
import ContextComponent from "./components/ContextComponent";
import ErrorBoundary from "./components/ErrorBoundary";
import TextDecorationExample from "./components/TextDecorationExample";
import AppKiller from "./components/AppKiller";

const App = () => {
  const [contextState, setContextState] = useState("poached eggs");

  return (
    <AppContext.Provider value={{ contextState, setContextState }}>
      <ErrorBoundary>
        {/* <AppKiller/> */}
        <StyledH1>React!</StyledH1>
        <RefExample />
        <ReverseWriting />
        <ConditionalRender />
        <TextDecorationExample />
        <VerticalWriting>Here we are</VerticalWriting>
        <ContextComponent />
      </ErrorBoundary>
    </AppContext.Provider>
  );
};

export default App;
