with open('/home/share/www_access_20140823.log') as f:
    accessDict = {}
    for oneAccess in f.readlines():
        oneAccessList = oneAccess.split(' ')
        accessDictKey = (oneAccessList[8],oneAccessList[6],oneAccessList[0])
        if accessDictKey in accessDict:
            accessDict[accessDictKey] += 1
        else:
            accessDict[accessDictKey] = 1

for k,v in accessDict.items():
    print [k[0],k[1],(k[2],v)]

