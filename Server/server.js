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
server.get("/getGpuInfo", (req, res, next) => {
  dataGpu = getGpuData(function (err, dataGpu) {
    var dataGpuArray = dataGpu.replace('\n', ', ').split(', ');
   
    var dataGpuJson = new Object();
    for (var i = 0; i < dataGpuArray.length / 2; i++) {
      dataGpuJson[dataGpuArray[i].replace('\r', '').replace('\n', '').replace('.', '')] = dataGpuArray[dataGpuArray.length / 2 + i].replace('\r', '').replace('\n', '');
    }
    res.json(dataGpuJson);
  });
});

function getGpuData(callback) {
  const { exec } = require("child_process");
  exec(
    "nvidia-smi --query-gpu=gpu_name,temperature.gpu,memory.used,memory.total,utilization.gpu,utilization.memory,timestamp --format=csv",
    (err, stdout, stderr) => {
      if (err) {
        console.log(stderr);
      }
      return callback(null, stdout);
    }
  );
}