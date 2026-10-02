from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """<!doctype html>
<html>
<head>
    <title>Dockerized Web App</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial;
            text-align: center;
            background: #f4f7fb;
            padding: 70px 20px;
        }

        .card {
            max-width: 650px;
            margin: auto;
            background: white;
            padding: 40px;
            border-radius: 14px;
            box-shadow: 0 8px 25px #0001;
        }

        .badge {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 20px;
            background: #eef2ff;
        }
    </style>
</head>

<body>
    <div class="card">
        <h1>Dockerized Web Application</h1>
        <p>A beginner-friendly Flask application running inside Docker.</p>
        <p class="badge">Flask + Python + Docker</p>
        <p>Container is running successfully </p>
    </div>
</body>
</html>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
