import justpy as jp

def app():
    #create an object of QuaserPage class
    wp = jp.QuasarPage()       

    #fill webpage using jp.QDiv            
    h1 = jp.QDiv(a=wp, text='Analysis of Course Review', classes='text-h1 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text='These graphs represent course review analysis')

    return wp

jp.justpy(app)       #it expects a function
