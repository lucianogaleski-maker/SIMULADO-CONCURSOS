# 🚀 GUIA DE DEPLOY NO RENDER.COM (GRATUITO)

## Passo 1: Criar conta no GitHub
1. Acesse https://github.com
2. Crie uma conta gratuita (se não tiver)

## Passo 2: Criar repositório
1. Clique em "New repository"
2. Nome: `simulado-concursos`
3. Deixe como **Público**
4. Clique em "Create repository"

## Passo 3: Subir os arquivos para o GitHub

### Opção A - Via GitHub Web (mais fácil):
1. No repositório criado, clique em "uploading an existing file"
2. Arraste TODOS os arquivos da pasta `C:\simulado_concursos`
3. Clique em "Commit changes"

### Opção B - Via Git (linha de comando):
```bash
cd C:\simulado_concursos
git init
git add .
git commit -m "Primeiro commit"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/simulado-concursos.git
git push -u origin main
```

## Passo 4: Criar conta no Render
1. Acesse https://render.com
2. Clique em "Get Started for Free"
3. Faça login com sua conta do GitHub

## Passo 5: Criar Web Service
1. No dashboard do Render, clique em "New +"
2. Selecione "Web Service"
3. Conecte seu repositório `simulado-concursos`
4. Configure:
   - **Name**: simulado-concursos
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free
5. Clique em "Create Web Service"

## Passo 6: Aguardar Deploy
- O Render vai instalar tudo automaticamente
- Aguarde 5-10 minutos
- Quando aparecer "Live", seu site está no ar!

## Passo 7: Acessar seu site
Seu site estará disponível em:
```
https://simulado-concursos.onrender.com
```

## ⚠️ IMPORTANTE - Banco de Dados

O banco SQLite será criado automaticamente, mas como você já tem concursos cadastrados localmente, você tem 2 opções:

### Opção 1: Deixar vazio (usuários cadastram do zero)
- Não precisa fazer nada
- Cada usuário cria sua conta

### Opção 2: Subir o banco com os concursos
1. Copie o arquivo `instance/simulado.db` para a raiz do projeto
2. Suba novamente para o GitHub
3. O Render vai usar esse banco

## 🎯 Pronto!
Agora qualquer pessoa pode acessar seu simulado pela internet gratuitamente!

## 📝 Observações:
- O plano gratuito do Render "dorme" após 15 minutos sem uso
- O primeiro acesso após "dormir" pode demorar 30-60 segundos
- Não há limite de usuários
- Não há limite de simulados

## 🔄 Para atualizar o site:
1. Faça alterações nos arquivos locais
2. Suba para o GitHub
3. O Render atualiza automaticamente

## 🆘 Problemas?
- Verifique os logs no dashboard do Render
- Certifique-se que todos os arquivos foram enviados
- Verifique se o requirements.txt está correto
