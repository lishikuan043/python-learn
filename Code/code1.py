
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



if __name__ == '__main__':
    print ("hello newcoder")
    #comment
    demo_string()
