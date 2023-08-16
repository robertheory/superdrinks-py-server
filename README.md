# superdrinks-py-server

Servidor para a aplicação Super Drinks

## Instalação

### Pré-requisitos

- Python 3.8.5
- Pip 20.0.2
- Virtualenv 20.0.2

### Instalação

1. Clone o repositório
   ```sh
   git clone git@github.com:robertheory/superdrinks-py-server.git
   ```
2. Acesse o diretório do projeto
   ```sh
   cd superdrinks-py-server
   ```
3. Crie um ambiente virtual
   ```sh
   python -m venv venv
   ```
4. Ative o ambiente virtual
   ```sh
   source venv/bin/activate
   ```
5. Instale as dependências
   ```sh
   pip install -r requirements.txt
   ```
6. Execute o servidor

   ```sh
   uvicorn main:app --reload
   ```

7. Acesse o servidor em http://localhost:8000
8. Acesse a documentação da API em http://localhost:8000/docs
9. Acesse a documentação interativa da API em http://localhost:8000/redoc

## Roadmap

- [x] Criar projeto
- [x] Criar modelo de drinks
- [x] Criar modelo de ingrediente
- [x] Rotas de drinks
- [ ] Rotas de ingredientes
- [ ] Conectar com banco de dados
- [ ] Docker
