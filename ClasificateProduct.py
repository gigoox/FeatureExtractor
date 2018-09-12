# coding=utf-8
def get_attributes(data):
    '''
    Clasifica el producto en una J específica, y a partir de eso obtiene una lista de categoriuas
    :return:
    '''
    return data['category']['attributes_categories']