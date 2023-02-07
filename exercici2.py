import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Andres Carles Pascual - Llistat.csv")
df = df.dropna()

def funcion1():
    grupo = df.groupby(by='GROUP').mean()
    faltas = grupo[grupo['GROUP'] == 'DAW2'].groupby(by='MODULE').mean()
    return faltas[['NAME'],['ABSENCES']]

def funcion2():
   pass

print(funcion1())