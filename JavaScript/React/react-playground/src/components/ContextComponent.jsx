import React, { useContext } from "react";
import { AppContext } from "../context/AppContext";

const ContextComponent = () => {
    const appContext = useContext(AppContext);
    
    return <p>{appContext.contextState}</p>
}

export default ContextComponent;