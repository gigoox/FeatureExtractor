import CleanData, ObtainData, nltk, ClasificateProduct
from nltk.stem import SnowballStemmer
from nltk import word_tokenize
from re import match

def downloadModules():
    nltk.download()


def processData():
    attributes = ClasificateProduct.clasificateAndGetAttributes()
    clean_data_lines = CleanData.cleanData(ObtainData.getData())
    clean_data_line_tokens = [[clean_data_line, word_tokenize(clean_data_line)] for clean_data_line in clean_data_lines]
    attribute_collected = dict()
    for attribute in attributes:
        attribute_collected[attribute] = getPosibleAttributes(attribute, clean_data_line_tokens)

    print attribute_collected


def getPosibleAttributes(attribute, data_line_tokens):
    print "Atributo "+attribute
    stemmed_attribute = stemmer.stem(attribute)
    for data_line_token in data_line_tokens:
        for token in data_line_token[1]:
            if match(stemmed_attribute, stemmer.stem(token)):
                print data_line_token
                return data_line_token




stemmer = SnowballStemmer('spanish')
processData()
