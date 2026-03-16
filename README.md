# 📚 SimuladoPro - Sistema de Simulados para Concursos

Sistema completo de simulados online para concursos públicos com cronômetro, correção automática e histórico de desempenho.

## 🎯 Funcionalidades

- ✅ Sistema de login e cadastro
- ✅ 5 concursos disponíveis
- ✅ Cronômetro em tempo real
- ✅ Correção automática com gabarito
- ✅ Análise de desempenho por matéria
- ✅ Histórico de simulados realizados
- ✅ Respostas embaralhadas aleatoriamente
- ✅ Design responsivo (mobile-friendly)

## 📋 Concursos Disponíveis

1. **Polícia Federal 2024** (CEBRASPE)
   - Português, Matemática, Direito Constitucional

2. **Banco do Brasil 2024** (FGV)
   - Matemática Financeira, Conhecimentos Bancários, Português

3. **SESA-PR 2024** (COPS-UEL)
   - Português, Legislação do SUS, Conhecimentos Gerais

4. **Prefeitura Rio Branco do Sul - PR** (FAUEL)
   - Língua Portuguesa, Matemática, Conhecimentos Gerais

5. **Polícia Civil do Paraná 2024** (PUC-PR)
   - Língua Portuguesa, Direito Penal, Direito Processual Penal

## 🚀 Como usar localmente

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o aplicativo:
```bash
python app.py
```

3. Acesse no navegador:
```
http://127.0.0.1:5000
```

## 🌐 Deploy na Internet (Gratuito)

Siga o guia completo em: [DEPLOY_RENDER.md](DEPLOY_RENDER.md)

## 🛠️ Tecnologias

- **Backend**: Python + Flask
- **Banco de Dados**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Autenticação**: Werkzeug (hash de senhas)

## 📊 Estrutura do Projeto

```
simulado_concursos/
├── app.py                  # Backend Flask
├── requirements.txt        # Dependências
├── Procfile               # Config Render
├── data/
│   └── questoes.json      # Banco de questões
├── templates/             # HTML
│   ├── base.html
│   ├── login.html
│   ├── cadastro.html
│   ├── dashboard.html
│   ├── simulado.html
│   └── historico.html
└── static/
    └── css/
        └── style.css      # Estilos
```

## 📝 Licença

Projeto livre para uso educacional.

## 👨‍💻 Desenvolvido com ❤️

Sistema desenvolvido para auxiliar candidatos na preparação para concursos públicos.
