import json
import random
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = 'simulado_secret_key_2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simulado.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ── MODELS ────────────────────────────────────────────────────────────────────
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

class Banca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

class Concurso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    orgao = db.Column(db.String(150))
    banca_id = db.Column(db.Integer, db.ForeignKey('banca.id'))
    banca = db.relationship('Banca', backref='concursos')

class Materia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    concurso_id = db.Column(db.Integer, db.ForeignKey('concurso.id'))
    concurso = db.relationship('Concurso', backref='materias')

class Questao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.Text, nullable=False)
    alternativa_a = db.Column(db.Text, nullable=False)
    alternativa_b = db.Column(db.Text, nullable=False)
    alternativa_c = db.Column(db.Text, nullable=False)
    alternativa_d = db.Column(db.Text, nullable=False)
    alternativa_e = db.Column(db.Text, nullable=False)
    resposta_correta = db.Column(db.String(1), nullable=False)
    materia_id = db.Column(db.Integer, db.ForeignKey('materia.id'))
    materia = db.relationship('Materia', backref='questoes')

class Desempenho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    concurso_id = db.Column(db.Integer, db.ForeignKey('concurso.id'))
    nota_total = db.Column(db.Float)
    total_questoes = db.Column(db.Integer)
    acertos = db.Column(db.Integer)
    tempo_gasto = db.Column(db.Integer)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    usuario = db.relationship('Usuario', backref='desempenhos')
    concurso = db.relationship('Concurso', backref='desempenhos')

class DesempenhoMateria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desempenho_id = db.Column(db.Integer, db.ForeignKey('desempenho.id'))
    materia_id = db.Column(db.Integer, db.ForeignKey('materia.id'))
    acertos = db.Column(db.Integer)
    total = db.Column(db.Integer)
    desempenho = db.relationship('Desempenho', backref='por_materia')
    materia = db.relationship('Materia')

# ── HELPERS ───────────────────────────────────────────────────────────────────
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def nivel_aptidao(nota):
    if nota < 50:
        return ('danger', 'Necessita reforçar a base teórica.')
    elif nota <= 75:
        return ('warning', 'Bom desempenho, foque nos erros específicos.')
    return ('success', 'Excelente! Você está no nível de competitividade para a vaga.')

# ── AUTH ──────────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        u = Usuario.query.filter_by(email=request.form['email']).first()
        if u and check_password_hash(u.senha, request.form['senha']):
            session['usuario_id'] = u.id
            session['usuario_nome'] = u.nome
            return redirect(url_for('dashboard'))
        erro = 'E-mail ou senha inválidos.'
    return render_template('login.html', erro=erro)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    erro = None
    if request.method == 'POST':
        if Usuario.query.filter_by(email=request.form['email']).first():
            erro = 'E-mail já cadastrado.'
        else:
            db.session.add(Usuario(nome=request.form['nome'], email=request.form['email'],
                                   senha=generate_password_hash(request.form['senha'])))
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('cadastro.html', erro=erro)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ── ROTAS ─────────────────────────────────────────────────────────────────────
@app.route('/dashboard')
@login_required
def dashboard():
    concursos = Concurso.query.all()
    historico = Desempenho.query.filter_by(usuario_id=session['usuario_id'])\
        .order_by(Desempenho.data.desc()).limit(5).all()
    return render_template('dashboard.html', concursos=concursos, historico=historico)

@app.route('/simulado/<int:concurso_id>')
@login_required
def simulado(concurso_id):
    concurso = Concurso.query.get_or_404(concurso_id)
    questoes_simulado = []
    for materia in Materia.query.filter_by(concurso_id=concurso_id).all():
        qs = Questao.query.filter_by(materia_id=materia.id).all()
        for q in random.sample(qs, min(15, len(qs))):
            questoes_simulado.append({
                'id': q.id, 'enunciado': q.enunciado, 'materia': materia.nome,
                'materia_id': materia.id,
                'alternativas': {'A': q.alternativa_a, 'B': q.alternativa_b,
                                 'C': q.alternativa_c, 'D': q.alternativa_d, 'E': q.alternativa_e}
            })
    random.shuffle(questoes_simulado)
    session['questoes_simulado'] = questoes_simulado
    session['concurso_id'] = concurso_id
    return render_template('simulado.html', concurso=concurso,
                           questoes=questoes_simulado, total=len(questoes_simulado))

