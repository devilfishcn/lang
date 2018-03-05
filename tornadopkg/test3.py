def h():
    print 'Wen Chuan',
    m = yield 5  # Fighting!
    print m
    d = yield 12
    print 'We are together!'

c = h()
c.next() 
