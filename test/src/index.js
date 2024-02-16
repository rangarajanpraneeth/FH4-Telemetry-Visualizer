import Chart from 'chart.js/auto'


const data = [
   // { year: 2010, count: 10 },
   // { year: 2011, count: 20 },
   // { year: 2012, count: 15 },
   // { year: 2013, count: 25 },
   // { year: 2014, count: 22 },
   // { year: 2015, count: 30 },
   // { year: 2016, count: 28 },
   // { year: 2017, count: 30 },
];

chart = new Chart(
   document.getElementById('acquisitions'),
   {
      type: 'line',
      data: {
         labels: data.map(row => row.year),
         datasets: [
            {
               label: 'Acquisitions by year',
               data: data.map(row => row.count)
            }
         ]
      }
   }
);

function addData(chart, label, newData) {
   chart.data.labels.push(label);
   chart.data.datasets.forEach((dataset) => {
       dataset.data.push(newData);
   });
   chart.update();
}

function charting() {
};


let yr = 0
let v = 0;
// for (i = 0; i < 100; i++) {
   // data.push({ year: yr, count: Math.random() * 100 })
   // console.log(yr)
   // charting()
// }
const PI = 3.14159265
setInterval(() => {
   addData(chart, yr, v)
   yr ++;
   v = Math.tan(yr)
   
}, 100);

