import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL ESTÁ VAZIA")
        url = "https://www.bytebank.com.br/cambio"
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)

        if not match:
            raise ValueError('URL NÃO É VALIDA')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        print(indice_interrogacao)
        url_origem = self.url[0:indice_interrogacao]
        return url_origem
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros
    def get_valor_parametro(self, parametro_busca):
        parametro_busca = "quantidade"
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)  # o segundo parametro é onde começa
        if (indice_e_comercial == -1):
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return (self.url)

    def __str__(self):
        return "A URL é: " + self.url

url = '//bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
print(len(url))
print(str(extrator_url))