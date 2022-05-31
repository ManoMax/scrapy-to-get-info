import scrapy


class MlSpider(scrapy.Spider):
    name = 'ml'

    start_urls = ['https://www.noticiaparaiba.com.br/noticia/7650/edital-divulga-resultados-das-provas-discursivas-do-concurso-da-policia-civil-da-paraiba']

    def parse(self, response, **kwargs):
        for p in response.xpath('//div[@class="texto"]/p/text()'):
            content = p.get()

            yield {
                content: content
            }
