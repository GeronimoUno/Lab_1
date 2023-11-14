# TODO Напишите функцию для поиска индекса товара
def func():
    list_ = []
    for i in items_list:
        if i is find_item:
            list_.append(items_list.index(i))
    list_.sort()
    list_.append(None)
    return list_[0]
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    index_item = func()  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
