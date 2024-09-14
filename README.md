# Integração com Google Calendar

Este projeto integra o Google Calendar com o seu aplicativo Django usando o Django Rest Framework (DRF). Ele permite criar e deletar eventos no Google Calendar usando a API do Google.

## Pré-requisitos

- Python 3.6+
- Django
- Google API Client Library for Python (`google-api-python-client`)
- Biblioteca `python-dotenv` para carregar variáveis de ambiente

## Instalação

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/juanpinheirx/wlc-google-calendar2
    cd seu-repositorio
    ```

2. **Crie um ambiente virtual**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure as credenciais do Google API**:

    - Vá para o [Google Cloud Console](https://console.cloud.google.com/).
    - Crie um novo projeto ou selecione um projeto existente.
    - Ative a API do Google Calendar.
    - Crie credenciais OAuth 2.0 e baixe o arquivo `credentials.json`.
    - Coloque o arquivo `credentials.json` no diretório pai do seu projeto.

5. **Configure as variáveis de ambiente**:

    - Crie um arquivo `.env` no diretório pai do seu projeto com as seguintes variáveis:

      ```env
      SECRET_KEY=your_secret_key
      DEBUG=True
      ALLOWED_HOSTS=localhost,127.0.0.1
      ```

6. **Execute as migrações do Django**:

    ```bash
    python manage.py migrate
    ```

7. **Crie um superusuário**:

    ```bash
    python manage.py createsuperuser
    ```

8. **Execute o servidor**:

    ```bash
    python manage.py runserver
    ```

## Uso

### Endpoints da API

A API fornece endpoints para criar e deletar eventos no Google Calendar.

#### Criar um Evento

**Endpoint**: `POST /api/tasks/`

**Exemplo de Requisição**:

```json
{
     "title": "Reunião de Projeto",
     "description": "Discussão sobre o progresso do projeto",
     "date": "2023-10-01",
     "time": "14:00:00"
}
```

**Exemplo de Resposta**:

```json
{
     "id": 1,
     "title": "Reunião de Projeto",
     "description": "Discussão sobre o progresso do projeto",
     "date": "2023-10-01",
     "time": "14:00:00",
     "google_calendar_id": "abc123"
}
```

#### Deletar um Evento

**Endpoint**: `DELETE /api/tasks/<id>/`

**Exemplo de Resposta**:

```json
{
     "message": "Evento deletado com sucesso"
}
```

## Estrutura do Projeto

```plaintext
seu-repositorio/
├── credentials.json  # Arquivo de credenciais do Google API
├── .env  # Arquivo de variáveis de ambiente
├── seu_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── google_calendar.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── requirements.txt
└── ...
```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).