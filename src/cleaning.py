import pandas as pd 
import os 
import numpy as np
import pymysql
import sqlalchemy as alch # python -m pip install --upgrade 'sqlalchemy<2.0'
from getpass import getpass

def importar_csvs_de_carpeta(carpeta):
    """
    Importa varios archivos CSV de una carpeta y los combina en un único DataFrame.
    """
    dfs = []  # lista para almacenar los DataFrames cargados
    
    # iterar sobre los archivos en la carpeta y cargar cada uno en un DataFrame
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.csv'):
            path_archivo = os.path.join(carpeta, archivo) #Path completo a cada archivo en la carpeta.
            df = pd.read_csv(path_archivo)
            dfs.append(df)
    
    # combinar los DataFrames en uno solo y devolverlo
    return pd.concat(dfs, ignore_index=True)

def guardar_df_como_csv(df, path):
    """
    La función sirve para guardar un DataFrame de pandas como un archivo CSV en la ubicación especificada. Toma
    2 argumentos:     
    - df -- el DataFrame a guardar
    - path -- la ruta completa del archivo CSV
    """
    df.to_csv(path, index=False)


def reemplazar_nans(df, columna1, columna2):
    """Esta función sirve para reemplzara los valores nulos de una columna1 por los valores de otra columna2 y una vez
    reemplazados los valores dropee la columna2. 
    Toma tres argumentos: 
    - df: DataFrame
    - Columa1: la columna que contiene los nans
    - Columna2: la columna que contiene los valores que queremos reemplazar por los nans"""
    
    df[columna1] = df[columna1].fillna(df[columna2])
    df.drop(columns=columna2, inplace = True)
    
    return df

def drop_filas_not_in_lista(df, column, list_):
    
    """Esta función se utiliza para dropear aquellas filas que contengan un valor en una columna que no se encuentra
    en una lista. Toma tres argumentos: 
    - df: Dataframe 
    - Column: el nombre de la columna 
    - list_: lista de valores, en este caso codigos de barrios de barcelona"""
    
    df.drop(df[~df[column].isin(list_)].index, inplace=True) 
    
    return df 

def cambiar_valores_columna (df, columna1, diccionario):
    """Esta función sirve para reemplazar los valores de una columna usando un diccionario. Toma tres argumentos: 
    -df: DataFrame
    -columna1: columna que contiene los valores que deseas modificar 
    -diccionario: diccionario que en las keys contiene el valor antiguo (el que quieres cambiar) y los values son
    los valores nuevos"""
    
    # Reemplazar los valores de la columna utilizando el diccionario
    df[columna1] = df[columna1].map(diccionario)
    
    # Devolver el DataFrame con la columna modificada
    return df

def rename_column (df, column1, nuevo_nombre): 

    """Esta función sirve para renombrar una columna pasando un diccionario
    donde la key es el nombre de la columna que se desea cambiar y el value
    el nuevo nombre que se quiere poner"""
    
    df = df.rename(columns = {column1: nuevo_nombre})
    
    return df

def crear_dataframe(diccionario):
    # Convertir el diccionario en un DataFrame
    df = pd.DataFrame.from_dict(diccionario)
    
    # Devolver el DataFrame
    return df

def borrar_columnas(df, list_columns):
    
    """Esta función se usa para borrar columnas de un dataframe y toma como argumentos: 
    - df: DataFrame pandas
    - list_columns: lista de los nombres de las columnas que quieres borrar"""
    
    df.drop(columns=list_columns, inplace = True)
    
    return df

def eliminar_filas (df, columna, lista_valores):
    
    """Esta función sirve para eliminar del dataframe las filas que contengan unos valores concretos en una columna. 
    La función toma tres argumentos:
    - df: Dataframe
    - columna: nombre de la columna que contiene los valores que queremos eliminar
    - lista_valores: lista de valores que no queremos tener"""
    
    # Seleccionar las filas que no contienen los valores a eliminar en la columna especificada
    filas_a_mantener = df.loc[~df[columna].isin(lista_valores)]
    
    # Crear un nuevo DataFrame con las filas seleccionadas
    df_filtrado = pd.DataFrame(filas_a_mantener)
    
    return df_filtrado


def drop_na_rows (df): 
    
    # Eliminar todas las filas que contienen valores NaN en cualquier columna
    df_filtrado = df.dropna(inplace=True)
    return df_filtrado


def cambiar_tipo_dato (df,column1, column2, tipo):

    """Esta función sirve para cambiar el tipo de los valores de dos 
    columnas y tomas 4 argumentos: 
    - df: Data Frame
    - column1: Nombre de la columna 1
    - column2: Nombre de la columna 2
    - tipo: tipo de valor que se desea (int,float,str,...)"""
    
    df[column1] = df[column1].astype(tipo)
    df[column2] = df[column2].astype(tipo)
    
    return df 


def cambiar_formato_columna(df, columna, valor_cambio):

    # Utilizar la función apply() de Pandas para aplicar una función lambda a cada valor de la columna
    df[columna] = df[columna].apply(lambda x: str(x)[:4])
    df[columna] = df[columna].astype(valor_cambio)
    
    return df


def filtros_df (df, column1, valor_column1):
    
    """Esta función sirve para aplicar un filtro al dataframe. La función toma 
    tres argumentos: 
    - df: DataFrame de precios de alquiler
    - column1: cualquier columna
    - valor_column1: valor que queremos de la columna1
    """
    df1 = df.copy()
    
    condition1 = df1[column1] <= valor_column1

    df1 = df1[condition1]
    
    return df1


def agrupar_count (df,column1, column2):
    """Funcion para agrupar un df y renombrar una columna"""

    df1 = df.copy()
    
    df1= df.groupby(column1)[column2].count().reset_index()

    df1 = df1.rename (columns={'created':'cantidad_equipamientos'})
    
    return df1


def crear_columna_km2 (df, column1, column2):

    """Funcion para crear un columna nueva en un df donde se aplica 
    una lambda. Toma tres argumentos: 
    - df: Data Frame 
    - column1: columna nueva 
    - column2: columna que contiene los valores que se le aplican a la lambda"""
    
    df[column1] = df[column2].apply(lambda x: x*0.01)
                                    
    return df 


def load_df_to_sql(df, table_name, dbName):
    """
    Carga un DataFrame en una tabla de una base de datos MySQL.
    
    Args:
        df (pandas.DataFrame): El DataFrame a cargar en la tabla.
        table_name (str): El nombre de la tabla en la que cargar los datos.
        dbName (str): El nombre de la base de datos en la que se encuentra la tabla.
    
    Returns:
       None
    """
    # Conectarse a la base de datos
    password = getpass("Please enter your password: ")
    connectionData = f"mysql+pymysql://root:{password}@localhost/{dbName}"
    engine = alch.create_engine(connectionData)
    
    # Cargar el DataFrame en la tabla
    df.to_sql(name=table_name, con = engine, if_exists="replace", index = True)
