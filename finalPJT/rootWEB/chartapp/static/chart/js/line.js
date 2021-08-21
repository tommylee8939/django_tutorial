Highcharts.chart('container', {
      chart: {
        type: 'spline'
      },
      title: {
        text: 'Monthly Average Temperature'
      },
      subtitle: {
        text: 'Source: WorldClimate.com'
      },
      xAxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
      },
      yAxis: {
        title: {
          text: 'Temperature'
        },
        labels: {
          formatter: function () {
            return this.value + '°';
          }
        }
      },
      tooltip: {
        crosshairs: true,
        shared: true
      },
      plotOptions: {
        spline: {
          marker: {
            radius: 4,
            lineColor: '#666666',
            lineWidth: 1
          }
        }
      },
      series: [{
        name: '서울',
        marker: {
          symbol: 'square'
        },
        data: seoul

      }, {
        name: 'London',
        marker: {
          symbol: '런던'
        },
        data: london
      }]
    });