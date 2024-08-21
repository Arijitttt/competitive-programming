def sparse_array(strings,quaries):
    result = []
    for query in quaries:
        count = strings.count(query)
        result.append(count)

    return result

strings = ['ab','ab','abc']
quaries = ['ab','abc','bc']

print(sparse_array(strings,quaries))