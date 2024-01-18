// const fs = require('fs')
// const path = require('path')

// function getCSV(file) {
//     const filePath = path.join(__dirname, './database', file);
//     const csvData =  fs.readFileSync(filePath, 'utf-8');
//     const rows = csvData.split('\r\n').map(row => row.split(','));

//     const header = rows[0];
//     const jsonData = rows.slice(1).map(row => {
//         const obj = {};
//         header.forEach((key, index) => {
//             obj[key] = row[index];
//         });
//         return obj;
//     });

//     return jsonData;
// }

// function pushCSV(file, csvData) {
//     const filePath = path.join(__dirname, './database', file);

//     existingData = fs.readFileSync(filePath)
//     newData = existingData + '\n' + csvData;
//     fs.writeFileSync(filePath, newData, {
//         encoding: 'utf8',
//         flag: 'w'
//     });

//     console.log("Upload complete");
// }

// uploadCSV('creampie.csv', '4,9,0')

// // let x = (getCSV('creampie.csv'));
// // x[0].a = '99';
// // uploadJSONcsv('creampie.csv', x);
// // console.log(getCSV('creampie.csv'));
