from zeep import Client

wsdl_url = "http://localhost:8888/ws/calculadora?wsdl"

try:
    client = Client(wsdl_url)

    print("--- Invocando Operações do Web Service SOAP ---")

    # 1. Chama a operação de cálculo de média
    media = client.service.calcularMediaFinal(
        notaProva=8.0, 
        notaTrabalho=7.5, 
        notaParticipacao=9.0
    )
    print(f"Média calculada pelo SOAP: {media}")

    # 2. Chama a operação de situação do aluno
    situacao = client.service.situacaoAluno(mediaFinal=media)
    print(f"Situação do Aluno: {situacao}")

except Exception as erro:
    print(f"Erro ao conectar ou executar no servidor SOAP: {erro}")
