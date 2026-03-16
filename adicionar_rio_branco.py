from app import app, db, Banca, Concurso, Materia, Questao
import random

with app.app_context():
    # Buscar ou criar banca
    banca = Banca.query.filter_by(nome='FAUEL').first()
    if not banca:
        banca = Banca(nome='FAUEL')
        db.session.add(banca)
        db.session.flush()
    
    # Criar concurso
    concurso = Concurso.query.filter_by(nome='Prefeitura Rio Branco do Sul - PR').first()
    if concurso:
        print('Concurso já existe!')
    else:
        concurso = Concurso(nome='Prefeitura Rio Branco do Sul - PR', 
                           orgao='Prefeitura Municipal', banca_id=banca.id)
        db.session.add(concurso)
        db.session.flush()
        
        # Matéria 1: Língua Portuguesa
        mat_port = Materia(nome='Língua Portuguesa', concurso_id=concurso.id)
        db.session.add(mat_port)
        db.session.flush()
        
        questoes_port = [
            {"e": "Assinale a alternativa em que o uso do acento indicativo de crase está CORRETO.", "a": ["Vou à pé até a prefeitura.", "Refiro-me à aquela funcionária.", "Compareça à reunião às 14h.", "Fui à Brasília ontem.", "Cheguei à uma conclusão."], "c": "Compareça à reunião às 14h."},
            {"e": "Qual alternativa apresenta ERRO de concordância verbal?", "a": ["Fazem dois meses que não o vejo.", "Houve muitos problemas na reunião.", "Deve haver soluções para isso.", "Faz anos que trabalho aqui.", "Existem várias opções."], "c": "Fazem dois meses que não o vejo."},
            {"e": "Em qual frase a colocação pronominal está INCORRETA?", "a": ["Nunca me contaram a verdade.", "Contar-lhe-ei tudo depois.", "Não te vi na reunião.", "Me empresta o documento?", "Sempre se esforçou muito."], "c": "Me empresta o documento?"},
            {"e": "Assinale a alternativa que apresenta um vício de linguagem (pleonasmo vicioso).", "a": ["Subir para cima", "Entrar para dentro", "Sair para fora", "Descer para baixo", "Todas as anteriores"], "c": "Todas as anteriores"},
            {"e": "Qual é a função sintática do termo destacado: 'Entreguei o documento AO DIRETOR'.", "a": ["Sujeito", "Objeto direto", "Objeto indireto", "Adjunto adverbial", "Predicativo"], "c": "Objeto indireto"},
            {"e": "Identifique a alternativa com ERRO ortográfico.", "a": ["Exceção", "Assessor", "Pretensão", "Excessão", "Obsessão"], "c": "Excessão"},
            {"e": "Em 'Quando você chegar, me avise', a oração destacada é:", "a": ["Subordinada adverbial temporal", "Subordinada substantiva", "Coordenada sindética", "Subordinada adjetiva", "Principal"], "c": "Subordinada adverbial temporal"},
            {"e": "Qual é o plural correto de 'cidadão'?", "a": ["Cidadões", "Cidadães", "Cidadãos", "Cidadans", "Cidadãoes"], "c": "Cidadãos"},
            {"e": "Assinale a alternativa em que 'se' é pronome apassivador.", "a": ["Ele se machucou.", "Precisa-se de funcionários.", "Vendem-se casas.", "Ela se arrependeu.", "Eles se encontraram."], "c": "Vendem-se casas."},
            {"e": "Qual é o sinônimo de 'idôneo'?", "a": ["Desonesto", "Corrupto", "Íntegro", "Falso", "Suspeito"], "c": "Íntegro"},
            {"e": "Em qual alternativa há um erro de regência verbal?", "a": ["Assisti ao filme ontem.", "Prefiro café a chá.", "Esqueci do compromisso.", "Obedeça às normas.", "Paguei ao fornecedor."], "c": "Esqueci do compromisso."},
            {"e": "Qual figura de linguagem está presente em 'Aquele funcionário é um leão'?", "a": ["Metáfora", "Metonímia", "Hipérbole", "Eufemismo", "Ironia"], "c": "Metáfora"},
            {"e": "Assinale a alternativa em que todas as palavras estão acentuadas corretamente.", "a": ["Saúde, baú, país", "Saude, bau, pais", "Saúde, bau, país", "Saude, baú, pais", "Saúde, baú, pais"], "c": "Saúde, baú, país"},
            {"e": "Qual é o antônimo de 'prolixo'?", "a": ["Extenso", "Detalhado", "Verboso", "Conciso", "Longo"], "c": "Conciso"},
            {"e": "Em 'É proibido entrada de pessoas não autorizadas', há erro de:", "a": ["Concordância nominal", "Concordância verbal", "Regência", "Crase", "Pontuação"], "c": "Concordância nominal"}
        ]
        
        for q in questoes_port:
            letras = ['A','B','C','D','E']
            alts = q['a'][:]
            idx = alts.index(q['c'])
            random.shuffle(letras)
            mapa = {letras[i]: alts[i] for i in range(5)}
            resp = letras[idx]
            db.session.add(Questao(enunciado=q['e'], alternativa_a=mapa['A'], alternativa_b=mapa['B'],
                alternativa_c=mapa['C'], alternativa_d=mapa['D'], alternativa_e=mapa['E'],
                resposta_correta=resp, materia_id=mat_port.id))
        
        db.session.commit()
        print('Prefeitura Rio Branco do Sul adicionada!')
