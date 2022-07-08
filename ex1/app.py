from flask import Flask, render_template, request, send_from_directory
# import RPi.GPIO as GPIO

app = Flask(__name__)

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def top():
    return render_template("index.html")

if __name__ == "__main__":
    try:
        app.run(debug=True, port=8000)
        # app.run(debug=False, host="0.0.0.0", port=8000)
    except Exception as e:
        print(e)
