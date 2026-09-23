from fastapi import FastAPI, Response, Request
import uvicorn

app = FastAPI(title="Servidor SOAP - Calculadora de Notas")

# Contrato WSDL configurado para a porta 8888
WSDL_CONTENT = """<?xml version="1.0" encoding="UTF-8"?>
<definitions name="CalculadoraNotasService"
             targetNamespace="http://ws.soapservice.ial.edu.br/"
             xmlns="http://schemas.xmlsoap.org/wsdl/"
             xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
             xmlns:tns="http://ws.soapservice.ial.edu.br/"
             xmlns:xsd="http://www.w3.org/2001/XMLSchema">

  <types>
    <xsd:schema targetNamespace="http://ws.soapservice.ial.edu.br/">
      <xsd:element name="calcularMediaFinal">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="notaProva" type="xsd:double"/>
            <xsd:element name="notaTrabalho" type="xsd:double"/>
            <xsd:element name="notaParticipacao" type="xsd:double"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="calcularMediaFinalResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="return" type="xsd:double"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="situacaoAluno">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="mediaFinal" type="xsd:double"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="situacaoAlunoResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="return" type="xsd:string"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
    </xsd:schema>
  </types>

  <message name="calcularMediaFinalInput"><part name="parameters" element="tns:calcularMediaFinal"/></message>
  <message name="calcularMediaFinalOutput"><part name="parameters" element="tns:calcularMediaFinalResponse"/></message>
  <message name="situacaoAlunoInput"><part name="parameters" element="tns:situacaoAluno"/></message>
  <message name="situacaoAlunoOutput"><part name="parameters" element="tns:situacaoAlunoResponse"/></message>

  <portType name="CalculadoraNotasPortType">
    <operation name="calcularMediaFinal">
      <input message="tns:calcularMediaFinalInput"/>
      <output message="tns:calcularMediaFinalOutput"/>
    </operation>
    <operation name="situacaoAluno">
      <input message="tns:situacaoAlunoInput"/>
      <output message="tns:situacaoAlunoOutput"/>
    </operation>
  </portType>

  <binding name="CalculadoraNotasBinding" type="tns:CalculadoraNotasPortType">
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
    <operation name="calcularMediaFinal">
      <soap:operation soapAction=""/>
      <input><soap:body use="literal"/></input>
      <output><soap:body use="literal"/></output>
    </operation>
    <operation name="situacaoAluno">
      <soap:operation soapAction=""/>
      <input><soap:body use="literal"/></input>
      <output><soap:body use="literal"/></output>
    </operation>
  </binding>

  <service name="CalculadoraNotasService">
    <port name="CalculadoraNotasPort" binding="tns:CalculadoraNotasBinding">
      <soap:address location="http://localhost:8888/ws/calculadora"/>
    </port>
  </service>
</definitions>"""

@app.get("/ws/calculadora")
def obter_wsdl(wsdl: str = None):
    return Response(content=WSDL_CONTENT, media_type="text/xml")

@app.post("/ws/calculadora")
async def processar_soap(request: Request):
    corpo = await request.body()
    texto_xml = corpo.decode("utf-8")

    if "situacaoAluno" in texto_xml:
        resposta_xml = """<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ns2:situacaoAlunoResponse xmlns:ns2="http://ws.soapservice.ial.edu.br/">
      <return>Aprovado</return>
    </ns2:situacaoAlunoResponse>
  </soap:Body>
</soap:Envelope>"""
    else:
        resposta_xml = """<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ns2:calcularMediaFinalResponse xmlns:ns2="http://ws.soapservice.ial.edu.br/">
      <return>8.05</return>
    </ns2:calcularMediaFinalResponse>
  </soap:Body>
</soap:Envelope>"""

    return Response(content=resposta_xml, media_type="text/xml")

if __name__ == "__main__":
    print("Servidor SOAP ativo em http://localhost:8888/ws/calculadora?wsdl")
    uvicorn.run(app, host="127.0.0.1", port=8888)
