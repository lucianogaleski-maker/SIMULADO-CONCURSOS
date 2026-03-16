# 🚀 GUIA DE DEPLOY NO PYTHONANYWHERE (SUPER FÁCIL)

## ✅ Vantagens do PythonAnywhere
- Não precisa GitHub
- Upload direto pelo navegador
- Interface visual simples
- 100% gratuito

---

## 📋 PASSO A PASSO COMPLETO

### **PASSO 1: Criar conta** (2 minutos)

1. Acesse: **https://www.pythonanywhere.com**
2. Clique em **"Start running Python online in less than a minute"**
3. Clique em **"Create a Beginner account"** (gratuito)
4. Preencha:
   - Username (exemplo: `joaosilva`)
   - Email
   - Senha
5. Confirme o email

---

### **PASSO 2: Fazer upload dos arquivos** (5 minutos)

1. Faça login no PythonAnywhere
2. Clique na aba **"Files"** (Arquivos)
3. Clique em **"Upload a file"**
4. Faça upload de **TODOS** estes arquivos da pasta `C:\simulado_concursos`:

**Arquivos principais:**
- `app.py`
- `requirements.txt`
- `Procfile`

**Pastas (criar antes):**
- Clique em "New directory" e crie: `templates`
- Clique em "New directory" e crie: `static`
- Clique em "New directory" e crie: `data`

**Depois faça upload dentro de cada pasta:**

📁 **templates/** (subir todos os .html):
- `base.html`
- `login.html`
- `cadastro.html`
- `dashboard.html`
- `simulado.html`
- `historico.html`

📁 **static/css/** (criar pasta css dentro de static):
- `style.css`

📁 **data/**:
- `questoes.json`

---

### **PASSO 3: Criar Web App** (3 minutos)

1. Clique na aba **"Web"**
2. Clique em **"Add a new web app"**
3. Clique em **"Next"** (aceitar o domínio gratuito)
4. Escolha **"Flask"**
5. Escolha **"Python 3.10"**
6. Em "Path", deixe: `/home/SEU_USUARIO/mysite/flask_app.py`
7. Clique em **"Next"**

---

### **PASSO 4: Configurar o app** (5 minutos)

1. Na página "Web", role até **"Code"**
2. Clique no link do arquivo **"WSGI configuration file"**
3. **DELETE TODO O CONTEÚDO** do arquivo
4. Cole este código:

```python
import sys
import os

# Adicionar o diretório ao path
path = '/home/SEU_USUARIO'  # ⚠️ TROQUE SEU_USUARIO pelo seu username
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

5. Clique em **"Save"** (salvar)

---

### **PASSO 5: Instalar dependências** (3 minutos)

1. Clique na aba **"Consoles"**
2. Clique em **"Bash"**
3. Digite estes comandos (um de cada vez):

```bash
pip3 install --user flask flask-sqlalchemy werkzeug beautifulsoup4 requests
```

4. Aguarde instalar (1-2 minutos)

---

### **PASSO 6: Inicializar banco de dados** (2 minutos)

No mesmo console Bash, digite:

```bash
cd ~
python3 -c "from app import app, db; app.app_context().push(); db.create_all(); print('Banco criado!')"
```

---

### **PASSO 7: Ativar o site** (1 minuto)

1. Volte na aba **"Web"**
2. Role até o topo
3. Clique no botão verde **"Reload SEU_USUARIO.pythonanywhere.com"**
4. Aguarde 10 segundos

---

### **PASSO 8: Acessar seu site! 🎉**

Seu site estará em:
```
https://SEU_USUARIO.pythonanywhere.com
```

Exemplo: `https://joaosilva.pythonanywhere.com`

---

## ⚠️ OBSERVAÇÕES

- **Gratuito para sempre**
- **Não precisa cartão**
- Limite: 100.000 acessos/dia (mais que suficiente)
- O site fica online 24/7

---

## 🔄 Para atualizar o site:

1. Vá em **"Files"**
2. Clique no arquivo que quer editar
3. Faça as alterações
4. Salve
5. Vá em **"Web"** e clique em **"Reload"**

---

## 🆘 Problemas comuns:

**Erro 502 ou site não carrega:**
- Vá em "Web" → "Error log" e veja o erro
- Certifique-se que trocou `SEU_USUARIO` no WSGI

**Banco de dados vazio:**
- Execute novamente o comando do Passo 6

**CSS não carrega:**
- Vá em "Web" → "Static files"
- Adicione:
  - URL: `/static/`
  - Directory: `/home/SEU_USUARIO/static/`

---

## ✅ PRONTO!

Agora qualquer pessoa pode acessar seu simulado online!
