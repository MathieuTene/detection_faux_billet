import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import joblib
import numpy as np
import plotly.graph_objects as go

# 1. Chargement du modèle et du scaler
try:
    model = joblib.load('model.joblib')
    scaler = joblib.load('scaler.joblib')
    feature_columns = ['diagonal', 'height_left', 'height_right', 'margin_low', 'margin_up', 'length']
    
    # --- CALCUL DES BORNES DE COHÉRENCE (Basé sur le bon sens et les données) ---
    # On définit des limites larges mais réalistes (environ +/- 10% des moyennes)
    # Si une valeur sort de ces limites, le billet est considéré comme "Incohérent"
    valid_bounds = {
        'diagonal': (170.0, 174.0),
        'height_left': (102.0, 106.0),
        'height_right': (102.0, 106.0),
        'margin_low': (2.0, 8.0),
        'margin_up': (2.0, 5.0),
        'length': (108.0, 116.0)
    }
except Exception as e:
    print(f"Erreur lors du chargement : {e}")

# 2. Initialisation de l'application
FA = "https://use.fontawesome.com/releases/v5.15.4/css/all.css"
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, FA])
app.title = "Analyse de billets (Dollar)"
server = app.server

# --- COMPOSANTS UI ---
navbar = dbc.NavbarSimple(
    brand="Analyse de billets (Dollar)",
    brand_href="#",
    color="primary",
    dark=True,
    className="mb-4 shadow-sm"
)

footer = html.Footer(
    dbc.Container(
        dbc.Row([
            dbc.Col(html.P("© 2026 - Mathieu TENE | Data Scientist", className="text-center text-muted my-4"))
        ])
    ),
    className="mt-5 border-top"
)

def create_input_field(label, id, value, icon):
    return dbc.Col([
        html.Div([
            html.I(className=f"fas {icon} me-2 text-primary"),
            html.Label(label, className="font-weight-bold")
        ]),
        dbc.Input(id=id, type="number", value=value, step=0.01, className="mb-3 shadow-sm border-0 bg-light")
    ], md=6)

# --- LAYOUT ---
app.layout = html.Div([
    navbar,
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H4("Paramètres de Mesure", className="mb-0 text-white"), className="bg-primary"),
                    dbc.CardBody([
                        html.P("Saisissez les dimensions du billet en millimètres.", className="text-muted mb-4"),
                        dbc.Row([
                            create_input_field("Diagonale", "diagonal", 171.96, "fa-ruler-combined"),
                            create_input_field("Longueur", "length", 112.96, "fa-arrows-alt-h"),
                        ]),
                        dbc.Row([
                            create_input_field("Hauteur Gauche", "height_left", 104.04, "fa-arrows-alt-v"),
                            create_input_field("Hauteur Droite", "height_right", 103.92, "fa-arrows-alt-v"),
                        ]),
                        dbc.Row([
                            create_input_field("Marge Inf.", "margin_low", 4.31, "fa-border-style"),
                            create_input_field("Marge Sup.", "margin_up", 3.14, "fa-border-style"),
                        ]),
                        html.Hr(),
                        dbc.Button("Lancer l'Analyse", id="btn-predict", color="primary", size="lg", className="w-100 shadow mt-3")
                    ])
                ], className="shadow border-0 rounded")
            ], lg=7),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H4("Résultat du Diagnostic", className="mb-0"), className="bg-dark text-white text-center"),
                    dbc.CardBody([
                        html.Div(id="prediction-output", children=[
                            html.Div([html.P("En attente des données...", className="lead text-muted")], className="text-center py-5")
                        ]),
                        html.Div(id="gauge-container")
                    ], className="d-flex flex-column justify-content-center h-100")
                ], className="shadow border-0 rounded h-100")
            ], lg=5)
        ], className="g-4"),
    ], fluid=False),
    footer
], style={"backgroundColor": "#f8f9fa", "minHeight": "100vh"})

# --- CALLBACKS ---
@app.callback(
    [Output("prediction-output", "children"),
     Output("gauge-container", "children")],
    Input("btn-predict", "n_clicks"),
    [State("diagonal", "value"),
     State("height_left", "value"),
     State("height_right", "value"),
     State("margin_low", "value"),
     State("margin_up", "value"),
     State("length", "value")],
    prevent_initial_call=True
)
def predict_bill(n_clicks, diag, h_left, h_right, m_low, m_up, length):
    try:
        # 1. Vérification de cohérence (Safety Check)
        inputs = {'diagonal': diag, 'height_left': h_left, 'height_right': h_right, 
                  'margin_low': m_low, 'margin_up': m_up, 'length': length}
        
        errors = []
        for feat, val in inputs.items():
            low, high = valid_bounds[feat]
            if val < low or val > high:
                errors.append(feat)
        
        if errors:
            result_ui = html.Div([
                html.I(className="fas fa-exclamation-circle fa-4x text-warning mb-3"),
                html.H3("MESURES INCOHÉRENTES", className="text-warning font-weight-bold"),
                html.P(f"Les valeurs pour {', '.join(errors)} sont hors des limites physiques d'un billet de banque.", className="text-muted")
            ], className="text-center p-4")
            return result_ui, ""

        # 2. Si cohérent, on procède à la prédiction
        df_input = pd.DataFrame({k: [float(v)] for k, v in inputs.items()})[feature_columns]
        features_scaled = scaler.transform(df_input)
        
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0]
        
        if prediction: # VRAI
            res_text, res_color, prob_val = "BILLET AUTHENTIQUE", "success", probability[1] * 100
        else: # FAUX
            res_text, res_color, prob_val = "ALERTE : CONTREFAÇON", "danger", probability[0] * 100

        result_ui = html.Div([
            html.H2(res_text, className=f"text-{res_color} font-weight-bold mb-0"),
            html.P(f"Confiance du modèle : {prob_val:.2f}%", className="text-muted lead mt-2")
        ], className="text-center p-4")
        
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = prob_val,
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "#2c3e50" if prediction else "#e74c3c"},
                'steps': [{'range': [0, 50], 'color': '#f8d7da'}, {'range': [50, 85], 'color': '#fff3cd'}, {'range': [85, 100], 'color': '#d4edda'}]
            }
        ))
        fig.update_layout(height=250, margin=dict(l=20, r=20, t=50, b=20), paper_bgcolor='rgba(0,0,0,0)')
        return result_ui, dcc.Graph(figure=fig, config={'displayModeBar': False})

    except Exception as e:
        return html.Div(f"Erreur : {e}", className="text-danger"), ""

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8050)
