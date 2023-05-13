import folium
from folium import Choropleth, Circle, Marker, Icon, Map, TileLayer
from folium.plugins import HeatMap, MarkerCluster
import geopandas as gpd
import json
import random
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import seaborn as sns
import statsmodels.api as s
import plotly.graph_objects as go




def lineplot (df, column_x, column_y, legend, title, label_x, label_y, label_legend):
    fig = fig.pxline(data_drame = df, 
                     x = column_x, 
                     y = column_y,
                     color = legend)
    fig.update_layout(
    width=900, # ancho de la figura en píxeles
    height=600, # alto de la figura en píxeles
    title={
        "text": title, # texto del título
        "font": {"size": 24} # tamaño de fuente del título
    },
    xaxis={
        "title": label_x, # etiqueta del eje X
        "title_font": {"size": 18}, # tamaño de fuente de la etiqueta del eje X
        "tickfont": {"size": 14} # tamaño de fuente de las marcas del eje X
    },
    yaxis={
        "title": label_y, # etiqueta del eje Y
        "title_font": {"size": 18}, # tamaño de fuente de la etiqueta del eje Y
        "tickfont": {"size": 14}},
    legend={
        "title": {"text": label_legend}, # texto del título de la leyenda
        "font": {"size": 14}})
    
    return fig 


def barplot (df, column_x, column_y, legend, title, animation): 

    """Esta funcion sirve para crear un barplot. Toma 6 argumentos: 
    - df: Data_frame
    - column_x: los datos de esta columna se situan en el eje x
    - column_y: los datos de esta columna se situan en el eje y
    - legend: los datos de esta columna se usan para asignar un color al gráfico
    - title: título del gráfico (string)
    - animation: """
    
    fig = px.bar(
        data_frame = df,
        x = column_x,
        y = column_y,
        color = legend,
        animation_frame = animation,
        barmode = 'group')
    
    fig.update_layout(
    width=1000, # ancho de la figura en píxeles
    height=600, # alto de la figura en píxeles
    title={
        "text": title, # texto del título
        "font": {"size": 24} # tamaño de fuente del título
    },
    xaxis={
        "title": label_x, # etiqueta del eje X
        "title_font": {"size": 18}, # tamaño de fuente de la etiqueta del eje X
        "tickfont": {"size": 14} # tamaño de fuente de las marcas del eje X
    },
    yaxis={
        "title": label_y, # etiqueta del eje Y
        "title_font": {"size": 18}, # tamaño de fuente de la etiqueta del eje Y
        "tickfont": {"size": 14}},
    legend={
        "title": {"text": label_legend}, # texto del título de la leyenda
        "font": {"size": 14}})
    
    return fig 


def plot_map(geo_json, df_, match_location, value_plotted,palette,animation, featureidkey, labels,valor_min, valor_max,title):
    fig = px.choropleth_mapbox(data_frame=df_,
        geojson=geo_json,
        locations=df_[match_location],
        featureidkey = featureidkey, #la key del json que hace match con la columna del df
        color=value_plotted,
        center={'lat':41.38879,  'lon':2.15899},
        mapbox_style='open-street-map', #tipo mapa
        zoom=10,
        color_continuous_scale=palette, #paleta de colores
        animation_frame=animation, #animación del eje x
        labels=labels, 
        width=850,  
        height=650)
    
    fig.update_layout(coloraxis=dict(cmin=valor_min, cmax=valor_max),
        width=900, # ancho de la figura en píxeles
        height=600, # alto de la figura en píxeles
        title={
        "text": title, # texto del título
        "font": {"size": 24} # tamaño de fuente del título
        })
    
    return fig


def hist_renta (df,column1, valor, columna_renta, title, eje_y,eje_x): 
    
    df = df[df[column1] == valor]
    
    sns.histplot(x=df[columna_renta], kde=True, color='seagreen', alpha = 0.5)
    plt.axvline(x=df[columna_renta].mean(), c="orange", label="mean")
    plt.axvline(x=df[columna_renta].median(), c="blue", label="median")
    plt.legend();
    plt.title(title)
    plt.ylabel(eje_y)
    plt.xlabel(eje_x)
    
    return plt


def scatter_plot (df_, columna_x, columna_y, legend, hover_name, title, label_x, label_y, label_legend): 
    
    fig = px.scatter(
    data_frame = df_, 
    x = columna_x,
    y = columna_y,
    color = legend,
    hover_name = hover_name,
    size="Import_€_Any")
    
    fig.update_layout(
    width=1000, # ancho de la figura en píxeles
    height=600, # alto de la figura en píxeles
    title={
        "text": title, # texto del título
        "font": {"size": 24} # tamaño de fuente del título
    },
    xaxis={
        "title": label_x, # etiqueta del eje X
        "title_font": {"size": 18}, # tamaño de fuente de la etiqueta del eje X
        "tickfont": {"size": 14} # tamaño de fuente de las marcas del eje X
    },
    yaxis={
        "title": label_y, # etiqueta del eje Y
        "title_font": {"size": 18}, # tamaño de fuente de la etiqueta del eje Y
        "tickfont": {"size": 14}},
    legend={
        "title": {"text": label_legend}, # texto del título de la leyenda
        "font": {"size": 14}})
    
    return fig


def swarmplot(df_, columna_x, columna_y, color, hover_name, title, columna_animacion, label_x, label_y,label_legend):
    
    fig = px.strip(
        data_frame= df_,
        x = columna_x,
        y = columna_y,
        color = color, 
        hover_name = hover_name, 
        animation_frame = columna_animacion)
    
    fig.update_layout(
    width=1000, # ancho de la figura en píxeles
    height=600, # alto de la figura en píxeles
    title={
        "text": title, # texto del título
        "font": {"size": 21} # tamaño de fuente del título
    },
    xaxis={
        "title": label_x, # etiqueta del eje X
        "title_font": {"size": 16}, # tamaño de fuente de la etiqueta del eje X
        "tickfont": {"size": 14} # tamaño de fuente de las marcas del eje X
    },
    yaxis={
        "title": label_y, # etiqueta del eje Y
        "title_font": {"size": 16}, # tamaño de fuente de la etiqueta del eje Y
        "tickfont": {"size": 14}},
    legend={
        "title": {"text": label_legend}, # texto del título de la leyenda
        "font": {"size": 13}})
    
    return fig


def diagrama_cajas (df, column_x, column_y, title, label_x, label_y ): 
    
    fig = px.box(
        data_frame = df,
        x = column_x,
        y = column_y)
    
    fig.update_layout(
    width=1000, # ancho de la figura en píxeles
    height=600, # alto de la figura en píxeles
    title={
        "text": title, # texto del título
        "font": {"size": 20} # tamaño de fuente del título
    },
    xaxis={
        "title": label_x, # etiqueta del eje X
        "title_font": {"size": 16}, # tamaño de fuente de la etiqueta del eje X
        "tickfont": {"size": 12} # tamaño de fuente de las marcas del eje X
    },
    yaxis={
        "title": label_y, # etiqueta del eje Y
        "title_font": {"size": 16}, # tamaño de fuente de la etiqueta del eje Y
        "tickfont": {"size": 12}})
    
    return fig 