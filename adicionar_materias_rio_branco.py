from app import app, db, Concurso, Materia, Questao
import random

with app.app_context():
    concurso = Concurso.query.filter_by(nome='Prefeitura Rio Branco do Sul - PR').first()
    
    # Matéria: Matemática
    mat_mat = Materia(nome='Matemática', concurso_id=concurso.id)
    db.session.add(mat_mat)
    db.session.flush()
    
    questoes_mat = [
        {"e": "Um produto custa R$ 250,00 e recebe um desconto de 20%. Qual o valor final?", "a": ["R$ 200,00", "R$ 210,00", "R$ 220,00", "R$ 230,00", "R$ 225,00"], "c": "R$ 200,00"},
        {"e": "Se 3 funcionários fazem um trabalho em 6 dias, quantos dias levarão 6 funcionários?", "a": ["2 dias", "3 dias", "4 dias", "9 dias", "12 dias"], "c": "3 dias"},
        {"e": "Qual é 30% de 800?", "a": ["200", "240", "260", "280", "300"], "c": "240"},
        {"e": "A soma dos ângulos internos de um quadrilátero é:", "a": ["180°", "270°", "360°", "450°", "540°"], "c": "360°"},
        {"e": "Se x + 15 = 42, então x é igual a:", "a": ["25", "26", "27", "28", "29"], "c": "27"},
        {"e": "Qual é a área de um retângulo de 8m por 5m?", "a": ["13 m²", "26 m²", "40 m²", "45 m²", "50 m²"], "c": "40 m²"},
        {"e": "A raiz quadrada de 169 é:", "a": ["11", "12", "13", "14", "15"], "c": "13"},
        {"e": "Um carro percorre 300 km com 25 litros. Quantos km percorre com 40 litros?", "a": ["400 km", "420 km", "450 km", "480 km", "500 km"], "c": "480 km"},
        {"e": "Qual é o resultado de 2³ × 2²?", "a": ["16", "24", "32", "64", "128"], "c": "32"},
        {"e": "Se um produto custava R$ 100,00 e passou a custar R$ 120,00, o aumento foi de:", "a": ["10%", "15%", "20%", "25%", "30%"], "c": "20%"},
        {"e": "O perímetro de um quadrado de lado 7 cm é:", "a": ["14 cm", "21 cm", "28 cm", "35 cm", "49 cm"], "c": "28 cm"},
        {"e": "Qual é o MMC de 6 e 8?", "a": ["12", "16", "24", "32", "48"], "c": "24"},
        {"e": "Se 5 canetas custam R$ 15,00, quanto custam 8 canetas?", "a": ["R$ 20,00", "R$ 22,00", "R$ 24,00", "R$ 26,00", "R$ 28,00"], "c": "R$ 24,00"},
        {"e": "Qual é o valor de 15% de R$ 200,00?", "a": ["R$ 20,00", "R$ 25,00", "R$ 30,00", "R$ 35,00", "R$ 40,00"], "c": "R$ 30,00"},
        {"e": "Um terreno retangular tem 20m de frente e 30m de fundo. Sua área é:", "a": ["50 m²", "100 m²", "400 m²", "600 m²", "900 m²"], "c": "600 m²"}
    ]
    
    for q in questoes_mat:
        letras = ['A','B','C','D','E']
        alts = q['a'][:]
        idx = alts.index(q['c'])
        random.shuffle(letras)
        mapa = {letras[i]: alts[i] for i in range(5)}
        resp = letras[idx]
        db.session.add(Questao(enunciado=q['e'], alternativa_a=mapa['A'], alternativa_b=mapa['B'],
            alternativa_c=mapa['C'], alternativa_d=mapa['D'], alternativa_e=mapa['E'],
            resposta_correta=resp, materia_id=mat_mat.id))
    
    # Matéria: Conhecimentos Gerais
    mat_cg = Materia(nome='Conhecimentos Gerais', concurso_id=concurso.id)
    db.session.add(mat_cg)
    db.session.flush()
    
    questoes_cg = [
        {"e": "Rio Branco do Sul está localizado em qual região do Paraná?", "a": ["Norte", "Sul", "Leste", "Oeste", "Região Metropolitana de Curitiba"], "c": "Região Metropolitana de Curitiba"},
        {"e": "Qual é a principal atividade econômica histórica de Rio Branco do Sul?", "a": ["Agricultura", "Mineração de calcário", "Turismo", "Indústria têxtil", "Pesca"], "c": "Mineração de calcário"},
        {"e": "O município de Rio Branco do Sul foi emancipado em:", "a": ["1870", "1890", "1912", "1947", "1960"], "c": "1912"},
        {"e": "Qual rio banha o município de Rio Branco do Sul?", "a": ["Rio Iguaçu", "Rio Ribeira", "Rio Açungui", "Rio Paraná", "Rio Tibagi"], "c": "Rio Ribeira"},
        {"e": "A população estimada de Rio Branco do Sul é de aproximadamente:", "a": ["10 mil", "20 mil", "32 mil", "50 mil", "70 mil"], "c": "32 mil"},
        {"e": "Qual é a distância aproximada entre Rio Branco do Sul e Curitiba?", "a": ["20 km", "40 km", "60 km", "80 km", "100 km"], "c": "40 km"},
        {"e": "O clima de Rio Branco do Sul é classificado como:", "a": ["Tropical", "Equatorial", "Subtropical", "Semiárido", "Temperado"], "c": "Subtropical"},
        {"e": "Qual é o gentílico de quem nasce em Rio Branco do Sul?", "a": ["Rio-branquense", "Riobranquense", "Rio-branquino", "Branquense", "Sulista"], "c": "Rio-branquense"},
        {"e": "A festa tradicional mais importante do município é:", "a": ["Festa do Peão", "Festa da Uva", "Festa do Calcário", "Oktoberfest", "Carnaval"], "c": "Festa do Calcário"},
        {"e": "Rio Branco do Sul faz divisa com qual município?", "a": ["Curitiba", "Ponta Grossa", "Almirante Tamandaré", "Paranaguá", "Londrina"], "c": "Almirante Tamandaré"},
        {"e": "O bioma predominante na região é:", "a": ["Cerrado", "Amazônia", "Mata Atlântica", "Caatinga", "Pampa"], "c": "Mata Atlântica"},
        {"e": "Qual é o principal produto agrícola do município?", "a": ["Café", "Soja", "Milho", "Trigo", "Arroz"], "c": "Milho"},
        {"e": "A altitude média de Rio Branco do Sul é de aproximadamente:", "a": ["500 m", "700 m", "900 m", "1100 m", "1300 m"], "c": "900 m"},
        {"e": "O município possui quantos distritos?", "a": ["1", "2", "3", "4", "5"], "c": "3"},
        {"e": "Qual rodovia principal passa por Rio Branco do Sul?", "a": ["BR-116", "BR-277", "PR-092", "BR-376", "PR-151"], "c": "PR-092"}
    ]
    
    for q in questoes_cg:
        letras = ['A','B','C','D','E']
        alts = q['a'][:]
        idx = alts.index(q['c'])
        random.shuffle(letras)
        mapa = {letras[i]: alts[i] for i in range(5)}
        resp = letras[idx]
        db.session.add(Questao(enunciado=q['e'], alternativa_a=mapa['A'], alternativa_b=mapa['B'],
            alternativa_c=mapa['C'], alternativa_d=mapa['D'], alternativa_e=mapa['E'],
            resposta_correta=resp, materia_id=mat_cg.id))
    
    db.session.commit()
    print('Matérias adicionadas para Rio Branco do Sul!')
