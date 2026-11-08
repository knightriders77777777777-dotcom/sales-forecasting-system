print("FLASK APP FILE IS RUNNING") 
from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

print("FLASK CREATED SUCCESSFULLY")

@app.route("/")


def home():
    print("HOME PAGE ROUTE FOUND")
    df = pd.read_csv("forecast_results.csv")
    table = df.to_html(index=False, border=0)

    html = """
    <html>
    <head>
        <title>Sales Forecasting Dashboard</title>
        <style>
            body {
                font-family: Arial;
                background: #e8f5e9;
                padding: 30px;
                text-align: center;
            }
            h1 {
                color: #1b5e20;
            }
            table {
                margin: auto;
                background: white;
                border-collapse: collapse;
            }
            th, td {
                padding: 12px;
                border: 1px solid #ccc;
            }
            img {
                width: 80%;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <h1>AI-Based Sales Forecasting System</h1>
        <h2>Next 30 Days Sales Prediction</h2>
        {{ table|safe }}
    </body>
    </html>
    """
    return render_template_string(html, table=table)

print("STARTING FLASK NOW")

if __name__ == "__main__":
    print("STARTING FLASK NOW")
    app.run(host="127.0.0.1", port=5000, debug=False)