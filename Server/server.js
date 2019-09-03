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
  dataGPU = updateGpuData(function (err, dataGPU) {
    res.json(dataGPU);
  });
});

function updateGpuData(callback) {
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

// some other commands for later
// wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed, status
// wmic OS get TotalVisibleMemorySize,FreePhysicalMemory
// wmic diskdrive get name,size,model,description