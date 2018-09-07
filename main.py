import os
from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template("index.html", page="home")

# TO RUN THIS
# python main.py
# -> Running on http://localhost:33507/

if __name__ == "__main__":
    from os import environ
    port = int(os.environ.get("PORT", 33507))
    app.run(debug=False, host='0.0.0.0', port=port)
