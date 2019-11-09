import plotly.graph_objects as plotly_ding
import numpy as np


# Deze method kan voor de Xas en Yas een integer waarde ontvangen voor het tekenen 
# van een rechtlijn. Je kunt ook een np.arange mee gegeven. Of zelfs een vergelijking

def TekenEenLijn(Xas, Yas): 
    if (isinstance(Xas, int)):
        x = []
        teller = 1 
        while teller < len(Yas): 
            x.append(Xas)
            teller +=1
    elif (isinstance(Xas, str)): 
        x = eval(Xas)
    else: 
        x = Xas
    if (isinstance(Yas, int)):
        y = []
        teller = 1
        while teller < len(x):
            y.append(Yas)
            teller += 1
    elif (isinstance(Yas, str)):
        y = eval(Yas)
    else:
        y = Yas
    figure = plotly_ding.Figure(data=plotly_ding.Scatter(x=x, y=y, mode="lines"))
    figure.write_html('first_figure.html', auto_open=True)

TekenEenLijn('y*2+1', np.arange(-10,10))