#
# Conteudo do arquivo `myapp.py`
#
from flask import Flask, render_template, request, redirect, flash, url_for
#from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
#from wtforms import StringField, SubmitField, IntegerField
#from wtforms.validators import DataRequired, Length, ValidationError
import sqlite3

app = Flask(__name__)
app.debug = True
app.secret_key = 'djhfjdhfdkfheirweuryeuryei'

#Adicionando configurações para uso do banco de dados sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalogos_livros.db'

#Criando o SQLAlchemy instância
db = SQLAlchemy(app)

# Modelo
class Profile(db.Model):
    # Id: Campo que armazena Id exclusivo para cada linha da tabela no Banco de Dados.
    # Titulo: Usado para armazenar o Título do Livro na tabela catalogos_livros
    # Autor: Usado para armazenar o Autor do Livro na tabela catalogos_livros
    # Exemplares: Usado para armazenar a quantidade de Exemplares de Livros na tabela catalogos_livros
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), unique=False, nullable=False)
    autor = db.Column(db.String(255), unique=False, nullable=False)
    exemplares = db.Column(db.Integer, nullable=False)
  
    # repr method repersents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Título do Livro: {self.titulo}, Autor do Livro: {self.autor}, Exemplares: {self.exemplares}"
  
#Pagina inicial do aplicativo
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

#Pagina para acesso ao aplicativo
@app.route("/acesso")
def acesso():
    return render_template("acesso.html")

#Pagina para informações do aplicativo
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

#Classe para criação do formulário de cadastro de livros
#class CreateCadastroForm(FlaskForm):
    #titulo = StringField(label=('Titulo do Livro:'), validators=[DataRequired(), Length(max=255)])
    #autor = StringField(label=('Autor do Livro:'), validators=[DataRequired(), Length(max=255)])
    #exemplares = IntegerField(label=('Exemplares:'), validators=[DataRequired(), Length(max=4)])
    #submit = SubmitField(label=('Cadastrar'))
#    titulo = StringField(label=('Titulo do Livro:'))
#    autor = StringField(label=('Autor do Livro:'))
#    exemplares = IntegerField(label=('Exemplares:'))
#    submit = SubmitField(label=('Cadastrar'))


#Conexão com banco de dados
def conecta_db():
        conn = sqlite3.connect("catalogos_livros.db")
        conn.row_factory = sqlite3.Row
        return conn

#Pagina para cadastro de livros
@app.route("/cadastrar", methods=['GET','POST'])
def cadastrar():
    form = CreateCadastroForm()
    titulo = form.titulo.data
    autor  = form.autor.data
    exemplares = form.exemplares.data

    if request.method == 'POST': 
        if form.validate_on_submit():
            conn = conecta_db()
            posts = conn.execute('INSERT INTO catalogos_livros(Titulo,Autor,Exemplares) VALUES (?,?,?)',(titulo,autor,exemplares))
            conn.commit()
            return render_template("sucesso.html", posts=posts)
                #return render_template("sucesso.html", form=form)
        else:
            msg = 'Erro'
            return render_template("erro.html", forms=msg)
        conn.close()
    return render_template("cadastrar.html", form=form)

#Pagina para disponibilidade de livros no aplicativo
@app.route("/disponibilidade")
def disponibilidade():
    #page = request.args.get('page', 1, type=int)
    posts = Profile.query.all()
    #conn = conecta_db()
    #posts = conn.execute('SELECT Id,Titulo,Autor,Exemplares FROM catalogos_livros ORDER BY Titulo').paginate
    #pagenum = conn.fetchall()
    #conn.close()
    return render_template("disponibilidade.html", posts=posts)

#Pagina para pesquisar livros ou autores
@app.route("/pesquisar")
def pesquisar():
#    if titulo :
#        conn = conecta_db()
#        posts = conn.execute('SELECT Id,Titulo,Autor,Exemplares FROM catalogos_livros where Titulo ? ORDER BY Titulo', (titulo)).fetchall()
#        conn.close()
#        return render_template("pesquisar", posts=posts)
#    if autor :
#        conn = conecta_db()
#        posts = conn.execute('SELECT Id,Titulo,Autor,Exemplares FROM catalogos_livros where Autor ? ORDER BY Autor', (autor)).fetchall()
#        conn.close()
#        return render_template("pesquisar", posts=posts)

    return render_template("pesquisar.html")

if __name__ == "__main__":
#    from waitress import server
    app.run(host='0.0.0.0', port=8080)
