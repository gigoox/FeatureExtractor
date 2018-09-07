# coding=utf-8
from re import match, IGNORECASE


def get_alto_ancho_largo_cm(data_tokenized):
    """
    :param data_tokenized:
    :return: el valor del alto, ancho o largo en cm
    """
    valor = None
    unidad_medida = None
    for token in data_tokenized:
        if not valor and match("^\d+[.,]?\d*", token):
            valor = token
        if not unidad_medida and match("^m[a-z]*[sto]$", token, IGNORECASE ):
            unidad_medida = token

    if unidad_medida:
        valor = float(valor) * 100

    return valor


def get_alto_ancho_largo_mt(data_tokenized):
    """
    :param data_tokenized:
    :return: el valor del alto, ancho o largo en cm
    """
    valor = None
    unidad_medida = None
    for token in data_tokenized:
        if not valor and match("^\d+[.,]?\d*", token):
            valor = token
        if not unidad_medida and match("^m[a-z]*[sto]$", token, IGNORECASE):
            unidad_medida = token

    if not unidad_medida:
        valor = float(valor) / 100

    return valor


def get_defined_values(data_tokenized, defined_values):
    """
    De una lista de valores intenta recuperar los valores que coinciden
    :param data_tokenized:
    :param defined_values:
    :return: lista con los valores encontrados
    """
    valores = list()
    for token in data_tokenized:
        for defined_value in defined_values:
            if match(defined_value, token):
                valores.append(token)
                defined_values.remove(defined_value)

    return valores


def get_specific_value(data_tokenized, text_type_to_search):
    """
    Dado un tipo de texto a buscar
    :param data_tokenized:
    :param text_type_to_search:
    :return:
    """
    if text_type_to_search == 'nombre':
        name = ' '
        nameList = list()
        for token in data_tokenized:
            if match('^[A-Z][.A-Za-z]*', token):
                nameList.append(token)
        return name.join(nameList)


def get_volumen_litros(data_tokenized):
    """
    :param data_tokenized:
    :return: cantidad de volumen en litros
    """
    valor_volumen = None
    medida_volumen = None
    for token in data_tokenized:
        if not valor_volumen and match('^\d+[.,]?\d*', token):
            valor_volumen = token
        if not medida_volumen:
            if match('^l[a-z]*[ost]', token, IGNORECASE):
                medida_volumen = 'lt'
            elif match('^cc', token, IGNORECASE):
                medida_volumen = 'cc'

    if not medida_volumen:
        if medida_volumen == 'cc':
            valor_volumen = float(valor_volumen) / 1000

    return valor_volumen


def get_integer_num_value(data_tokenized):
    """

    :param data_tokenized:
    :return: entrega el token que contenga solo valor numerico
    """
    for token in data_tokenized:
        if match('^\d*\d$+', token):
            return token


def get_num_value(data_tokenized):
    """

    :param data_tokenized:
    :return: entrega el token que contenga solo valor numerico
    """
    for token in data_tokenized:
        if match('^\d[\d,.]*\d$', token):
            return token


def get_masa_kg(data_tokenized):
    """
    :param data_tokenized:
    :return: entrega el valor en kilogramos
    """
    valor_masa = None
    medida_masa = None
    for token in data_tokenized:
        if not valor_masa and match("^\d+[.,]?\d*", token):
            valor_masa = token
        if not medida_masa and match("^g[a-z]*[sro]$", token, IGNORECASE):
            medida_masa = token

    if medida_masa:
        valor_masa = float(valor_masa) / 1000

    return valor_masa


def get_masa_gr(data_tokenized):
    """
    :param data_tokenized:
    :return: entrega el valor en gramos
    """
    valor_masa = None
    medida_masa = None
    for token in data_tokenized:
        if not valor_masa and match("^\d+[.,]?\d*", token):
            valor_masa = token
        if not medida_masa and match("^g[a-z]*[sro]$", token, IGNORECASE):
            medida_masa = token

    if not medida_masa:
        valor_masa = float(valor_masa) * 1000

    return valor_masa