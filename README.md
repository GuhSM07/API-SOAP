# API-SOAP

# Web Service SOAP em Python — Calculadora de Notas

Este repositório contém a implementação de um **Web Service SOAP** (servidor e cliente) desenvolvido em Python para a disciplina de **Arquitetura de APIs (IAL-221)**.

## 📌 Visão Geral do Projeto

O projeto demonstra a publicação e o consumo de serviços Web baseados em **SOAP** e contrato **WSDL**:

* **`servidor_soap.py`**: Aplicação que expõe o contrato WSDL no endereço `http://localhost:8888/ws/calculadora?wsdl` e processa as requisições em formato XML.
* **`cliente_soap.py`**: Cliente em Python que utiliza a biblioteca **Zeep** para ler o WSDL e invocar as operações remotas do serviço.

### ⚙️ Operações do Serviço:
1. **`calcularMediaFinal`**: Recebe as notas da prova (peso 50%), trabalho (peso 30%) e participação (peso 20%) e retorna a média calculada.
2. **`situacaoAluno`**: Recebe a média final e indica a situação acadêmica do estudante (`Aprovado`, `Recuperação` ou `Reprovado`).

---

## 🛠️ Pré-requisitos e Instalação

1. Certifique-se de estar com o **Python 3** instalado (ou utilizando o **GitHub Codespaces**).
2. Instale as dependências do projeto através do arquivo `requirements.txt`:

bash
pip install -r requirements.txt



## 🚀 Como Executar

Para demonstrar a comunicação cliente-servidor, abra duas abas de terminal no seu ambiente de desenvolvimento:

### 1 Iniciar o Servidor SOAP

No primeiro terminal, execute:


python servidor_soap.py


*(O console indicará que o serviço está ativo na porta 8888).*

### 2 Executar o Cliente SOAP

Em um segundo terminal, execute:


python cliente_soap.py



### 📊 Saída Esperada no Terminal do Cliente:


--- Invocando Operações do Web Service SOAP ---
Média calculada pelo SOAP: 8.05
Situação do Aluno: Aprovado



---

## 🧰 Tecnologias Utilizadas

* **Python 3**
* **FastAPI &amp; Uvicorn**: Servidor leve para disponibilizar a rota HTTP do WSDL e das chamadas SOAP.
* **Zeep**: Cliente SOAP padrão em Python para interpretação automática de WSDL.



---

### Como criar e salvar o arquivo no seu GitHub

1. No seu VS Code / Codespaces, crie um novo arquivo chamado **`README.md`** na raiz da pasta.
2. Cole o conteúdo acima e salve o arquivo (`Ctrl + S`).
3. No terminal, execute os comandos do Git para enviar para o repositório:
   '''bash
   git add README.md
   git commit -m "Adiciona documentacao README do projeto SOAP"
   git push origin main
