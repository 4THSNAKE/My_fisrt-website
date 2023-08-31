from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("app.html")

# @app.route('/')
# def nav():
#     return render_template("nav.html")

# @app.route("/")
# def index():
#     return "hello world"
# @app.route("/whereami")
# def whereami():
#     return "Ghana"

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("404.html")

# @app.route('/foo/<name>')
# def foo(name):
#     return render_template("fool.html",to=name)
if __name__ == "__main__":
    app.run(debug=True)
