import React from "react";
import { Grid2 as Grid, Typography } from "@mui/material";
import StyledMuiH1 from "./component/StyledMuiH1";
import MuiList from "./component/MuiList";
import DrawerComponent from "./component/DrawerComponent";

const App = () => {
    return (
        <Grid container direction="column">
            <Grid size="grow">
                <StyledMuiH1>React!</StyledMuiH1>
            </Grid>
            <Grid size="grow">
                <Typography variant="h2">React!</Typography>
            </Grid>
            <Grid size="grow">
                <MuiList/>
            </Grid>
            <Grid size="grow">
                <DrawerComponent/>
            </Grid>
        </Grid>
    )
};

export default App;
