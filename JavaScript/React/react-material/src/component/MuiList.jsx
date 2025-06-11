import React from "react";
import { List, ListItem, ListItemIcon, ListItemText } from "@mui/material";
import DeckIcon from '@mui/icons-material/Deck';
import PregnantWomanIcon from '@mui/icons-material/PregnantWoman';
import BlenderIcon from '@mui/icons-material/Blender';

const MuiList = () => {
    return <List>
        <ListItem>
            <ListItemIcon><DeckIcon/></ListItemIcon>
            <ListItemText primary="Patio" />
        </ListItem>
        <ListItem>
            <ListItemIcon><PregnantWomanIcon/></ListItemIcon>
            <ListItemText primary="Pregnant Woman" />
        </ListItem>
        <ListItem>
            <ListItemIcon><BlenderIcon/></ListItemIcon>
            <ListItemText primary="Blend" />
        </ListItem>
    </List>
}

export default MuiList;