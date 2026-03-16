from app import app, db, Concurso, Materia, Questao
import random

with app.app_context():
    concurso = Concurso.query.filter_by(nome='SESA-PR 2024').first()
    
    # Matéria: Legislação do SUS
    mat_sus = Materia(nome='Legislação do SUS', concurso_id=concurso.id)
    db.session.add(mat_sus)
    db.session.flush()
    
    questoes_sus = [
        {"e": "A Lei 8.080/90 dispõe sobre as condições para promoção, proteção e recuperação da saúde. Qual princípio NÃO está previsto no SUS?", "a": ["Universalidade", "Integralidade", "Equidade", "Hierarquização", "Lucratividade"], "c": "Lucratividade"},
        {"e": "Segundo a Constituição Federal de 1988, a saúde é:", "a": ["Dever exclusivo do Estado", "Direito de todos e dever do Estado", "Responsabilidade individual", "Serviço privado", "Opcional"], "c": "Direito de todos e dever do Estado"},
        {"e": "Qual instância é responsável pela formulação de estratégias e controle da execução da política de saúde?", "a": ["Conselho de Saúde", "Secretaria de Saúde", "Ministério da Saúde", "Vigilância Sanitária", "ANVISA"], "c": "Conselho de Saúde"},
        {"e": "A participação da comunidade no SUS é garantida através de:", "a": ["Conselhos e Conferências de Saúde", "Apenas votação", "Doações financeiras", "Trabalho voluntário obrigatório", "Nenhuma forma"], "c": "Conselhos e Conferências de Saúde"},
        {"e": "O SUS é financiado com recursos:", "a": ["Apenas federais", "Apenas estaduais", "Apenas municipais", "Das três esferas de governo", "Apenas de doações"], "c": "Das três esferas de governo"},
        {"e": "A descentralização no SUS significa:", "a": ["Centralizar tudo em Brasília", "Redistribuir responsabilidades entre União, Estados e Municípios", "Privatizar serviços", "Eliminar postos de saúde", "Reduzir atendimentos"], "c": "Redistribuir responsabilidades entre União, Estados e Municípios"},
        {"e": "Qual NOK é uma atribuição do SUS?", "a": ["Vigilância sanitária", "Vigilância epidemiológica", "Saúde do trabalhador", "Venda de medicamentos com lucro", "Assistência terapêutica"], "c": "Venda de medicamentos com lucro"},
        {"e": "A integralidade da assistência no SUS refere-se a:", "a": ["Atendimento parcial", "Conjunto articulado de ações preventivas e curativas", "Apenas emergências", "Somente consultas", "Atendimento pago"], "c": "Conjunto articulado de ações preventivas e curativas"},
        {"e": "O controle social no SUS é exercido por:", "a": ["Apenas médicos", "Gestores de saúde", "Conselhos de Saúde com participação popular", "Empresas privadas", "Políticos"], "c": "Conselhos de Saúde com participação popular"},
        {"e": "A Lei 8.142/90 trata de:", "a": ["Financiamento do SUS", "Participação da comunidade e transferências intergovernamentais", "Privatização da saúde", "Planos de saúde", "Medicamentos"], "c": "Participação da comunidade e transferências intergovernamentais"},
        {"e": "Qual é a base territorial de atuação do SUS?", "a": ["Nacional apenas", "Estadual apenas", "Municipal", "Internacional", "Regional apenas"], "c": "Municipal"},
        {"e": "A universalidade no SUS significa:", "a": ["Atendimento apenas para contribuintes", "Acesso para todos sem discriminação", "Atendimento pago", "Apenas emergências", "Serviço limitado"], "c": "Acesso para todos sem discriminação"},
        {"e": "O Pacto pela Saúde estabelece compromissos entre:", "a": ["Apenas hospitais", "Gestores das três esferas de governo", "Médicos e pacientes", "Empresas privadas", "ONGs"], "c": "Gestores das três esferas de governo"},
        {"e": "A Atenção Básica no SUS é caracterizada por:", "a": ["Alta complexidade", "Primeiro nível de atenção e porta de entrada", "Apenas cirurgias", "Atendimento terciário", "Emergências"], "c": "Primeiro nível de atenção e porta de entrada"},
        {"e": "Qual princípio do SUS garante atendimento conforme necessidades específicas?", "a": ["Universalidade", "Integralidade", "Equidade", "Descentralização", "Hierarquização"], "c": "Equidade"}
    ]
    
    for q in questoes_sus:
        letras = ['A','B','C','D','E']
        alts = q['a'][:]
        idx = alts.index(q['c'])
        random.shuffle(letras)
        mapa = {letras[i]: alts[i] for i in range(5)}
        resp = letras[idx]
        db.session.add(Questao(enunciado=q['e'], alternativa_a=mapa['A'], alternativa_b=mapa['B'],
            alternativa_c=mapa['C'], alternativa_d=mapa['D'], alternativa_e=mapa['E'],
            resposta_correta=resp, materia_id=mat_sus.id))
    
    # Matéria: Conhecimentos Gerais
    mat_cg = Materia(nome='Conhecimentos Gerais', concurso_id=concurso.id)
    db.session.add(mat_cg)
    db.session.flush()
    
    questoes_cg = [
        {"e": "O Paraná faz divisa com qual país?", "a": ["Uruguai", "Argentina", "Bolívia", "Chile", "Peru"], "c": "Argentina"},
        {"e": "A capital do Paraná é:", "a": ["Londrina", "Maringá", "Curitiba", "Ponta Grossa", "Cascavel"], "c": "Curitiba"},
        {"e": "Qual é o bioma predominante no Paraná?", "a": ["Amazônia", "Cerrado", "Mata Atlântica", "Caatinga", "Pampa"], "c": "Mata Atlântica"},
        {"e": "O Paraná é conhecido nacionalmente pela produção de:", "a": ["Cacau", "Café", "Algodão", "Cana-de-açúcar", "Arroz"], "c": "Café"},
        {"e": "Qual rio forma a fronteira entre Paraná e Mato Grosso do Sul?", "a": ["Rio Iguaçu", "Rio Paraná", "Rio Tibagi", "Rio Ivaí", "Rio Paranapanema"], "c": "Rio Paraná"},
        {"e": "As Cataratas do Iguaçu estão localizadas em qual cidade paranaense?", "a": ["Curitiba", "Londrina", "Foz do Iguaçu", "Paranaguá", "Maringá"], "c": "Foz do Iguaçu"},
        {"e": "Qual é o principal porto do Paraná?", "a": ["Santos", "Paranaguá", "Rio Grande", "Itajaí", "Vitória"], "c": "Paranaguá"},
        {"e": "O Paraná foi desmembrado de qual província em 1853?", "a": ["Rio de Janeiro", "Minas Gerais", "São Paulo", "Santa Catarina", "Rio Grande do Sul"], "c": "São Paulo"},
        {"e": "Qual é a população aproximada do Paraná?", "a": ["5 milhões", "8 milhões", "11 milhões", "15 milhões", "20 milhões"], "c": "11 milhões"},
        {"e": "O clima predominante no Paraná é:", "a": ["Equatorial", "Tropical", "Subtropical", "Semiárido", "Desértico"], "c": "Subtropical"},
        {"e": "Qual cidade paranaense é conhecida como 'Capital do Café'?", "a": ["Curitiba", "Londrina", "Maringá", "Apucarana", "Cornélio Procópio"], "c": "Londrina"},
        {"e": "A Serra do Mar está localizada em qual região do Paraná?", "a": ["Norte", "Sul", "Leste", "Oeste", "Centro"], "c": "Leste"},
        {"e": "Qual é o gentílico de quem nasce no Paraná?", "a": ["Paranense", "Paranaense", "Paranista", "Paranauense", "Paraniano"], "c": "Paranaense"},
        {"e": "O Parque Nacional do Iguaçu foi criado em:", "a": ["1900", "1939", "1950", "1970", "1988"], "c": "1939"},
        {"e": "Qual universidade pública é a mais antiga do Paraná?", "a": ["UEL", "UEM", "UFPR", "UEPG", "UNIOESTE"], "c": "UFPR"}
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
    print('Matérias SUS e Conhecimentos Gerais adicionadas!')
