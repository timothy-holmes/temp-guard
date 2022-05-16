
    function setupNewChart(tempData) {
        const canvas = document.getElementById('temp-chart');
        const ctx = canvas.getContext('2d');
        const config = {
            type: 'line',
            data: {
                labels: tempData.DateTimes,
                datasets: [{
                label: 'Users created',
                data: tempData.Temps,
                borderColor: 'green',
                backgroundColor: '#404040',
                fill: true,
                animations: false // <-- now plural, instead of "animation" before
                }]
            }
        }
        
        const myLineChart = new Chart(ctx, config);
    }

    function updateChart() {
        // assign programmatically the datasets again, otherwise data changes won't show
        myLineChart.data.labels = tempData.DateTimes;
        myLineChart.data.datasets[0].data = tempData.Temps;

        myLineChart.update();
    };

    function updateData() {
        // get data for back-end
        // using fetch -- uri: http://127.0.0.1:4999/current-temp
        // add new point to tempData arrays, but clip oldest point if too many points (max 100?)
    }

    function initialize() {
        // this needs a while loop to make sure there is at least one point before moving on
        updateData();
        // new at least one point before chart setup can occur
        setupNewChart();
    }

    function refreshCanvas() {
        updateData();
        updateChart();
    }