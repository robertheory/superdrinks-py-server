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

### Usando requests do Thunder Client

1. Instale a extensão Thunder Client no VSCode
2. Importe o arquito `superdrinks-thunder-client-requests.json` no Thunder Client
3. Execute as requests

### Salvando suas requests do Thunder Client
1. Exporte suas requests do Thunder Client
2. Substitua o arquivo `superdrinks-thunder-client-requests.json` pelo seu arquivo exportado


## Roadmap

- [x] Criar projeto
- [x] Criar modelo de drinks
- [x] Criar modelo de ingrediente
- [x] Rotas de drinks
- [ ] Rotas de ingredientes
- [x] Conectar com banco de dados
- [x] Docker

## Exemplos

### Objeto drink

```
{
    "id": "1",
    "name": "Mojito",
    "description": "A refreshing Cuban cocktail",
    "prepare_method": "Muddle mint leaves with sugar and lime juice. Add a splash of soda water and fill the glass with cracked ice. Pour the rum and top with soda water. Garnish and serve with straw.",
    "ingredients": [
        {
            "id": "1",
            "name": "Mint leaves",
            "quantity": 6,
            "prepare": "Muddle",
            "description": "Fresh mint leaves",
            "unit": "leaves"
        },
        {
            "id": "2",
            "name": "Sugar",
            "quantity": 2,
            "prepare": "Muddle",
            "description": "White sugar",
            "unit": "tsp"
        },
        {
            "id": "3",
            "name": "Lime juice",
            "quantity": 1,
            "prepare": "Muddle",
            "description": "Fresh lime juice",
            "unit": "oz"
        },
        {
            "id": "4",
            "name": "Soda water",
            "quantity": 1,
            "prepare": "Top",
            "description": "Soda water",
            "unit": "oz"
        },
        {
            "id": "5",
            "name": "White rum",
            "quantity": 2,
            "prepare": "Pour",
            "description": "White rum",
            "unit": "oz"
        }
    ]
}
```

### Objeto ingredient

```
{
    "id": "1",
    "name": "Mint leaves",
    "quantity": 6,
    "prepare": "Muddle",
    "description": "Fresh mint leaves",
    "unit": "leaves"
}
```