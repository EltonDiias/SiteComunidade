from comunidadeimpressionadora import app
from comunidadeimpressionadora import database


@app.before_first_request
def create_tables():
    database.create_all()


if __name__ == '__main__':
    app.run(debug=True)
# apenas roda o meu site