import justpy as jp
import pandas
from datetime import datetime 
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp']) 
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_average = data.groupby(['Week']).mean()

#copy code from highcharts documentation/charts/spline chart 
chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    #create an object of QuaserPage class
    wp = jp.QuasarPage()       

    #fill webpage using jp.QDiv            
    h1 = jp.QDiv(a=wp, text='Analysis of Course Review', classes='text-h1 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text='These graphs represent course review analysis')
    
    #fill webpage using highcharts library
    hc = jp.HighCharts(a=wp, options=chart_def)

    #change copied data using data structure manipulation
    hc.options.title.text = 'Average Rating per day' 
    hc.options.subtitle.text = 'According to udemy data'
    #x
    #y
    hc.options.xAxis.categories = list(week_average.index)
    hc.options.series[0].data =list(week_average['Rating'])
    hc.options.yAxis.title.text = 'Ratings'
    hc.options.xAxis.title.text = 'Week'
    hc.options.series[0].name = 'Average Rating'

    return wp

jp.justpy(app)       #it expects a function
