import json

new_toc = [
    "# DETECTION DE FAUX BILLETS\n",
    "## par Mathieu TENE\n",
    "\n",
    "--- \n",
    "## Table des matières\n",
    "\n",
    "1. [I. Exploration et Nettoyage](#section1)\n",
    "2. [II. Préparation des données](#section2)\n",
    "3. [III. Modélisation](#section3)\n",
    "4. [IV. Modèle Final et Préparation au Déploiement](#section4)\n",
    "\n",
    "---"
]

new_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["# IV. <a id='section4'></a>MODÈLE FINAL ET PRÉPARATION AU DÉPLOIEMENT"]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### IV.1 Choix du Random Forest\n",
            "\n",
            "Bien que la régression logistique offre d'excellentes performances, nous avons choisi d'implémenter un **Random Forest** pour le déploiement final. \n",
            "\n",
            "Ce choix se justifie par une meilleure robustesse face aux données aberrantes (extrapolation) et une stabilité accrue en conditions réelles."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import joblib\n",
            "from sklearn.ensemble import RandomForestClassifier\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "\n",
            "# Entraînement final\n",
            "features = ['diagonal', 'height_left', 'height_right', 'margin_low', 'margin_up', 'length']\n",
            "X_final = df[features]\n",
            "y_final = df['is_genuine']\n",
            "\n",
            "scaler_final = StandardScaler()\n",
            "X_scaled = scaler_final.fit_transform(X_final)\n",
            "\n",
            "model_final = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)\n",
            "model_final.fit(X_scaled, y_final)\n",
            "\n",
            "# Sauvegarde\n",
            "joblib.dump(model_final, 'model.joblib')\n",
            "joblib.dump(scaler_final, 'scaler.joblib')\n",
            "print('Modèle et Scaler sauvegardés pour le déploiement.')"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### IV.2 Application Dash\n",
            "\n",
            "L'étape finale a été le développement d'une application web interactive permettant de tester des billets en temps réel avec un système de contrôle de cohérence des données."
        ]
    }
]

file_path = 'Detection_faux_billets.ipynb'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Mise à jour de la TOC (cellule 0)
    if nb['cells']:
        nb['cells'][0]['source'] = new_toc

    # Ajout des nouvelles cellules à la fin
    nb['cells'].extend(new_cells)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print('OK')
except Exception as e:
    print(f'ERROR: {e}')
