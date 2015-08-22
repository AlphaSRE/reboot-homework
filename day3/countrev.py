import sys
read_me = '''first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''
def Count(read_me):
    d = {}
    for i in read_me:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    d2 = {}
    for Word,Count in d.items():
        d2[Count] = Word
    
    l1 = d2.keys()
    l1.sort()
    for i in l1[-2:-12:-1]:
        print d2[i],i


def rev(str1):
    l1 = []
    l2 = str1.split(' ')
    for i in l2:
        l1.append(i[::-1])
    print ' '.join(l1)


if __name__  == '__main__':
    if len(sys.argv) != 2:
        print "Usage:python countrev.py count/rev"
        sys.exit(0)
    if sys.argv[1] == 'rev':
        rev(read_me)
        sys.exit(0)
    if sys.argv[1] == 'count':
        Count(read_me)
        sys.exit(0)
