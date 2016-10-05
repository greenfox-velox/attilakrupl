google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ['Age', 'Number of people'],
    ['0-18', 1],
    ['19-25', 1],
    ['26-35', 7],
    ['36-45', 5],
    ['46-55', 1],
    ['over 55', 0]
  ]);

  var options = {
    title: 'My contacts sorted by age',
    pieHole: 0.4,
  };

  var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
  chart.draw(data, options);
}
