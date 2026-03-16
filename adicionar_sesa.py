from app import app, db, Banca, Concurso, Materia, Questao
import random

with app.app_context():
    # Criar banca COPS-UEL
    banca = Banca.query.filter_by(nome='COPS-UEL').first()
    if not banca:
        banca = Banca(nome='COPS-UEL')
        db.session.add(banca)
        db.session.flush()
    
    # Criar concurso SESA-PR
    concurso = Concurso.query.filter_by(nome='SESA-PR 2024').first()
    if concurso:
        print('SESA-PR já existe!')
    else:
        concurso = Concurso(nome='SESA-PR 2024', orgao='Secretaria de Saúde do Paraná', banca_id=banca.id)
        db.session.add(concurso)
        db.session.flush()
        
        # Matéria 1: Português
        mat_port = Materia(nome='Português', concurso_id=concurso.id)
        db.session.add(mat_port)
        db.session.flush()
        
        questoes_port = [
            {"e": "Assinale a alternativa que apresenta correta aplicação das regras de concordância nominal.", "a": ["Os documentos médicos anexos foram enviados.", "Seguem anexo as prescrições.", "É necessário a atenção do paciente.", "Bastante pessoas compareceram.", "Meio confusa, a enfermeira saiu."], "c": "Seguem anexo as prescrições."},
            {"e": "Identifique a alternativa em que a colocação pronominal está INCORRETA.", "a": ["Nunca me disseram a verdade.", "Dir-lhe-ei tudo amanhã.", "Não o vi ontem.", "Me falaram sobre o caso.", "Sempre se dedicou ao trabalho."], "c": "Me falaram sobre o caso."},
            {"e": "Qual das frases abaixo apresenta erro de regência verbal?", "a": ["O médico assistiu o paciente.", "Prefiro trabalhar a descansar.", "Aspiramos a uma vida melhor.", "Esqueci-me do compromisso.", "Informei-lhe sobre o resultado."], "c": "Informei-lhe sobre o resultado."},
            {"e": "Em qual alternativa o uso da vírgula está CORRETO?", "a": ["O paciente, que chegou cedo foi atendido.", "Maria, a enfermeira mais experiente, coordena a equipe.", "Ele disse, que viria hoje.", "Os médicos, e enfermeiros trabalham juntos.", "Comprei, remédios e curativos."], "c": "Maria, a enfermeira mais experiente, coordena a equipe."},
            {"e": "Assinale a alternativa que contém um erro ortográfico.", "a": ["Exceção", "Assessoria", "Paralisar", "Pretensioso", "Obsessão"], "c": "Paralisar"},
            {"e": "Qual é o sinônimo de 'idôneo'?", "a": ["Desonesto", "Íntegro", "Corrupto", "Falso", "Duvidoso"], "c": "Íntegro"},
            {"e": "Em 'Embora estivesse cansado, continuou trabalhando', a oração destacada é:", "a": ["Causal", "Concessiva", "Consecutiva", "Condicional", "Final"], "c": "Concessiva"},
            {"e": "Qual alternativa apresenta um período composto por coordenação?", "a": ["Quando chegou, todos saíram.", "Estudou muito, mas não passou.", "É importante que você venha.", "O médico que atende aqui é experiente.", "Espero que melhore logo."], "c": "Estudou muito, mas não passou."},
            {"e": "Assinale a alternativa em que 'que' é pronome relativo.", "a": ["Que dia lindo!", "Espero que você venha.", "O livro que li é ótimo.", "Que horas são?", "É melhor que fique."], "c": "O livro que li é ótimo."},
            {"e": "Qual é o antônimo de 'ínfimo'?", "a": ["Pequeno", "Mínimo", "Máximo", "Reduzido", "Inferior"], "c": "Máximo"},
            {"e": "Em 'Faz dez anos que trabalho aqui', o verbo 'fazer' é:", "a": ["Pessoal", "Impessoal", "Transitivo direto", "Transitivo indireto", "De ligação"], "c": "Impessoal"},
            {"e": "Assinale a frase com uso CORRETO da crase.", "a": ["Vou à Curitiba amanhã.", "Refiro-me à ela.", "Cheguei à uma hora.", "Fui à farmácia.", "Estou à espera desde às 8h."], "c": "Fui à farmácia."},
            {"e": "Qual é a função sintática de 'ao paciente' em 'O médico explicou o diagnóstico ao paciente'?", "a": ["Sujeito", "Objeto direto", "Objeto indireto", "Adjunto adverbial", "Complemento nominal"], "c": "Objeto indireto"},
            {"e": "Identifique a figura de linguagem em 'A sala estava um forno'.", "a": ["Metáfora", "Metonímia", "Hipérbole", "Eufemismo", "Ironia"], "c": "Metáfora"},
            {"e": "Assinale a alternativa em que todas as palavras estão grafadas corretamente.", "a": ["Privilégio, beneficente, meteorologia", "Previlégio, beneficiente, metereologia", "Privilégio, beneficiente, meteorologia", "Previlégio, beneficente, metereologia", "Privilégio, beneficente, metereologia"], "c": "Privilégio, beneficente, meteorologia"}
        ]
        
        for q in questoes_port:
            letras = ['A','B','C','D','E']
            alts = q['a'][:]
            idx_correta = alts.index(q['c'])
            random.shuffle(letras)
            mapa = {letras[i]: alts[i] for i in range(5)}
            resp = letras[idx_correta]
            db.session.add(Questao(enunciado=q['e'], alternativa_a=mapa['A'], alternativa_b=mapa['B'],
                alternativa_c=mapa['C'], alternativa_d=mapa['D'], alternativa_e=mapa['E'],
                resposta_correta=resp, materia_id=mat_port.id))
        
        db.session.commit()
        print('SESA-PR adicionada com sucesso!')
