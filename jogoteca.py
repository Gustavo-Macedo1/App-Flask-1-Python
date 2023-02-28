from flask import Flask, render_template, request, redirect, session, flash

class Jogos:
  def __init__(self, nome, categoria, plataforma):
    self.nome = nome
    self.categoria = categoria
    self.plataforma = plataforma

jogo1 = Jogos('Need for Speed', 'Racing', 'PS2')
jogo2 = Jogos('Elden Ring', 'RPG', 'PS5')
jogo3 = Jogos('Overcooked 2', 'Simulation', 'PC')
lista_jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'gustavomacedo'

@app.route('/')
def gerar_inicial():
  return render_template('lista.html', titulo='Jogos', jogos = lista_jogos)

@app.route('/novo')
def novo_jogo():
  return render_template('novo jogo.html', titulo='Criar novo jogo')

@app.route('/criar', methods=['POST',])
def criar_jogo():
  nome = request.form['nome']
  categoria = request.form['categoria']
  plataforma = request.form['plataforma']
  novo = Jogos(nome, categoria, plataforma)
  lista_jogos.append(novo)
  return redirect('/')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
  if request.form['senha'] == 'alohomora':
    session['usuario_logado'] = request.form['usuario']
    flash('Olá, ' + session['usuario_logado'] +'! Seja bem-vindo(a)!')
    return redirect('/')
  else:
    flash('Erro! Usuário ou senha incorreto(a).')
    return redirect('/login')

@app.route('/logout')
def logout():
  session['usuario_logado'] = None
  flash('Logout realizado com sucesso.')
  return redirect('/')

app.run(debug=True)