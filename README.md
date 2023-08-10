# Bienvenidos a mi proyecto para la carrera Data Scientist
![](https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png)

En esta ocación, la empresa Henry nos contrata como científicos de datos para realizar consultas a travez de una API y un sistema de  recomendacion de películas.
Nuestro trabajo fue realizar el trabajo de ETL y EDA para lograr dichos resultados, con el siguiente [Datasets](https://drive.google.com/file/d/1Rp7SNuoRnmdoQMa5LWXuK4i7W1ILblYb/view)

####  A CONTINUACION, DETALLAREMOS LOS ARCHIVOS LOGRADOS POR EL DEPARTAMENTO:

## Archivos :
- [EDA_ML.ipynb](https://github.com/Davidarr96/Proyecto1_MLoperations/blob/main/EDA_ML.ipynb) -> notebook con el análisis exploratorio de los datos.
- [Modelo_Recomendaciòn.ipynb](https://github.com/Davidarr96/Proyecto1_MLoperations/blob/main/Modelo_Recomendaciòn.ipynb) -> notebook con el sistema de recomendación de películas.
- [Proyecto1_MLoperations.ipynb](https://github.com/Davidarr96/Proyecto1_MLoperations/blob/main/Proyecto1_MLoperations.ipynb) -> notebook con el paso a paso  del ETL.
- [README.md](https://github.com/Davidarr96/Proyecto1_MLoperations/blob/main/README.md) -> instrucciones y documentación del proyecto.
- [data_movies.csv](https://github.com/Davidarr96/Proyecto1_MLoperations/blob/main/data_movies.csv) ->csv con el datasets que utilizaremos para la API.
- [main.py](https://github.com/Davidarr96/Proyecto1_MLoperations/blob/main/main.py) -> archivo de codigo para la API.
- [requirements.txt](https://github.com/Davidarr96/Proyecto1_MLoperations/blob/main/requirements.txt) -> archivo txt con lo requirementos para el deployado de nuestra api.

## FUNCIONALIDADES DE LA API:

🎉 Mensaje de bienvenida : [Hola](https://ejemplo-nombre-deploy-nhor.onrender.com)

✔️ Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes (nombre del mes, en str, ejemplo 'enero') historicamente.

🚀 [LINK](https://ejemplo-nombre-deploy-nhor.onrender.com/docs#/default/peliculas_mes_peliculas_mes__mes__get)

✔️ Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia (de la semana, en str, ejemplo 'lunes') historicamente.

🚀 [LINK](https://ejemplo-nombre-deploy-nhor.onrender.com/docs#/default/peliculas_dia_peliculas_dia__dia__get)

✔️ Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio.
 
 🚀 [LINK](https://ejemplo-nombre-deploy-nhor.onrender.com/docs#/default/franquicia_franquicia__franquicia__get)
 
 ✔️ Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo.
 
  🚀 [LINK](https://ejemplo-nombre-deploy-nhor.onrender.com/docs#/default/peliculas_pais_peliculas_pais__pais__get)
  
  ✔️ Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron.
  
   🚀 [LINK](https://ejemplo-nombre-deploy-nhor.onrender.com/docs#/default/productoras_productoras__productora__get)
  
  #### ADVERTENCIA 

⚠️Los meses admitidos son [enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre]

⚠️ Los días admitidos son [lunes, martes, miercoles, jueves, viernes, sábado, domingo]

✨ MUCHAS GRACIAS ✨

Agradezco el tiempo que te has tomado para testear mi api y darme un feedback 💪

