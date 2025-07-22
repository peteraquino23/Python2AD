#Graficos com Dash
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

#Dicionário com as informações da caixa Droqdown
dados_conceitos = {
    'java':{'Variaveis': 8, 'Condicionais': 12, 'Loops': 4, 'Poo': 15, 'Funcoes': 4},
    'python':{'Variaveis': 12, 'Condicionais': 8, 'Loops': 18, 'Poo': 17, 'Funcoes': 8},
    'sql':{'Variaveis': 10, 'Condicionais': 15, 'Loops': 7, 'Poo': 5, 'Funcoes': 16},
    'golang':{'Variaveis': 14, 'Condicionais': 19, 'Loops': 19, 'Poo': 12, 'Funcoes': 10},
    'javascript':{'Variaveis': 16, 'Condicionais': 17, 'Loops': 12, 'Poo': 20, 'Funcoes': 19},
}

#criar mapa de cores
cores_map = dict(
    java='#1F77B4',
    python='#FF7F0E',
    sql='#2CA02C',
    golang='#D62728',
    javascript='#9467bd'
)

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.H4('Cursos de TI', style={'textAlign': 'center'}),
    html.Div(
        dcc.Dropdown(
            id = 'dropdown_linguagens',
            options = [{'label': 'Java', 'value': 'java'},
                       {'label': 'Python', 'value': 'python'},
                       {'label': 'SQL', 'value': 'sql'},
                       {'label': 'Golang', 'value': 'golang'},
                       {'label': 'JavaScript', 'value': 'javascript'}
                       ],
            value=['python'],
            multi=True,
            style={'width': '50%', 'margin': '0 auto'}
            
        ),
    ),
    dcc.Graph(id='grafico_linguagem')
]), 

dcc.Graph(id='grafico_linguagem')
style={'width': '80%', 'margin': '0 auto'}



# Uma função que vai ser chamada atravez do evento
# Nesse caso ela vai ser chamada quando o dropdown mudar
@app.callback(
    Output('grafico_linguagem', 'figure'),
    Input('dropdown_linguagens', 'value')
)

def scater_linguaens(linguagens_selecionadas):
    scarter_trace = []
    for linguagem in linguagens_selecionadas:
        dados_linguagem = dados_conceitos[linguagem]
        for conceito, conhecimento in dados_linguagem.items():
            scarter_trace.append(
                go.Scatter(
                    x=[conceito],
                    y=[conhecimento],
                    mode='markers',
                    name=linguagem.title(),
                    marker={'size': 20, 'color': cores_map[linguagem]},
                      showlegend=False
                )
            )
    scarter_layout = go.Layout(
        title='Meus Conhecimentos de Linguagem',
        xaxis=dict(
            title='Conceitos',showgrid=False),
        yaxis=dict(
            title='Níveis de Conhecimento',showgrid=False)
    )
                
    return {'data': scarter_trace, 'layout': scarter_layout}
    
    

if __name__ == '__main__':
    app.run(debug=True)