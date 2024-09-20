import datetime
from flask import Flask, render_template,request

app = Flask(__name__)

entries = []

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formated_date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entry_content, formated_date))
    return render_template("home.html",entries=entries)