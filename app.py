from flask import Flask, render_template
# from views import views

app = Flask(__name__)

# app.register_blueprint(views, url_prefix="/views")
# #app.register_blueprint(views, url_prefix="/home")


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
