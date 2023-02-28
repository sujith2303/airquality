from flask import Flask, render_template, request, jsonify
import os
import numpy as np
from keras.models import load_model
from  train import pre


webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir,template_folder=template_dir)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        try:
            if request.form:
                dict_req = dict(request.form)
                print(dict_req)
                array = list(map(int,dict_req.values()))
                print(array)
                response = pre(array)
                if response>0 and response<0.5:
                    response='verybad'
                elif response>0.5 and response<1:
                    response = 'average'
                else:
                    response = 'cool'

                return render_template("index.html", response=response)

        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!! Try again later!"}
            error = {"error": e}

            return render_template("404.html", error=error)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)