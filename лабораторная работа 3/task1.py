# TODO Напишите функцию для поиска индекса товара
def search_item(items_list_f, find_item_f):
    result = None
    if find_item_f in items_list_f:
        result = items_list_f.index(find_item_f)
    return result
    #по своей сути функция является методом index который в случае необнаружения,
    #не будет вызывать ошибку, а возвращать None
    #если не прибегать к методу то надо было пройтись циклом по списку со строгим условием равенства


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_item(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
