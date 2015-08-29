def filter(func,seq):
    filtered_seq = []
    for eachItem in seq:
        if func(eachItem):
            filtered_seq.append(eachItem)
    return filtered_seq


