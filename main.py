import uvicorn
import pandas as pd, numpy as np
from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

# cargar el dataset
movies_df = pd.read_csv('data_movies.csv')

@app.get('/')
def home():
    return {'message':"Bienvenido a la API de películas"}

'''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes
(nombre del mes, en str, ejemplo 'enero') historicamente'''


@app.get("/peliculas_mes/{mes}")
def peliculas_mes(mes):
    meses = {
        'enero': 'January',
        'febrero': 'February',
        'marzo': 'March',
        'abril': 'April',
        'mayo': 'May',
        'junio': 'June',
        'julio':'July',
        'agosto':'August',
        'septiembre': 'September',
        'octubre': 'Octuber',
        'noviembre': 'November',
        'diciembre': 'December'
    }
    
    df = pd.read_csv('data_movies.csv')
    df = df.dropna(subset=['release_date'])
    df['release_date'] = pd.to_datetime(df['release_date'])
    df_mes = df[df['release_date'].dt.month_name() == meses[mes].capitalize()]
    
    cantidad = len(df_mes)
    
    return {"mes": mes, "cantidad": cantidad}


'''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia 
(de la semana, en str, ejemplo 'lunes') historicamente'''

@app.get("/peliculas_dia/{dia}")
def peliculas_dia(dia):
    dias = {
    'lunes': 'Monday',
    'martes': 'Tuesday',
    'miércoles': 'Wednesday',
    'miercoles': 'Wednesday',
    'jueves': 'Thursday',
    'viernes': 'Friday',
    'sábado': 'Saturday',
    'sabado': 'Saturday',
    'domingo': 'Sunday'
    }
    
    df = pd.read_csv('data_movies.csv') #usar otro dataset solo las columnas a usar
    df_dia = df[df['release_date'].dt.day_name() == dias[dia].capitalize()]
    df = df.dropna(subset=['release_date'])
    df['release_date'] = pd.to_datetime(df['release_date'])

    respuesta = len(df_dia)
    
    return {'dia': dia, 'cantidad': respuesta}


'''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio''' 

@app.get("/franquicia/{franquicia}")
def franquicia(franquicia):
    peliculas = movies_df[movies_df["belongs_to_collection"].str.contains(franquicia, na=False)]
    cantidad = len(peliculas)
    ganancia_total = peliculas["revenue"].sum()
    ganancia_promedio = peliculas["revenue"].mean()
    return {"franquicia": franquicia, "cantidad": cantidad, "ganancia_total": ganancia_total, "ganancia_promedio": ganancia_promedio}


'''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''


@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais):
    peliculas = movies_df[movies_df["production_countries"].str.contains(pais, na=False)]
    cantidad = len(peliculas)
    return {"pais": pais, "cantidad": cantidad}


'''Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron'''


@app.get("/productoras/{productora}")
def productoras(productora):
    peliculas = movies_df[movies_df["production_companies"].str.contains(productora, na=False)]
    cantidad = len(peliculas)
    ganancia_total = peliculas["revenue"].sum()
    return {"productora": productora, "ganancia_total": ganancia_total, "cantidad": cantidad}


'''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'''


@app.get("/productoras/{productora}")
def productoras(productora):
    peliculas = movies_df[movies_df["production_companies"].str.contains(productora, na=False)]
    cantidad = len(peliculas)
    ganancia_total = peliculas["revenue"].sum()
    return {"productora": productora, "ganancia_total": ganancia_total, "cantidad": cantidad}
