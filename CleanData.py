import re
import unidecode
from nltk import word_tokenize
from re import sub

MAX_CHAR = 65
MIN_LINES = 2


def cleanData(data):
    """
    :param data: texto inicial
    :return: texto to lowercase, eliminado sparrafos largos
    """

    # Dividimos el texto en parrafos

    clean_data = list()
    section_tokenized = list()
    line = None
    data = sub("<br/>|<br>|<p>|</p>", "\\n", data)
    data = sub("<>-_\*", "", data)
    sections = data.splitlines()
    for section in sections:
        section = unidecode.unidecode(section.decode("utf-8"))
        if len(section) <= MAX_CHAR and re.search('[^\W_]', section):
            if not line:
                line = section
            else:
                line = '{} {}'.format(line,section)
            section_tokenized.extend(word_tokenize(section))
            if len(section_tokenized) <= MIN_LINES:
                continue
            else:
                clean_data.append(line)
                line = None
                section_tokenized = list()

    return  clean_data
