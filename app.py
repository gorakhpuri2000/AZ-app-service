from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My Python Web Page</title>
        </head>
        <body style="font-family: Arial; background-color:#f4f4f4; text-align:center;">
            <h1>Welcome to My Python Web Page 🚀</h1>
            <p>This page is running using Flask</p>
            <p>Deployed on Azure App Service</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
