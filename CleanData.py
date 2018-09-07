import re
import unidecode

MAX_CHAR = 50


def cleanData(data):
    """
    :param data: texto inicial
    :return: texto to lowercase, eliminado sparrafos largos
    """

    # Dividimos el texto en parrafos

    attributes = list()
    sections = data.splitlines()
    for section in sections:
        if len(section) <= MAX_CHAR and re.match('[^\W_]',section):
            attributes.append(unidecode.unidecode(section.decode("utf-8")))

    return attributes
