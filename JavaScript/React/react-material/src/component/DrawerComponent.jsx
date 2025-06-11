import React from "react";
import { Button, Drawer, Typography } from "@mui/material";
import { useState } from "react";
import { useCallback } from "react";

const DrawerComponent = () => {
    const [open, setOpen] = useState();

    const drawerHandler = useCallback(() => {
        setOpen(!open)
    }, [open])

    return <>
    <Drawer open={open} anchor="top">
        <Typography variant="h1">Content</Typography>
        <Button variant="outlined" onClick={drawerHandler}>Close</Button>

    </Drawer>
    <Button variant="contained" onClick={drawerHandler}>Open Drawer</Button>
    </>
}

export default DrawerComponent;