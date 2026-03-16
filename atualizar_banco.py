from app import app, db, Usuario, Acesso
from datetime import datetime

with app.app_context():
    # Criar novas tabelas
    db.create_all()
    
    # Atualizar usuários existentes sem data de criação
    usuarios_sem_data = Usuario.query.filter_by(criado_em=None).all()
    for u in usuarios_sem_data:
        u.criado_em = datetime.utcnow()
    
    if usuarios_sem_data:
        db.session.commit()
        print(f'{len(usuarios_sem_data)} usuários atualizados com data de criação')
    
    print('Banco de dados atualizado com sucesso!')
    print(f'Total de usuários: {Usuario.query.count()}')
    print(f'Total de acessos registrados: {Acesso.query.count()}')
