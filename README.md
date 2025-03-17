# NexoAPI

**NexoAPI** é uma API RESTful desenvolvida em Python, projetada para fornecer serviços essenciais ao aplicativo Nexo. Esta API lida com operações CRUD, autenticação de usuários e outras funcionalidades necessárias para o funcionamento do aplicativo.

## 🚀 Objetivos do Projeto

- **Desenvolvimento de uma API RESTful**: Implementação de uma API seguindo os princípios REST para comunicação eficiente com o frontend.
- **Gestão de Dados**: Manipulação e armazenamento seguro de dados dos usuários e das funcionalidades do aplicativo.
- **Autenticação e Autorização**: Implementação de mecanismos seguros para autenticação e autorização de usuários.

## 🛠️ Tecnologias Utilizadas

- **Python** → Linguagem principal do desenvolvimento.
- **FastAPI** → Framework moderno e de alto desempenho para construção de APIs com Python 3.7+ baseado em padrões do Python-type hints.
- **SQLAlchemy** → ORM (Object-Relational Mapping) para interações com o banco de dados.
- **Alembic** → Ferramenta de migração de banco de dados para SQLAlchemy.
- **Banco de Dados** → Dependendo do ambiente e necessidade, pode-se utilizar SQLite para desenvolvimento e PostgreSQL para produção.
- **Pytest** → Framework de testes para Python.

## 📌 Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

- **app/**
  - **api/**: Contém os endpoints da API.
  - **core/**: Configurações centrais, como segurança e configurações da aplicação.
  - **db/**: Configurações e modelos do banco de dados.
  - **models/**: Definições das classes que representam as tabelas do banco de dados.
  - **schemas/**: Definições dos schemas Pydantic para validação e serialização de dados.
  - **services/**: Lógica de negócios e manipulação de dados.
  - **tests/**: Casos de teste para as funcionalidades da API.
  - **main.py**: Ponto de entrada da aplicação.

## 🔧 Configuração e Execução

Para configurar e executar o projeto localmente, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/gottard1/NexoAPI.git
   cd NexoAPI
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   - Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
     ```
     DATABASE_URL=sqlite:///./test.db  # Ou a URL do banco de dados que estiver utilizando
     SECRET_KEY=sua_chave_secreta
     ALGORITHM=HS256
     ACCESS_TOKEN_EXPIRE_MINUTES=30
     ```

5. **Execute as migrações do banco de dados:**
   ```bash
   alembic upgrade head
   ```

6. **Inicie o servidor:**
   ```bash
   uvicorn app.main:app --reload
   ```

7. **Acesse a documentação interativa da API:**
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📄 Licença

Este projeto está licenciado sob a [Nome da Licença]. Consulte o arquivo `LICENSE` para mais informações.

## 📞 Contato

Para mais informações ou suporte, entre em contato com [Marcel Felipe] em [marcel.id22@gmail.com].
