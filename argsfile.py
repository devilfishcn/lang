def fun(arg1,arg2='default',*args):
    print 'arg1',arg1
    print 'arg2',arg2
    for eacharg in args:
        print 'tuple arg:',eacharg
fun('python')
fun('python','excellent')
fun('python','excellent','i','love','python',100,'years')  

def fun2(arg1,arg2='default',*args,**kwargs):
    print 'arg1',arg1
    print 'arg2',arg2
    for eacharg in args:
        print 'tuple arg:',eacharg
    for eachkwarg in kwargs.keys():
        print 'dict arg',eachkwarg,':',kwargs[eachkwarg]
fun2('python','excellent','i','love',language='python',mumber=100,time='years')  


def fun3(*args,**kwargs):
    for eacharg in args:
        print 'tuple arg:',eacharg
    for eachkwarg in kwargs.keys():
        print 'dict arg',eachkwarg,':',kwargs[eachkwarg]
fun2('python','excellent','i','love',language='python',mumber=100,time='years')  