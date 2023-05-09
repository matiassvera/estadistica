import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

datos = pd.read_csv('ds_salaries.csv', header=0)

#Grafico de barras del top 10 trabajos mas frecuentes del 2023
trabajos = datos[datos['work_year'] == 2023]['job_title'].value_counts()[:10]
grafico = px.bar(y=trabajos.values, x=trabajos.index,
                 text=trabajos.values, title='Los 10 trabajos mas frecuentes en Data Science en el año 2023')
grafico.update_layout(xaxis_title="Nombre de trabajo", yaxis_title="Cantidad", xaxis_title_font_size=25,
                      yaxis_title_font_size=25, title_font_size=40)
grafico.show()

# Histograma salario en USD
plt.figure(figsize=[12, 4])
sns.histplot(data=datos['salary_in_usd'], kde=True)
plt.title('Distribución de los salarios en USD')
plt.show()

#Definicion de la funcion para crear los histogramas por anio
def histogramaSalariosPorAnio(datos):
    fig, axs = plt.subplots(ncols=len(datos["work_year"].unique()), figsize=(15, 5))
    for i, anio in enumerate(sorted(datos["work_year"].unique())):
        df = datos[datos["work_year"] == anio]
        salarioPromedio = df["salary_in_usd"].mean()
        axs[i].hist(df["salary_in_usd"])
        axs[i].axvline(salarioPromedio, color='green', label=f"Salario promedio = ${salarioPromedio:,.0f}")
        axs[i].set_xlabel("Salario en USD")
        axs[i].set_ylabel("Frecuencia")
        axs[i].set_title(anio)
        axs[i].legend()
    fig.suptitle("Distribución de salarios en USD")
    plt.tight_layout()
    plt.show()

#Filtramos por trabajo los datos
datosDataAnalyst = datos[datos['job_title'] == 'Data Analyst']
datosDataEngineer = datos[datos['job_title']== 'Data Engineer']
datosDataScientist = datos[datos['job_title']== 'Data Scientist']
datosAppliedScientist = datos[datos['job_title'] == 'Applied Scientist']
datosResearchEngineer = datos[datos['job_title']== 'Research Engineer']
datosDataManager = datos[datos['job_title']== 'Data Manager']

#Realizamos cada uno de los histogramas
histogramaSalariosPorAnio(datosDataAnalyst)
histogramaSalariosPorAnio(datosDataEngineer)
histogramaSalariosPorAnio(datosDataScientist)
histogramaSalariosPorAnio(datosAppliedScientist)
histogramaSalariosPorAnio(datosResearchEngineer)
histogramaSalariosPorAnio(datosDataManager)

#Diagrama de caja de la distribucion de los salarios en USD
figura = px.box(y = datos['salary_in_usd'], title = 'Salario en USD')
figura.update_layout(title_font_size = 40)
figura.show()