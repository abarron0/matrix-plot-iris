import pandas as pd
import plotly.express as px
from pathlib import Path

carpeta_datos = Path(r"C:\Users\Usuario\Downloads\Nueva carpeta")
archivo_datos = carpeta_datos / "iris.data"

columnas = [
    "longitud_sepalo",
    "anchura_sepalo",
    "longitud_petalo",
    "anchura_petalo",
    "especie"
]

df = pd.read_csv(archivo_datos, header=None, names=columnas).dropna()

df["especie"] = df["especie"].str.replace("Iris-", "", regex=False)
df["especie"] = df["especie"].replace({
    "setosa": "Setosa",
    "versicolor": "Versicolor",
    "virginica": "Virginica"
})

fig = px.scatter_matrix(
    df,
    dimensions=[
        "longitud_sepalo",
        "anchura_sepalo",
        "longitud_petalo",
        "anchura_petalo"
    ],
    color="especie",
    labels={
        "longitud_sepalo": "Longitud del sépalo",
        "anchura_sepalo": "Anchura del sépalo",
        "longitud_petalo": "Longitud del pétalo",
        "anchura_petalo": "Anchura del pétalo",
        "especie": "Especie"
    },
    width=1200,
    height=1200
)

fig.update_traces(
    diagonal_visible=False,
    marker=dict(size=6)
)

titulo = (
    "<b>¿Cómo se relacionan las medidas del sépalo y del pétalo<br>"
    "en las distintas especies de iris?</b>"
)

divisiones = [0.25, 0.50, 0.75]
shapes = []

for x in divisiones:
    shapes.append(
        dict(
            type="line",
            xref="paper",
            yref="paper",
            x0=x,
            x1=x,
            y0=0,
            y1=1,
            line=dict(color="gray", width=2)
        )
    )

for y in divisiones:
    shapes.append(
        dict(
            type="line",
            xref="paper",
            yref="paper",
            x0=0,
            x1=1,
            y0=y,
            y1=y,
            line=dict(color="gray", width=2)
        )
    )

fig.update_layout(
    title=dict(
        text=titulo,
        x=0.5,
        xanchor="center",
        y=0.98,
        yanchor="top",
        font=dict(size=32)
    ),
    plot_bgcolor="white",
    paper_bgcolor="white",
    legend_title_text="Especie",
    margin=dict(t=180, b=160, l=90, r=90),
    shapes=shapes,
    annotations=[
        dict(
            text='Fuente: <a href="https://archive.ics.uci.edu/dataset/53/iris" target="_blank">UCI Machine Learning Repository, Iris Data Set</a>',
            x=1,
            y=-0.14,
            xref="paper",
            yref="paper",
            showarrow=False,
            xanchor="right",
            yanchor="top",
            font=dict(size=13, color="gray")
        )
    ]
)

fig.update_xaxes(
    showgrid=True,
    gridcolor="#d9d9d9",
    zeroline=False
)

fig.update_yaxes(
    showgrid=True,
    gridcolor="#d9d9d9",
    zeroline=False
)

archivo_salida = carpeta_datos / "matrix_plot_iris.html"
fig.write_html(str(archivo_salida))
fig.show()
