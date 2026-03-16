from app import app, db, Concurso, Materia, Questao
import random

with app.app_context():
    concurso = Concurso.query.filter_by(nome='Polícia Civil do Paraná 2024').first()
    
    # Matéria: Direito Penal
    mat_penal = Materia(nome='Direito Penal', concurso_id=concurso.id)
    db.session.add(mat_penal)
    db.session.flush()
    
    questoes_penal = [
        {"e": "Segundo o Código Penal, o crime é consumado quando:", "a": ["Há apenas a intenção", "Reúnem-se todos os elementos de sua definição legal", "Há tentativa", "Há desistência voluntária", "Há arrependimento"], "c": "Reúnem-se todos os elementos de sua definição legal"},
        {"e": "A legítima defesa é uma causa de:", "a": ["Agravante", "Qualificadora", "Excludente de ilicitude", "Atenuante", "Aumento de pena"], "c": "Excludente de ilicitude"},
        {"e": "O crime de homicídio está previsto no artigo:", "a": ["121 do CP", "129 do CP", "155 do CP", "157 do CP", "171 do CP"], "c": "121 do CP"},
        {"e": "A pena de reclusão deve ser cumprida em regime:", "a": ["Apenas aberto", "Apenas fechado", "Fechado, semiaberto ou aberto", "Apenas semiaberto", "Domiciliar"], "c": "Fechado, semiaberto ou aberto"},
        {"e": "O furto qualificado tem pena:", "a": ["Menor que o furto simples", "Igual ao furto simples", "Aumentada", "Reduzida", "Extinta"], "c": "Aumentada"},
        {"e": "A prescrição da pretensão punitiva ocorre:", "a": ["Antes do trânsito em julgado", "Após o cumprimento da pena", "Durante a execução", "Nunca ocorre", "Apenas em crimes culposos"], "c": "Antes do trânsito em julgado"},
        {"e": "O crime de roubo está previsto no artigo:", "a": ["155 do CP", "157 do CP", "171 do CP", "129 do CP", "121 do CP"], "c": "157 do CP"},
        {"e": "A tentativa é punível quando:", "a": ["O crime se consuma", "Iniciada a execução, não se consuma por circunstâncias alheias à vontade do agente", "Há desistência voluntária", "Há arrependimento eficaz", "O crime é impossível"], "c": "Iniciada a execução, não se consuma por circunstâncias alheias à vontade do agente"},
        {"e": "O dolo é caracterizado pela:", "a": ["Negligência", "Imprudência", "Imperícia", "Vontade consciente de realizar o crime", "Culpa"], "c": "Vontade consciente de realizar o crime"},
        {"e": "A reincidência é considerada:", "a": ["Atenuante", "Excludente", "Agravante", "Causa de diminuição", "Irrelevante"], "c": "Agravante"},
        {"e": "O crime de estelionato está previsto no artigo:", "a": ["155 do CP", "157 do CP", "171 do CP", "129 do CP", "121 do CP"], "c": "171 do CP"},
        {"e": "A menoridade penal no Brasil é até:", "a": ["16 anos", "17 anos", "18 anos", "21 anos", "14 anos"], "c": "18 anos"},
        {"e": "O estado de necessidade é:", "a": ["Agravante", "Qualificadora", "Excludente de ilicitude", "Atenuante", "Crime"], "c": "Excludente de ilicitude"},
        {"e": "A pena de detenção deve ser cumprida em regime:", "a": ["Apenas fechado", "Semiaberto ou aberto", "Apenas aberto", "Fechado, semiaberto ou aberto", "Domiciliar"], "c": "Semiaberto ou aberto"},
        {"e": "O crime de lesão corporal está previsto no artigo:", "a": ["121 do CP", "129 do CP", "155 do CP", "157 do CP", "171 do CP"], "c": "129 do CP"}
    ]
    
    for q in questoes_penal:
        letras = ['A','B','C','D','E']
        alts = q['a'][:]
        idx = alts.index(q['c'])
        random.shuffle(letras)
        mapa = {letras[i]: alts[i] for i in range(5)}
        resp = letras[idx]
        db.session.add(Questao(enunciado=q['e'], alternativa_a=mapa['A'], alternativa_b=mapa['B'],
            alternativa_c=mapa['C'], alternativa_d=mapa['D'], alternativa_e=mapa['E'],
            resposta_correta=resp, materia_id=mat_penal.id))
    
    # Matéria: Direito Processual Penal
    mat_cpp = Materia(nome='Direito Processual Penal', concurso_id=concurso.id)
    db.session.add(mat_cpp)
    db.session.flush()
    
    questoes_cpp = [
        {"e": "O inquérito policial é:", "a": ["Contraditório", "Dispensável", "Procedimento administrativo investigatório", "Obrigatório sempre", "Judicial"], "c": "Procedimento administrativo investigatório"},
        {"e": "A prisão em flagrante pode ser realizada por:", "a": ["Apenas policiais", "Apenas delegados", "Qualquer pessoa do povo", "Apenas juízes", "Apenas promotores"], "c": "Qualquer pessoa do povo"},
        {"e": "O prazo para conclusão do inquérito policial (réu preso) é de:", "a": ["5 dias", "10 dias", "15 dias", "30 dias", "60 dias"], "c": "10 dias"},
        {"e": "A denúncia é oferecida pelo:", "a": ["Delegado", "Juiz", "Ministério Público", "Advogado", "Vítima"], "c": "Ministério Público"},
        {"e": "O habeas corpus é cabível quando:", "a": ["Há ameaça ou violação à liberdade de locomoção", "Há dano ao patrimônio", "Há ofensa à honra", "Há lesão corporal", "Sempre"], "c": "Há ameaça ou violação à liberdade de locomoção"},
        {"e": "A prisão preventiva pode ser decretada:", "a": ["Pelo delegado", "Pelo promotor", "Pelo juiz", "Por qualquer policial", "Pela vítima"], "c": "Pelo juiz"},
        {"e": "O prazo para oferecimento da denúncia (réu preso) é de:", "a": ["3 dias", "5 dias", "10 dias", "15 dias", "30 dias"], "c": "5 dias"},
        {"e": "A ação penal pública é promovida pelo:", "a": ["Delegado", "Juiz", "Ministério Público", "Advogado", "Vítima"], "c": "Ministério Público"},
        {"e": "O recurso cabível contra sentença condenatória é:", "a": ["Habeas corpus", "Mandado de segurança", "Apelação", "Agravo", "Embargos"], "c": "Apelação"},
        {"e": "A prisão temporária tem prazo máximo de:", "a": ["5 dias", "10 dias", "30 dias", "60 dias", "90 dias"], "c": "30 dias"},
        {"e": "O interrogatório do réu é:", "a": ["Obrigatório", "Facultativo", "Meio de defesa", "Prova testemunhal", "Dispensável"], "c": "Meio de defesa"},
        {"e": "A competência para julgar crimes dolosos contra a vida é do:", "a": ["Juiz singular", "Tribunal do Júri", "STF", "STJ", "Delegado"], "c": "Tribunal do Júri"},
        {"e": "O prazo para conclusão do inquérito policial (réu solto) é de:", "a": ["10 dias", "15 dias", "30 dias", "60 dias", "90 dias"], "c": "30 dias"},
        {"e": "A prisão em flagrante deve ser comunicada ao juiz em:", "a": ["12 horas", "24 horas", "48 horas", "72 horas", "5 dias"], "c": "24 horas"},
        {"e": "O princípio do contraditório significa:", "a": ["Direito de não produzir provas", "Direito de se manifestar sobre as provas", "Direito ao silêncio", "Direito de recorrer", "Direito de não ser preso"], "c": "Direito de se manifestar sobre as provas"}
    ]
    
    for q in questoes_cpp:
        letras = ['A','B','C','D','E']
        alts = q['a'][:]
        idx = alts.index(q['c'])
        random.shuffle(letras)
        mapa = {letras[i]: alts[i] for i in range(5)}
        resp = letras[idx]
        db.session.add(Questao(enunciado=q['e'], alternativa_a=mapa['A'], alternativa_b=mapa['B'],
            alternativa_c=mapa['C'], alternativa_d=mapa['D'], alternativa_e=mapa['E'],
            resposta_correta=resp, materia_id=mat_cpp.id))
    
    db.session.commit()
    print('Matérias Direito Penal e Processual Penal adicionadas!')
