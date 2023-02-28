from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogos:
  def __init__(self, nome, categoria, plataforma):
    self.nome = nome
    self.categoria = categoria
    self.plataforma = plataforma

jogo1 = Jogos('Need for Speed', 'Racing', 'PS2')
jogo2 = Jogos('Elden Ring', 'RPG', 'PS5')
jogo3 = Jogos('Overcooked 2', 'Simulation', 'PC')
lista_jogos = [jogo1, jogo2, jogo3]

class Usuario:
  def __init__(self, nome, nick, senha):
    self.nome = nome
    self.nick = nick
    self.senha = senha

user1 = Usuario('Gustavo Macedo', 'programador', 'github12')
user2 = Usuario('Guilherme Briggs', 'guizinho', 'dublador')
user3 = Usuario('Rihanna', 'cantomuito', 'sourica123')

users = { user1.nick : user1,
          user2.nick : user2,
          user3.nick : user3 }

app = Flask(__name__)
app.secret_key = 'gustavomacedo'

@app.route('/')
def gerar_inicial():
  return render_template('lista.html', titulo='Jogos', jogos = lista_jogos)

@app.route('/novo')
def novo_jogo():
  if 'usuario_logado' not in session or session['usuario_logado'] == None:
    return redirect(url_for('login', proximo=url_for('novo_jogo')))
  else:
    return render_template('novo jogo.html', titulo='Criar novo jogo')

@app.route('/criar', methods=['POST',])
def criar_jogo():
  nome = request.form['nome']
  categoria = request.form['categoria']
  plataforma = request.form['plataforma']
  novo = Jogos(nome, categoria, plataforma)
  lista_jogos.append(novo)
  return redirect(url_for('gerar_inicial'))

@app.route('/login')
def login():
  proxima = request.args.get('proximo')
  return render_template('login.html', prox = proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
  if request.form['usuario'] in users:
    usuario = users[request.form['usuario']]
    if request.form['senha'] == usuario.senha:
      session['usuario_logado'] = usuario.nick
      flash('Olá, ' + usuario.nick +'! Seja bem-vindo(a)!')
      proxima = request.form['proxima']
      return redirect(proxima)

  flash('Erro! Usuário ou senha incorreto(a).')
  return redirect(url_for('login'))

@app.route('/logout')
def logout():
  session['usuario_logado'] = None
  flash('Logout realizado com sucesso.')
  return redirect(url_for('gerar_inicial'))

app.run(debug=True)