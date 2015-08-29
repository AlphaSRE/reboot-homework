def red(fuc,seq,initial=None):
    lseq = list(seq)
    if initial is None:
        res = lseq.pop(0)
    else:
        res = initial
    for eachItem in lseq:
        res = func(res,eachItem)
    return res
