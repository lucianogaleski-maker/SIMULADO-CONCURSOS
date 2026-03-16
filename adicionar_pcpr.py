from app import app, db, Banca, Concurso, Materia, Questao
import random

with app.app_context():
    # Buscar ou criar banca
    banca = Banca.query.filter_by(nome='PUC-PR').first()
    if not banca:
        banca = Banca(nome='PUC-PR')
        db.session.add(banca)
        db.session.flush()
    
    # Criar concurso
    concurso = Concurso.query.filter_by(nome='Polícia Civil do Paraná 2024').first()
    if concurso:
        print('Concurso já existe!')
    else:
        concurso = Concurso(nome='Polícia Civil do Paraná 2024', 
                           orgao='Polícia Civil do Paraná', banca_id=banca.id)
        db.session.add(concurso)
        db.session.flush()
        
        # Matéria 1: Língua Portuguesa
        mat_port = Materia(nome='Língua Portuguesa', concurso_id=concurso.id)
        db.session.add(mat_port)
        db.session.flush()
        
        questoes_port = [
            {"e": "Assinale a alternativa que apresenta ERRO de concordância verbal.", "a": ["Fazem cinco anos que ele saiu.", "Deve haver soluções para o caso.", "Houve muitas denúncias.", "Existem provas suficientes.", "Faz meses que não o vejo."], "c": "Fazem cinco anos que ele saiu."},
            {"e": "Em qual alternativa a regência verbal está CORRETA?", "a": ["O delegado assistiu o depoimento.", "Prefiro investigar do que esperar.", "Aspiramos a uma polícia melhor.", "Esqueci do documento.", "Informei-lhe sobre o caso."], "c": "Aspiramos a uma polícia melhor."},
            {"e": "Assinale a alternativa com uso CORRETO da crase.", "a": ["Fui à delegacia ontem.", "Refiro-me à ela.", "Cheguei à uma conclusão.", "Vou à Brasília.", "Estou à espera desde às 8h."], "c": "Fui à delegacia ontem."},
            {"e": "Qual é a função sintática de 'ao suspeito' em 'O policial prendeu o suspeito'?", "a": ["Sujeito", "Objeto direto", "Objeto indireto", "Adjunto adverbial", "Complemento nominal"], "c": "Objeto direto"},
            {"e": "Identifique a alternativa com ERRO ortográfico.", "a": ["Exceção", "Assessor", "Excessão", "Obsessão", "Pretensão"], "c": "Excessão"},
            {"e": "Em 'Embora tivesse provas, não denunciou', a oração destacada é:", "a": ["Subordinada adverbial concessiva", "Subordinada adverbial causal", "Coordenada adversativa", "Subordinada substantiva", "Principal"], "c": "Subordinada adverbial concessiva"},
            {"e": "Qual é o plural correto de 'investigação criminal'?", "a": ["Investigação criminais", "Investigações criminal", "Investigações criminais", "Investigação criminals", "Investigações criminals"], "c": "Investigações criminais"},
            {"e": "Assinale a alternativa em que 'se' é partícula apassivadora.", "a": ["Ele se machucou na operação.", "Precisa-se de investigadores.", "Apuram-se os fatos.", "Ela se arrependeu.", "Eles se encontraram."], "c": "Apuram-se os fatos."},
            {"e": "Qual é o sinônimo de 'idôneo'?", "a": ["Corrupto", "Desonesto", "Íntegro", "Suspeito", "Duvidoso"], "c": "Íntegro"},
            {"e": "Em qual alternativa a colocação pronominal está INCORRETA?", "a": ["Nunca me contaram a verdade.", "Dir-lhe-ei tudo amanhã.", "Não o vi na delegacia.", "Me disseram que você viria.", "Sempre se dedicou ao trabalho."], "c": "Me disseram que você viria."},
            {"e": "Qual figura de linguagem está em 'Aquele policial é um leão'?", "a": ["Metáfora", "Metonímia", "Hipérbole", "Eufemismo", "Ironia"], "c": "Metáfora"},
            {"e": "Assinale a alternativa com todas as palavras acentuadas corretamente.", "a": ["Polícia, inquérito, réu", "Policia, inquerito, reu", "Polícia, inquerito, réu", "Policia, inquérito, reu", "Polícia, inquérito, reu"], "c": "Polícia, inquérito, réu"},
            {"e": "Qual é o antônimo de 'culpado'?", "a": ["Réu", "Suspeito", "Inocente", "Acusado", "Indiciado"], "c": "Inocente"},
            {"e": "Em 'É proibido entrada de pessoas não autorizadas', há erro de:", "a": ["Concordância nominal", "Concordância verbal", "Regência", "Crase", "Pontuação"], "c": "Concordância nominal"},
            {"e": "Qual alternativa apresenta um período composto por subordinação?", "a": ["Estudou muito e passou.", "Chegou cedo, mas saiu tarde.", "Quando terminar, me avise.", "Ele veio, ela foi.", "Trabalha ou estuda."], "c": "Quando terminar, me avise."}
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
        print('Polícia Civil do Paraná adicionada!')
