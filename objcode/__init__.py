
class Human(object):
    
    def say(self):
        print 'i am human'
        
        
        
class Person(Human):
    
    def say(self):
        print 'i am person'
        super(Person,self).say()
    
    
class Student(Person):
    def say(self):
        print 'i am student'
        super(Human,self).say()


class Worker(Person):
    def say(self):
        print 'i am work'
        super(Student,self).say()
        
        
class Seller(Person):
    pass

# person=Person()
# person.say()

# stu=Student()
# stu.say()

# worker=Worker()
# worker.say()

sell=Seller()
sell.say()