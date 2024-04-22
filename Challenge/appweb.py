from flask import Flask, render_template
import pandas as pd
import plotly
import plotly.express as px
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    # List to store the data from all JSON files
    todos_os_dados = []

    # Get the list of JSON files in the directory
    arquivos_json = [arq for arq in os.listdir("graficos") if arq.endswith(".json")]

    # Loop through each JSON file
    for arquivo in arquivos_json:
        with open(os.path.join("graficos", arquivo), "r") as f:
            dados = json.load(f)
            todos_os_dados.append(dados)

    # Convert data to Pandas DataFrame
    df = pd.DataFrame(todos_os_dados)  # Use todos_os_dados instead of dados

    # Create the plot (example of a bar chart)
    fig = px.bar(df, x="categoria", y="valor")

    # Convert the plot to JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # Render the template with the plot
    return render_template("index.html", graphJSON=graphJSON)

if __name__ == "__main__":
    app.run(debug=True)