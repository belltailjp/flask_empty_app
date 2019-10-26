import flask
app = flask.Flask(__name__)


@app.route('/')
def root():
    return flask.abort(403)


if __name__ == '__main__':
    app.run(debug=True)
