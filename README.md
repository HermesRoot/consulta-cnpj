# Consulta CNPJ

Este é um projeto simples para consulta de CNPJ utilizando Flask no backend e uma interface web no frontend.

## 🖥️ Captura de Tela
![Screenshot do consulta-cnpj](https://raw.githubusercontent.com/HermesRoot/consulta-cnpj/refs/heads/main/screenshot.jpg)

## 📌 Tecnologias Utilizadas

- **Backend:** Flask, Flask-CORS, Requests  
- **Frontend:** HTML, CSS, JavaScript (Fetch API, SweetAlert2)

## 🔥 Funcionalidades

✅ Consulta de CNPJ via BrasilAPI

✅ Validação do CNPJ antes da requisição

✅ Interface moderna e responsiva

✅ Exibição detalhada das informações da empresa

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o Repositório 

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows
```
### 3️⃣ Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o Backend

```bash
python api_cnpj.py  # Ou o nome do seu arquivo Flask
```

O servidor rodará em `http://localhost:5001`.

### 5️⃣ Executar o Frontend

Basta abrir o arquivo `consulta_cnpj.html` no navegador.

### 💡 Dica: Caso queira testar a API sem rodar o frontend, basta acessar no navegador:

```bash
http://localhost:5001/consulta-cnpj?cnpj=00000000000191
```

(Substitua pelo CNPJ desejado)

## 📝 Licença

Este projeto está licenciado sob a licença **MIT** — veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

Desenvolvido por **HermesRoot**.



















