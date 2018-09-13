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
        unidad_medida = search("m[a-z]{0,4}[sto]\\b", data, IGNORECASE)
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
    #valores = list()
    for defined_value in defined_values:
        if search('\\b{}\\b'.format(defined_value['type']), data, IGNORECASE):
            return defined_value


def get_specific_value(data, attr = ''):
    """
    Dado un tipo de texto a buscar
    :param data_tokenized:
    :param text_type_to_search:
    :return:
    """
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
        medida_volumen = search('l[a-z]{0,4}[ost]?', data, IGNORECASE)
        if not medida_volumen:
            valor_volumen = float(valor_volumen) / 1000

    return valor_volumen


def get_num_value(data):
    """

    :param data_tokenized:
    :return: entrega el token que contenga solo valor numerico
    """
    num_value = search('\\b\d*[.,]*\d+', data).group()
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


def extract_atribute(data, attribute):
    """
    En base al atributo se extrae la información segun el tipo de valor que se espera
    :param data_tokenized:
    :param attribute:
    :return:
    """
    """
    type_attribute = attribute['observation']
    attribute_value = None
    if type_attribute == 'dimension':
        tipo_medida = search('largo|ancho|alto',attribute['value'],IGNORECASE)
        if tipo_medida:
            tipo_medida = tipo_medida.group().lower()
            attribute_value = get_alto_ancho_largo(data, tipo_medida)
        else:
            attribute_value = get_alto_ancho_largo(data)
    elif type_attribute == 'masa':
        attribute_value = get_masa(data)
    elif type_attribute == 'opciones':
        attribute_value = get_defined_values(data,attribute['types'])
    elif type_attribute == 'numero':
        attribute_value = get_num_value(data)
    elif type_attribute == 'generico':
        attribute_value = get_specific_value(data, attribute['value'])
    elif type_attribute == 'capacidad':
        attribute_value = get_volumen_litros(data)
    return attribute_value
    """
    attribute_name = attribute['value']
    attribute_options = attribute['types']
    if len(attribute_options):
        attribute_value = get_defined_values(data, attribute_options)
    else:
        attribute_type = search('\\b(alto|largo|ancho)\\b', attribute_name, IGNORECASE)
        if attribute_type:
            attribute_value = get_alto_ancho_largo(data, attribute_type.group().lower())
        else:
            attribute_type = search('\\bpeso\\b', attribute_name, IGNORECASE)
            if attribute_type:
                attribute_value = get_masa(data)
            else:
                attribute_value = get_specific_value(data, attribute_name)
    return attribute_value