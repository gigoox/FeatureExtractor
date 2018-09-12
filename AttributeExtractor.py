# coding=utf-8
from re import IGNORECASE, findall, search, sub

def get_alto_ancho_largo(data, tipo_medida = 'largo', tipo_medicion = 'cm'):
    """
    :param data_tokenized:
    :return: el valor del alto, ancho o largo en cm
    """
    valor = None
    valores = search('\\b(\d+[,.]?\d*([ a-zA-Z]*)?[xX]{1} ?)(\d+[,.]?\d*)(([ a-zA-Z]*)?[xX]{1} ?)?(\d+[,.]?\d*)?', data)
    if valores:
        valores = findall('\d+[.,]?\d*', valores.group())
        if len(valores) == 2:
            if tipo_medida == 'ancho':
                valor = valores[0]
            elif tipo_medida == 'alto':
                valor = valores[1]
        else:
            if tipo_medida == 'largo':
                valor = valores[0]
            elif tipo_medida == 'ancho':
                valor = valores[1]
            elif tipo_medida == 'alto':
                valor = valores[2]

    else:
        valor = search("\d+[.,]?\d*", data).group()
    if valor:
        unidad_medida = search("m[a-z]*[sto]$", data, IGNORECASE)
        if unidad_medida:
            if tipo_medicion == 'cm':
                valor = float(valor) * 100
        else:
            if tipo_medicion == 'mt':
                valor = float(valor) / 100

    return valor


def get_defined_values(data, defined_values):
    """
    De una lista de valores intenta recuperar los valores que coinciden
    :param data_tokenized:
    :param defined_values:
    :return: lista con los valores encontrados
    """
    valores = list()
    for defined_value in defined_values:
        valores.append(findall(defined_value, data))

    return valores


def get_specific_value(data, text_type_to_search, attr = ''):
    """
    Dado un tipo de texto a buscar
    :param data_tokenized:
    :param text_type_to_search:
    :return:
    """
    value = None
    if text_type_to_search == 'nombre':
        value = search('[A-Z][.A-Za-z]* ([A-Z][.a-z]*) ([A-Z][.a-z]*)', data).group()
    elif text_type_to_search == 'default':
        value = search('(?<={}).*'.format(attr), data, IGNORECASE).group()
        value = sub('[;:=]', '', value)

    return value


def get_volumen_litros(data):
    """
    :param data_tokenized:
    :return: cantidad de volumen en litros
    """
    valor_volumen = search('\d+[.,]?\d*', data).group()
    if valor_volumen:
        medida_volumen = search('l[a-z]{0,4}[ost]?', data, IGNORECASE).group()
        if not medida_volumen:
            valor_volumen = float(valor_volumen) / 1000

    return valor_volumen


def get_integer_num_value(data):
    """

    :param data_tokenized:
    :return: entrega el token que contenga solo valor numerico
    """
    integer_num_value = search('\d*\d', data).group()
    return integer_num_value


def get_num_value(data):
    """

    :param data_tokenized:
    :return: entrega el token que contenga solo valor numerico
    """
    num_value = search('\d[\d,.]*\d$', data).group()
    return num_value


def get_masa(data, tipo_medida = 'gr'):
    """
    :param data_tokenized:
    :return: entrega el valor en kilogramos
    """
    valor_masa = search("\d+[.,]?\d*", data).group()
    if valor_masa:
        medida_masa = search("[^a-z]g[a-z]{0,4}[sro]?", data, IGNORECASE)
        if medida_masa:
            if tipo_medida == 'kg':
                valor_masa = float(valor_masa) / 1000
        else:
            if tipo_medida == 'gr':
                valor_masa = float(valor_masa) * 1000

    return valor_masa


def extractAtribute(data, attribute, values = list()):
    """
    En base al atributo se extrae la información segun el tipo de valor que se espera
    :param data_tokenized:
    :param attribute:
    :return:
    """

print get_alto_ancho_largo('Dimensiones: 9.2 metros x 7.7 metros x 2.2 metros','alto')