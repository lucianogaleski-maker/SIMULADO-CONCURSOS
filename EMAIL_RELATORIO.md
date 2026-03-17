# 📧 SISTEMA DE ENVIO DE RELATÓRIO POR EMAIL

## ⚠️ IMPORTANTE:

O relatório **JÁ ESTÁ PROTEGIDO**! 
- Só você acessa com login: `luka51` / `080898336699`
- URL: `/login-admin`

---

## 📧 Para enviar relatório por email automaticamente:

### **Opção 1: Serviço Externo (Recomendado)**

Use o **cron-job.org** (gratuito):

1. Acesse: https://cron-job.org
2. Crie uma conta gratuita
3. Crie um novo cron job:
   - **URL**: `https://simulado-concursos.onrender.com/enviar-relatorio-email?token=SENHA_SECRETA`
   - **Horário**: `23:59` (todos os dias)
   - **Método**: GET

---

### **Opção 2: Manual (Mais Simples)**

Acesse esta URL sempre que quiser receber o relatório:
```
https://simulado-concursos.onrender.com/enviar-relatorio-email?token=luka51secret
```

O relatório será enviado para: **chaveirogaleski@gmail.com**

---

## 🔧 O que vou implementar:

1. ✅ Rota `/enviar-relatorio-email` protegida por token
2. ✅ Gera relatório em HTML
3. ✅ Envia por email usando serviço gratuito
4. ✅ Email: chaveirogaleski@gmail.com

---

## 📝 Serviços de Email Gratuitos:

Para enviar emails, preciso de um serviço SMTP. Opções:

1. **Gmail** - Você precisa criar uma "Senha de App"
2. **SendGrid** - 100 emails/dia grátis
3. **Mailgun** - 5.000 emails/mês grátis

---

## ❓ Qual você prefere?

1. **Gmail** (usa seu email pessoal)
2. **SendGrid** (serviço profissional)
3. **Manual** (você acessa a URL quando quiser)

Me diga qual opção você quer que eu implemente!
