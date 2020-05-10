# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def hello():
#     return "Hello world!"
# if __name__ == "__main__":
#     app.run()


from flask import Flask, render_template, json
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


app.static_folder = 'static'
if __name__ == "__main__":
    app.run()