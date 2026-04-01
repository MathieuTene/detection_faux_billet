import json

# Contenu des nouvelles cellules à ajouter
new_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# IV. <a id='deploiement'></a>MODÈLE FINAL ET PRÉPARATION AU DÉPLOIEMENT"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### IV.1 Choix du Random Forest\n",
            "\n",
            "Bien que la régression logistique offre d'excellentes performances sur le dataset d'entraînement, nous avons choisi d'implémenter un **Random Forest** pour le déploiement final. \n",
            "\n",
            "Ce choix se justifie par une meilleure robustesse face aux données aberrantes (extrapolation) lors des tests utilisateurs, garantissant ainsi un outil plus fiable en conditions réelles."
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
            "# Préparation des colonnes de caractéristiques\n",
            "features = ['diagonal', 'height_left', 'height_right', 'margin_low', 'margin_up', 'length']\n",
            "X = df[features]\n",
            "y = df['is_genuine']\n",
            "\n",
            "# Entraînement final sur l'ensemble des données\n",
            "final_scaler = StandardScaler()\n",
            "X_scaled = final_scaler.fit_transform(X)\n",
            "\n",
            "final_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)\n",
            "final_model.fit(X_scaled, y)\n",
            "\n",
            "# Sauvegarde des fichiers pour l'application Dash\n",
            "joblib.dump(final_model, 'model.joblib')\n",
            "joblib.dump(final_scaler, 'scaler.joblib')\n",
            "\n",
            "print(\"Modèle final (Random Forest) et Scaler sauvegardés avec succès.\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### IV.2 Déploiement : Application Dash\n",
            "\n",
            "L'étape finale a consisté à développer une application interactive avec **Dash (Plotly)** et **Bootstrap**. \n",
            "\n",
            "**Fonctionnalités clés :**\n",
            "*   Interface de saisie intuitive pour les mesures du billet.\n",
            "*   Système de vérification de la **cohérence des données** pour bloquer les saisies physiquement impossibles.\n",
            "*   Diagnostic instantané avec jauge de confiance visuelle.\n",
            "*   Architecture prête pour un déploiement cloud (DigitalOcean, Heroku)."
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# CONCLUSION\n",
            "\n",
            "Ce projet a permis de couvrir l'intégralité de la chaîne de valeur d'un projet Data Science : de la préparation des données et l'analyse statistique jusqu'à la mise à disposition d'un produit fini via une interface web sécurisée et performante."
        ]
    }
]

# Table des matières mise à jour
toc_source = [
    "# DETECTION DE FAUX BILLETS\n",
    "## par Mathieu TENE\n",
    "\n",
    "--- \n",
    "## Table des matières\n",
    "\n",
    "1. [I. Exploration et Nettoyage](#section1)\n",
    "   * [I.1 Vérifications et corrections](#section1-1)\n",
    "   * [I.2 Exploration des données](#section1-2)\n",
    "   * [I.3 Visualisation](#section1-3)\n",
    "2. [II. Préparation des données](#section2)\n",
    "   * [Gestion des valeurs manquantes](#section2-1)\n",
    "   * [Standardisation et Split](#section2-2)\n",
    "3. [III. Modélisation](#section3)\n",
    "   * [Comparaison des algorithmes](#section3-1)\n",
    "   * [Analyse des performances](#section3-2)\n",
    "4. [IV. Modèle Final et Préparation au Déploiement](#section4)\n",
    "   * [Choix du Random Forest](#section4-1)\n",
    "   * [Sauvegarde du modèle et du scaler](#section4-2)\n",
    "   * [Présentation de l'application Dash](#section4-3)\n",
    "\n",
    "---"
]

try:
    # On repart du fichier corrompu pour essayer de sauver ce qu'on peut ou on attend la restauration
    # Mais le plus simple est de ré-appliquer les changements sur une base saine.
    # Je vais générer un script qui attend que le fichier soit "propre" avant d'agir.
    print("Script de réparation prêt.")
except Exception as e:
    print(e)
