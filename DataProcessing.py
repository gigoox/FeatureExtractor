# coding=utf-8
import CleanData, nltk, ClasificateProduct, unidecode, AttributeExtractor
from nltk.stem import SnowballStemmer
from re import search, IGNORECASE, sub
from nltk import word_tokenize
from sys import argv
from simplejson import loads, dumps


class AttributeValue(object):
    def __init__(self, attribute_id, attribute_value):
        self.attributes_id = attribute_id
        self.description = attribute_value if attribute_value else ''


def download_modules():
    nltk.download()


def process_data(json_data):
    stemmer = SnowballStemmer('spanish')
    attributes = ClasificateProduct.get_attributes(json_data)
    clean_data_line = CleanData.cleanData(json_data['description'])
    attribute_collected = list()
    for attribute in attributes:
        attribute_value = None
        # Limpia elementos innecesarios del atributo
        clean_attribute = sub('\(.*\)', '', attribute['value'])
        posible_attribute = get_attributes(clean_attribute, clean_data_line, stemmer)
        if not posible_attribute:
            for synonym_attr in get_synonyms(clean_attribute):
                posible_attribute = get_attributes(synonym_attr, clean_data_line, stemmer)
                if posible_attribute:
                    break
        if posible_attribute:
            attribute_value = AttributeExtractor.extract_atribute(posible_attribute, attribute)
        attribute_collected.append(dumps(AttributeValue(attribute['id'], attribute_value).__dict__))

    print dumps(attribute_collected)
    # print clean_data_line


def get_attributes(attribute, data_lines, stemmer):
    # print "Atributo "+attribute

    token_attribute_regex = ''
    for token_attribute in word_tokenize(attribute):
        token_attribute_regex = '{}{}{}'.format(token_attribute_regex, '.*', stemmer.stem(token_attribute))

    for line in data_lines:
        if search(token_attribute_regex, line, IGNORECASE):
            # print data_line_token
            return line


def get_synonyms(attribute):
    synonyms = list()
    # sinonimos para medidas de tamano
    synonyms_size = ['dimension', 'tamano']
    for synonym_size in synonyms_size:
        if search('largo|ancho|alto', attribute, IGNORECASE):
            synonyms.append(sub('(?i)(largo|ancho|alto)', synonym_size, attribute))
    return synonyms


def main():
    print '--------------------------------------'
    data = unidecode.unidecode(argv[1].decode("utf-8"))
    process_data(loads(data))


if __name__ == '__main__':
    main()
