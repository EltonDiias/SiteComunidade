from main import app
from comunidadeimpressionadora.models import Usuario
from comunidadeimpressionadora import database

# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username='Lira', email='lira@gmail.com', senha='1234124')
#     usuario2 = Usuario(username='Elton', email='elton@gmail.com', senha='elton1234')
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()


with app.app_context():
    usuarios = Usuario.query.all()
    print(usuarios[1].email)

# with app.app_context():
#     post = Post(id_usuario=2, titulo='Meu primeiro Post. Felicidades!!!',
#                 corpo="Muito feliz em aprender mais. Agradeço a todos a oportunidade.")
#     database.session.add(post)
#     database.session.commit()


# with app.app_context():
#     post_teste = Post.query.first()
#     print(post_teste.titulo)
#     print(post_teste.corpo)
#     print(post_teste.data_criacao)
#     print(post_teste.autor.email)


# Usuario.query.all()
# Usuario.query.first()

# with app.app_context():
#     database.drop_all()
#     database.create_all()