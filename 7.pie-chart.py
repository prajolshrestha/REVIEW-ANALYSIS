import justpy as jp
import pandas
from datetime import datetime 
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp']) 
share = data.groupby(['Course Name'])['Rating'].count()

#copy code from highcharts documentation/charts/spline chart 
chart_def = """
{
    chart: {
        
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in May, 2020'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 70.67,
            sliced: true,
            selected: true
        }, {
            name: 'Edge',
            y: 14.77
        },  {
            name: 'Firefox',
            y: 4.86
        }, {
            name: 'Safari',
            y: 2.63
        }, {
            name: 'Internet Explorer',
            y: 1.53
        },  {
            name: 'Opera',
            y: 1.40
        }, {
            name: 'Sogou Explorer',
            y: 0.84
        }, {
            name: 'QQ',
            y: 0.51
        }, {
            name: 'Other',
            y: 2.6
        }]
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

    # #change copied data using data structure manipulation
    hc.options.title.text = 'Average Rating per day' 
    hc.options.subtitle.text = 'According to udemy data'
    #x
    #y
    
    hc.options.series[0].data =[{"name": v1, "y": v2} for v1,v2 in zip(share.index,share)]


    return wp

jp.justpy(app)       #it expects a function