@app.route('/finalizar', methods=['POST'])
@login_required
def finalizar():
    data = request.get_json()
    respostas, tempo = data.get('respostas', {}), data.get('tempo', 0)
    questoes = session.get('questoes_simulado', [])
    acertos_total, por_materia = 0, {}

    for q in questoes:
        qid, mat, mat_id = str(q['id']), q['materia'], q['materia_id']
        if mat not in por_materia:
            por_materia[mat] = {'materia_id': mat_id, 'acertos': 0, 'total': 0}
        por_materia[mat]['total'] += 1
        qdb = Questao.query.get(q['id'])
        if qdb and respostas.get(qid) == qdb.resposta_correta:
            acertos_total += 1
            por_materia[mat]['acertos'] += 1

    total = len(questoes)
    nota = round((acertos_total / total) * 100, 1) if total else 0
    nivel_cls, nivel_msg = nivel_aptidao(nota)

    desemp = Desempenho(usuario_id=session['usuario_id'], concurso_id=session.get('concurso_id'),
                        nota_total=nota, total_questoes=total, acertos=acertos_total, tempo_gasto=tempo)
    db.session.add(desemp)
    db.session.flush()
    for mat_nome, info in por_materia.items():
        db.session.add(DesempenhoMateria(desempenho_id=desemp.id, materia_id=info['materia_id'],
                                         acertos=info['acertos'], total=info['total']))
    db.session.commit()
    return jsonify({'nota': nota, 'acertos': acertos_total, 'total': total,
                    'nivel_cls': nivel_cls, 'nivel_msg': nivel_msg,
                    'por_materia': por_materia, 'tempo': tempo})

@app.route('/historico')
@login_required
def historico():
    registros = Desempenho.query.filter_by(usuario_id=session['usuario_id'])\
        .order_by(Desempenho.data.desc()).all()
    return render_template('historico.html', registros=registros)

# ── POPULAR BANCO ─────────────────────────────────────────────────────────────
def popular_banco():
    with open('data/questoes.json', encoding='utf-8') as f:
        dados = json.load(f)
    for banca_data in dados['bancas']:
        banca = Banca(nome=banca_data['nome'])
        db.session.add(banca)
        db.session.flush()
        for cd in banca_data['concursos']:
            concurso = Concurso(nome=cd['nome'], orgao=cd['orgao'], banca_id=banca.id)
            db.session.add(concurso)
            db.session.flush()
            for md in cd['materias']:
                materia = Materia(nome=md['nome'], concurso_id=concurso.id)
                db.session.add(materia)
                db.session.flush()
                for q in md['questoes']:
                    letras = ['A', 'B', 'C', 'D', 'E']
                    alts = q['alternativas'][:]
                    correta_texto = q['correta']
                    correta_idx = alts.index(correta_texto)
                    random.shuffle(letras)
                    mapa = {letras[i]: alts[i] for i in range(5)}
                    resposta_correta = letras[correta_idx]
                    db.session.add(Questao(
                        enunciado=q['enunciado'],
                        alternativa_a=mapa['A'], alternativa_b=mapa['B'],
                        alternativa_c=mapa['C'], alternativa_d=mapa['D'],
                        alternativa_e=mapa['E'], resposta_correta=resposta_correta,
                        materia_id=materia.id
                    ))
    db.session.commit()
    print("Banco de dados populado com sucesso!")

# Inicializar banco ao iniciar
with app.app_context():
    db.create_all()
    if Banca.query.count() == 0:
        try:
            popular_banco()
        except:
            pass

if __name__ == '__main__':
    app.run(debug=True)
