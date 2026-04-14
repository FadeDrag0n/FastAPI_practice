list_ = [{'id': 1, 'name': ''}, {'id': 2, 'name': ''}, {'id': 3, 'name': ''}]


def deleting(id_):
    for item in list_:
        if item["id"] == id_:
            list_.remove(item)
    return f'success'


print(deleting(1))
print(list_)
