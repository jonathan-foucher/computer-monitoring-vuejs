// imports
var express = require("express");
var cors = require('cors');
const { exec } = require("child_process");

var server = express();

// using cors to grant access for the client
server.use(cors());

// server listening on the port 3000
server.listen(3000, () => {
  console.log("Server running on port 3000");
});

// ====> GPU <====
// get response for gpu info
server.get("/getGpuInfo", (req, res, next) => {
  dataGpu = getGpuData(function (err, dataGpu) {
    var dataGpuArray = dataGpu.replace('timestamp', 'timestamp, ').replace(/(?:\\[rn]|[\r\n]+)+/g, "").split(', ');

    var dataGpuJson = new Object();
    for (var i = 0; i < dataGpuArray.length / 2; i++) {
      dataGpuJson[dataGpuArray[i].replace(' [%]', '').replace(' [MiB]', '').replace('.', '')] = dataGpuArray[dataGpuArray.length / 2 + i];
    }
    res.json(dataGpuJson);
  });
});

// get the gpu info from the system
function getGpuData(callback) {

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

// ====> CPU <====
// get response for cpu info
server.get("/getCpuInfo", (req, res, next) => {
  dataCpu = getCpuData(function (err, dataCpu) {
    var dataCpuArray = dataCpu.replace('VoltageCaps', 'VoltageCaps,').replace(/(?:\\[rn]|[\r\n]+)+/g, "").split(',');

    var dataCpuJson = new Object();
    for (var i = 0; i < dataCpuArray.length / 2; i++) {
      dataCpuJson[dataCpuArray[i].replace('/.//g', '')] = dataCpuArray[dataCpuArray.length / 2 + i];
    }

    dataCpuJson["dateTime"] = Date.now();
    res.json(dataCpuJson);
  });
});

// get the cpu info from the system
function getCpuData(callback) {

  exec(
    "wmic cpu get /format:csv",
    (err, stdout, stderr) => {
      if (err) {
        console.log(stderr);
      }
      return callback(null, stdout);
    }
  );
}