# Project--III
## Descripción
Este proyecto es un análisis descriptivo de la evolución del nivel educativo en la ciudad de Barcelona considerando los niveles de educación, la renta y el sexo de la población, así como su distribución entre los barrios y distritos de la ciudad. 

Las hipótesis planteadas son:
  - La evolución del nivel de estudios en la ciudad de Barcelona ha sido positiva del 2009 al 2019 forma global, por sexos, y barrios.
- Los distritos con rentas más elevadas tienen un porcentaje de población mayor con estudios superiores
- La brecha entre los barrios más pobres y los barrios más ricos ha aumentado


## Workflow

**Data aquisition:** Para llevar a cabo este estudio, los datos han sido extraídos de Barcelona Open Data y la web del Departamento de Estadística y Difusión de Datos de la ciudad de Barcelona. Los data sets utilizados son:
- [Padrón de habitantes. Población de la ciudad de Barcelona según sexo y nivel académico](https://opendata-ajuntament.barcelona.cat/data/ca/dataset/est-padro-nivell-academic-sexe) 
- [Renta disponible de los hogares de la ciudad de Barcelona por cápita y barrio](https://opendata-ajuntament.barcelona.cat/data/ca/dataset/renda-disponible-llars-bcn)
- [Renta disponible de los hogares de la ciudad de Barcelona por cápita y distrito](https://ajuntament.barcelona.cat/estadistica/catala/Estadistiques_per_temes/Economia/Renda_i_tributs/Renda_disponible_llars/Anual/T011.htm)

**Data management:** Los datos han sido transformados y limpiados con la librería pandas. Una vez limpios se han importado los diferentes dataframes a una base de datos de SQL des de Python usando las librerías pymysql, sqlalchemy y getpass. En SQL se han modificado los tipos de datos de las tablas y asignado Primary and Foreign Keys para relacionarlas entre ellas. 

**Data analysis:** Para realizar el análisis, se han importado a Python los dataframes transformados usando Querys de SQL con las librerías pymysql, sqlalchemy y getpass. A partir de estos dataframes, se han realizado visualizaciones para representar los datos, extraer patrones y probar las hipótesis. Las librerías utilizadas para las visualizaciones son plotly, folium y seaborn. 

**Conclusiones:** Extraer unas conclusiones en base al resultado de las visualizaciones. 

## Organización
El repositorio consiste de un README file, a .gitignore file, project_final.ipynb y las siguientes carpetas: 
-	Data/: que incluy dos subcarpetas con los csv originales y los csv transformados después del data cleaning. 
-	src/: contiene los archivos .py para diferentes ejecutables: cleaning.py para la limpieza y transformación de los datasets y visualization.py para mostrar los gráficos. 

## Conclusiones
- La evolución del nivel educativo de la población de Barcelona es positivo
- El número de mujeres con estudios superiores es mayor que el número de hombres, mientras que el número de mujeres sin estudios mínimos obligatorios también es mayor. 
- La distribución de niveles educativos por barrios varía. La renta y el nivel educativo tienen una correlación positiva cuando mayor es la renta por cápita, el porcentaje de población con estudios superiores es más elevado. En cambio, la correlación es negativa si miramos al porcentaje de población sin estudios mínimos obligatorios.
- No puedo determinar que la brecha haya aumentado, tendría que mirar el coeficiente Gini. 




