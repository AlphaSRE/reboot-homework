def testIn(Val,List):
    idx = 0
    while True:
        if List[idx] == Val:
            print True
            break
        elif List[idx] != Val:
            idx += 1
        else:
            print False
            break

testIn(1,[0,0])
