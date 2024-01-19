const fs = require('fs'); //json
const path = require('path');
const PORT = 2693;
const HOST = '127.0.0.1';

const dgram = require('dgram');
let server = dgram.createSocket('udp4');

const fToC = f => (f - 32) * 5 / 9;

let fileCounter = 0;


const parsePackets = packets => {
   return {
      inRace: packets.readInt32LE(0), // 1 in race 0 not in race
      timestamp: packets.readInt32LE(4), // can overflow to 0 eventually

      engineMaxRPM: packets.readFloatLE(8),
      engineIdleRPM: packets.readFloatLE(12),
      engineRPM: packets.readFloatLE(16),

      carAccelerationX: packets.readFloatLE(20), // X=left/right Y=up Z=forward
      carAccelerationY: packets.readFloatLE(24),
      carAccelerationZ: packets.readFloatLE(28),

      carVelocityX: packets.readFloatLE(32), // X=left/right Y=up Z=forward
      carVelocityY: packets.readFloatLE(36),
      carVelocityZ: packets.readFloatLE(40),

      carAngularVelocityX: packets.readFloatLE(44), // X=left/right Y=up Z=forward
      carAngularVelocityY: packets.readFloatLE(48),
      carAngularVelocityZ: packets.readFloatLE(52),

      carYaw: packets.readFloatLE(54),
      carPitch: packets.readFloatLE(60),
      carRoll: packets.readFloatLE(64),

      suspensionTravelNormalizedFL: packets.readFloatLE(68), // 0.0f=max stretch 1.0=max compression
      suspensionTravelNormalizedFR: packets.readFloatLE(72),
      suspensionTravelNormalizedRL: packets.readFloatLE(76),
      suspensionTravelNormalizedRR: packets.readFloatLE(80),

      tireSlipRatioFL: packets.readFloatLE(84), // 0(100% grip) |ratio| > 1 (loss of grip)
      tireSlipRatioFR: packets.readFloatLE(88),
      tireSlipRatioRL: packets.readFloatLE(92),
      tireSlipRatioRR: packets.readFloatLE(96),

      wheelRotationSpeedFL: packets.readFloatLE(100), // radians per second
      wheelRotationSpeedFR: packets.readFloatLE(104),
      wheelRotationSpeedRL: packets.readFloatLE(108),
      wheelRotationSpeedRR: packets.readFloatLE(112),

      wheelOnRumbleFL: packets.readInt32LE(116), // 1(true) 0(false)
      wheelOnRumbleFR: packets.readInt32LE(120),
      wheelOnRumbleRL: packets.readInt32LE(124),
      wheelOnRumbleRR: packets.readInt32LE(128),

      wheelInPuddleDepthFL: packets.readFloatLE(132), // 0(shallowest) 1(deepest)
      wheelInPuddleDepthFR: packets.readFloatLE(136),
      wheelInPuddleDepthRL: packets.readFloatLE(140),
      wheelInPuddleDepthRR: packets.readFloatLE(144),

      forceFeedbackRumbleFL: packets.readFloatLE(148),
      forceFeedbackRumbleFR: packets.readFloatLE(152),
      forceFeedbackRumbleRL: packets.readFloatLE(156),
      forceFeedbackRumbleRR: packets.readFloatLE(160),

      tireSlipAngleFL: packets.readFloatLE(164), // 0(100% grip) |angle| > 1 (loss of grip)
      tireSlipAngleFR: packets.readFloatLE(168),
      tireSlipAngleRL: packets.readFloatLE(172),
      tireSlipAngleRR: packets.readFloatLE(176),

      tireSlipCombinedFL: packets.readFloatLE(180), // 0(100% grip) |slip| > 1 (loss of grip)
      tireSlipCombinedFR: packets.readFloatLE(184),
      tireSlipCombinedRL: packets.readFloatLE(188),
      tireSlipCombinedRR: packets.readFloatLE(192),

      suspensionTravelFL: packets.readFloatLE(196), // meters
      suspensionTravelFR: packets.readFloatLE(200),
      suspensionTravelRL: packets.readFloatLE(204),
      suspensionTravelRR: packets.readFloatLE(208),

      carID: packets.readInt32LE(212),
      carPerformanceClass: packets.readInt32LE(216), // 0(D)-7(X)
      carPerformanceIndex: packets.readInt32LE(220), // 100-999
      carDrivetrainType: packets.readInt32LE(224), // 0=FWD 1=RWD 2=AWD
      carCylinderCount: packets.readInt32LE(228),

      carPositionX: packets.readFloatLE(244),
      carPositionY: packets.readFloatLE(248),
      carPositionZ: packets.readFloatLE(252),

      carSpeed: Math.round(packets.readFloatLE(256)), // meters per second
      enginePower: packets.readFloatLE(260) / 746, // watts
      engineTorque: packets.readFloatLE(264), // newton meters

      tireTemperatureFL: fToC(packets.readFloatLE(268)), // farenheit
      tireTemperatureFR: fToC(packets.readFloatLE(272)),
      tireTemperatureRL: fToC(packets.readFloatLE(276)),
      tireTemperatureRR: fToC(packets.readFloatLE(280)),

      engineBoost: packets.readFloatLE(284),
      engineFuel: packets.readFloatLE(288),

      distanceTravelled: packets.readFloatLE(292),

      raceBestLap: packets.readFloatLE(296),
      raceLastLap: packets.readFloatLE(300),
      raceCurrentLap: packets.readFloatLE(304),
      raceTime: packets.readFloatLE(308),
      raceLap: packets.readUint16LE(312),
      racePosition: packets.readUintLE(314, 1),

      inputThrottle: packets.readUintLE(315, 1),
      inputBrake: packets.readUintLE(316, 1),
      inputClutch: packets.readUintLE(317, 1),
      inputHandbrake: packets.readUintLE(318, 1),
      inputGear: packets.readUintLE(319, 1),
      inputSteering: packets.readIntLE(320, 1),

      normalizedDrivingLine: packets.readIntLE(321, 1),
      normalizedAIBrakeDifference: packets.readInt16LE(322)
   }
}

