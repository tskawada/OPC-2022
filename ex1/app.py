from flask import Flask, render_template, request, send_from_directory
# servo.py
import RPi.GPIO as GPIO
import time
import argparse
import servo

app = Flask(__name__)
Angle = servo.Servo(0)

@app.route("/", methods=["GET", "POST"])
def stop():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("index.html")

@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "GET":
        return render_template("start.html")
    elif request.method == "POST":
        # angle = request.json["angleValue"]
        jsonData = request.json
        angle = jsonData["angleValue"]
        Angle.angle(angle)
        print(Angle.read_ang())
        return render_template("start.html")

if __name__ == "__main__":
    try:
        app.run(debug=True, port=8000)
        # app.run(debug=False, host="0.0.0.0", port=8000)
    except Exception as e:
        print(e)
        del Angle
