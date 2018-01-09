
def demo_string():
    stra = 'HELlo world!'
    print (stra.capitalize())
    stra = stra.replace('world', 'newcoder')
    print(stra)
    strb = ' \n\rhello world \r\n'
    print 1, strb.lstrip()
    print 2, strb.rstrip()
    strc = 'hello w'
    print 3, strc.startswith('hel')
    print 4, strc.endswith('x')
    print 5, stra + strb + strc
    print 6, len(strc)
    print 7, '-'.join(['a', 'b', 'c'])
    print 8, strc.split(" ")
    print 9, strc.find('llo')


def demo_buildfuncion():
    print 1, range(1, 10, 3)
    print 2, chr(65), ord('a')


def demo_control():
    score = 65
    if score > 99:
        print 1, 'A'
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'

    while score < 100:
        print score
        score += 10
    score = 65

if __name__ == '__main__':
    print ("hello newcoder")
    #comment
    demo_string()
    demo_buildfuncion()
    demo_control()