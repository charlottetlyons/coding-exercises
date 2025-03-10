import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import "./styles.css";

const rootNode = document.getElementById("root");
const root = createRoot(rootNode);
root.render(
    <BrowserRouter>
        <App />
    </BrowserRouter>
);