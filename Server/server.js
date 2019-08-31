// imports
var express = require("express");
var cors = require('cors');
var server = express();

// using cors to grant access to the client
server.use(cors());

// server listening on the port 3000
server.listen(3000, () => {
    console.log("Server running on port 3000");
});

// get
server.get("/url", (req, res, next) => {
    res.json("First api test");
});