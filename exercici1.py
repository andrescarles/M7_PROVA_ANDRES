import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Andres Carles Pascual - Llistat.csv")
df = df.dropna()

def funcion1():
    notas = df.groupby(by='NAME').mean()
    return notas[['NOTES']]

def funcion2():
    funcion1().plot.bar(legend=False)
    plt.yticks(rotation='vertical')
    plt.title('Andres Carles')
    plt.xlabel('ALUMNAT')
    plt.ylabel('NOTES')
    plt.show()

