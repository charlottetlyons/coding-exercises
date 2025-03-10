import React from "react";
import { Grid2 as Grid, Typography } from "@mui/material";
import StyledMuiH1 from "./component/StyledMuiH1";

const App = () => {
    return (
        <Grid container columns="2">
            <Grid size="grow">
                <StyledMuiH1>React!</StyledMuiH1>
            </Grid>
            <Grid size="grow">
                <Typography variant="h2">React!</Typography>
            </Grid>
        </Grid>
    )
};

export default App;
