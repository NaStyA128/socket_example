from flask import Flask, request, render_template

app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
@app.route('/<id>')
def index(id):
    # name = request.args.get('name')
    # return render_template('index.html', name=name)

    name = id
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run()
