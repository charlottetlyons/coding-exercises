import React, { useCallback, useState } from "react";
import { Drawer } from "@mui/material";

const DrawerComponent = () => {
    const [isOpen, setIsOpen] = useState(false)

    const drawerHandler = useCallback(() => {
        setIsOpen(!isOpen)
    }, [setIsOpen, isOpen])

    return <>
        <button onClick={drawerHandler}>Open Drawer</button>
        <Drawer open={isOpen} anchor="top">
            <h1>Drawer</h1>
            <button onClick={drawerHandler}>Close</button>
        </Drawer>
    </>
}

export default DrawerComponent;