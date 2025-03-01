import React from "react";
import { Grid2 as Grid, Typography } from "@mui/material";

const App = () => {
    return (
        <Grid container columns="2">
            <Grid size="grow">
                <Typography variant="h1">React!</Typography>
            </Grid>
            <Grid size="grow">
                <Typography variant="h2">React!</Typography>
            </Grid>
        </Grid>
    )
};

export default App;
