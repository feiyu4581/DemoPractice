
begain_str = "it's begain"
end_str = "it's end"

memory_dict = {}


def run(x, y):
    if x == 0:
        return {'counts': y, 'message': 'begain'}
    if y == 0:
        return {'counts': x, 'message': 'begain'}

    key = str(x) + ',' + str(y)
    if memory_dict.get(key):
        return memory_dict.get(key)

    deletion = run(x - 1, y)
    insertion = run(x, y - 1)
    equal = run(x - 1, y - 1)

    if deletion.get('counts') < insertion.get('counts') and deletion.get('counts') < equal.get('counts'):
        value = {'counts': deletion.get('counts') + 1, 'message': deletion.get('message') + '\ndeletion' + str(x)}

    elif insertion.get('counts') < deletion.get('counts') and insertion.get('counts') < equal.get('counts'):
        value = {'counts': insertion.get('counts') + 1, 'message': insertion.get('message') + '\ninsertion' + str(x)}

    else:
        if begain_str[x - 1] == end_str[y - 1]:
            value = {'counts': equal.get('counts'), 'message': equal.get('message') + '\nnothing' + str(x)}
        else:
            value = {'counts': equal.get('counts') + 1, 'message': equal.get('message') + '\nreplace' + str(x)}

    memory_dict.update({key: value})

    return value


print run(len(begain_str), len(end_str))
