function getNewData() {
    // get data from back-end using fetch
    // uri: http://127.0.0.1:4999/current-temp

    return fetch('http://127.0.0.1:4999/current-temp')
        .then((response) => response.json())
        .then((responseData) => {
            console.log(responseData);
            return responseData;
            })
        .catch(error => console.warn(error));
}



function setupNewChart() {
    const canvas = document.getElementById('temp-chart');
    const ctx = canvas.getContext('2d');
    const config = {
        type: 'line',
        data: {
            datasets: [{
            label: 'CPU temp (d\xB0C)',
            data: [],
            pointBackgroundColor: '#009900',
            backgroundColor: '#404040',
            fill: true,
            animations: false  // plural
            }]
        },
        labels: ['Green'],
        options: {
            parsing: {
                xAxisKey: 'datetime',
                yAxisKey: 'temp'
            }
        }
    }
    
    const newChart = new Chart(ctx, config);
    return newChart;
}

function refreshChart() {
    // assign programmatically the datasets again, otherwise data changes won't show
    getNewData()
        .then(
            response => {
                tempChart.data.datasets[0].data.push(response);
                if (tempChart.data.datasets[0].data.length > 100) {
                    tempChart.data.datasets[0].data.shift();
                }
                console.log(response);
                tempChart.update();
            }
        );
};

const tempChart = setupNewChart();

document.addEventListener("DOMContentLoaded", function(event) {
    window.setInterval(function(){
        refreshChart();
    }, 1000);
});