const express = require("express");

const port = process.env.PORT || 3000;

const app = express();

app.use(express.json());
app.use(express.urlencoded());

app.get("/", (req, res) => {
    res.send("Hello");
});

app.listen(port, () => {
    console.log(`Running on port ${port}`);
});