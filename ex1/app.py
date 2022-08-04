from flask import Flask, render_template, request, send_from_directory
# servo.py
import RPi.GPIO as GPIO
import time
import servo
import relay

app = Flask(__name__)
Angle = servo.Servo()
Motor = relay.Relay()

@app.route("/", methods=["GET", "POST"])
def stop():
    # GETメソッド
    if request.method == "GET":
        # ********* KADAI *********
        
        # *************************
        return render_template("stop.html")
    # POSTメソッド
    elif request.method == "POST":
        # ********* KADAI *********

        # *************************
        return render_template("stop.html")

@app.route("/start", methods=["GET", "POST"])
def start():
    # GETメソッド
    if request.method == "GET":
        # ********* KADAI *********

        # *************************
        return render_template("start.html")
    # POSTメソッド
    elif request.method == "POST":
        # ブラウザからスライダーの値を受け取り，angleに格納
        jsonData = request.json
        angle = int(jsonData["angleValue"])
        # ********* KADAI *********

        # *************************
        return render_template("start.html")
        
if __name__ == "__main__":
    Motor.stop()
    try:
        app.run(debug=False, host="0.0.0.0", port=8000)
    except Exception as e:
        print(e)
        del Angle
        del Motor