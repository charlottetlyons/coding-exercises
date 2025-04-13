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
import ParallaxComponent from "./components/ParallaxComponent";
import BlurredEdgesElement from "./components/BlurredEdgesElement";
import DrawerComponent from "./components/DrawerComponent";
import AppKiller from "./components/AppKiller";
import useInputValidation from "./hooks/useTestHook"

const App = () => {
  const [contextState, setContextState] = useState("poached eggs");

  const { validate } = useInputValidation();

  return (
    <AppContext.Provider value={{ contextState, setContextState }}>
      <ErrorBoundary>
        <input onChange={(event) => validate(event.target.value)}/>
        {/* <AppKiller/> */}
        <StyledH1>React!</StyledH1>
        <RefExample />
        <ReverseWriting />
        <ConditionalRender />
        <TextDecorationExample />
        <VerticalWriting>Here we are</VerticalWriting>
        <ContextComponent />
        <BlurredEdgesElement />
        <DrawerComponent />
        <ParallaxComponent/>
      </ErrorBoundary>
    </AppContext.Provider>
  );
};

export default App;
