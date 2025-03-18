import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./styles.css";
import PageA from "./PageA";
import PageB from "./PageB";

const router = createBrowserRouter([{
    path: "/",
    element: <PageA/>
}, {
    path: "/page-b",
    element: <PageB/>
}]);

const rootNode = document.getElementById("root");
const root = createRoot(rootNode);
root.render(
    <RouterProvider router={router}/>
);