const renderVisualizer = data => { }

server.on('listening', () => {
   let address = server.address();
   console.log(`Listening on ${address.address}:${address.port}`);
});

let headers = 'inRace,timestamp,engineMaxRPM,engineIdleRPM,engineRPMcarAccelerationX,carAccelerationY,carAccelerationZcarVelocityX,carVelocityY,carVelocityZcarAngularVelocityX,carAngularVelocityY,carAngularVelocityZcarYaw,carPitch,carRollsuspensionTravelNormalizedFL,suspensionTravelNormalizedFR,suspensionTravelNormalizedRL,suspensionTravelNormalizedRRtireSlipRatioFL, tireSlipRatioFR,tireSlipRatioRL,tireSlipRatioRRwheelRotationSpeedFL, wheelRotationSpeedFR,wheelRotationSpeedRL,wheelRotationSpeedRR,wheelOnRumbleFL,wheelOnRumbleFR,wheelOnRumbleRL,wheelOnRumbleRRwheelInPuddleDepthFL,wheelInPuddleDepthFR,wheelInPuddleDepthRL,wheelInPuddleDepthRRforceFeedbackRumbleFL,forceFeedbackRumbleFR,forceFeedbackRumbleRL,forceFeedbackRumbleRRtireSlipAngleFL,tireSlipAngleFR,tireSlipAngleRL,tireSlipAngleRRtireSlipCombinedFL,tireSlipCombinedFR,tireSlipCombinedRL,tireSlipCombinedRRsuspensionTravelFL,suspensionTravelFR,suspensionTravelRL,suspensionTravelRRcarID,carPerformanceClass,carPerformanceIndex,carDrivetrainType,carCylinderCountcarPositionX,carPositionY,carPositionZcarSpeed,enginePower,engineTorquetireTemperatureFL,tireTemperatureFR,tireTemperatureRL,tireTemperatureRRengineBoost,engineFueldistanceTravelledraceBestLap,raceLastLap,raceCurrentLap,raceTime,raceLap,racePositioninputThrottle,inputBrake,inputClutch,inputHandbrake,inputGear,inputSteeringnormalizedDrivingLine,normalizedAIBrakeDifference';

let raceData = '';

server.on('message', packets => {
   const data = parsePackets(packets);
   renderVisualizer(data);
   let newData = ({
      timestamp: data.timestamp,
      posX: data.carPositionX,
      posY: data.carPositionY,
      posZ: data.carPositionZ,
      speed: data.carSpeed,
      throttle: data.inputThrottle,
      brake: data.inputBrake,
      clutch: data.inputClutch,
      handbrake: data.inputHandbrake,
      gear: data.inputGear,
      steering: data.inputSteering
   });
   let x = Object.values(data).join(',');
      // pushCSV('creampie.csv', x);
   if(inRace == 1)
      raceData += ('\n' + x);
   // if (JSON.stringify(newData) !== '{}') {
   //    // uploadJSONDatabase(`raceData1.json`, file);
   //    raceData.push(newData);
   // }

   // console.log(data);
});

server.bind(PORT, HOST);

process.on('SIGINT', () => {
   pushCSV('raceData2.json', raceData);

   console.log(`Exiting...`);
   process.exit();
});

// function getJSON(file) { //gets data from JSON file in a useable format
//    const filePath = path.join(__dirname, '../../database', file);
//    return JSON.parse(fs.readFileSync(filePath));
// }

// function uploadJSONDatabase(file, data) { //overwrites JSON file and uploads with data
//    const filePath = path.join(__dirname, '../../database', file);
//    fs.writeFileSync(filePath, JSON.stringify(data, null, 2), {
//       encoding: 'utf8',
//       flag: 'w'
//    });
//    console.log("Upload complete");
//    return fs.readdirSync(path.join(__dirname, '../../database'));
// }


function getCSV(file) {
   const filePath = path.join(__dirname, '../../database', file);
   const csvData =  fs.readFileSync(filePath, 'utf-8');
   const rows = csvData.split('\r\n').map(row => row.split(','));

   const header = rows[0];
   const jsonData = rows.slice(1).map(row => {
       const obj = {};
       header.forEach((key, index) => {
           obj[key] = row[index];
       });
       return obj;
   });

   return jsonData;
}

function pushCSV(file, csvData) {
   const filePath = path.join(__dirname, '../../database', file);

   let existingData = fs.readFileSync(filePath)
   let newData = existingData + '\n' + csvData;
   fs.writeFileSync(filePath, newData, {
       encoding: 'utf8',
       flag: 'w'
   });

   // console.log("Upload complete");
}

function startRecording() {
   
   fileCounter++;
}