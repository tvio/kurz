
#TEST
x = input("napis neco")
print("Hello " +x)
print(f"bla bla {x} blah blah")

#lze modifikovat + poradi
list = ["karel","tomas","anicka"]
#nelze modifikovat + poradi
touple  = ("karel","tomas","anicka")
#muze mit duplicity  + neresi poradi
set = {"karel","karel", "bob"}
set2 = {"karel","anicka"}
diff = set.difference(set2)
add = set.union(set2)
intersec = set.intersection(set2)


print (list[0]+ touple[0])
#list.remove("unique")
#list.append("unique")
set.add("karel")


friends = ["a","b","c"]
for friend in friends:
    print(f"{friend} jop")

dictionary = {"rold":24,"tomas":50}
dictionary["rold"] = 50
print(dictionary["rold"])
d = {"rold":24,"tomas":50}

for jmeno,vek in d.items():
    print(f"kdo {jmeno}: vek {vek}")

#list of dictionaries
lod = [{"jmeno":"karel","vek":24}, {"jmeno":"pajos","vek":44}]
print(lod[0]["vek"])

# dict of tuples
osoby = [("uklizec", 25, "karel"),("hajzlbaba", 66, "anicka"),("potapec", 44, "tonda")]  
for povolani,vek,jmeno in osoby:
    print (f"jmeno {jmeno},vek {vek},povolani {povolani}")

#lambda fce
add = lambda x,y:x+y
print (add(5,7))
#nebo
print((lambda x,y:x+y)(5,7))
#nebo lze pak pouzit map
#argumenty libovolneho mnozstvi
#*args - nepojmenovane parametry
#keywork arguments **kwargs
#*nums rozlozi tuple do parametru  da se dat jako argument do vice parametru funkce
#myfunc(*tuple)
# pass dictonary **nums do parametru
#myfunc(**dict)

def both(*args,**kwargs):
    print(args)
    print(kwargs)
both(1,3,5,name="bob,age=25")
#def post(url,data=None,json=None,**kwargs):
#    return request ('post',url,data=data,json=json,**kwargs)

class Student:
    types = ("splhnoun","trouba")
    def __init__(self,age,types):
        self.name = "Rolf"
        self.age= age
        self.types=types
        
    #premeni objekt na string
    def __str__(self):
        return f"person {self.name},{self.age},{self.types}"
    # __repr__ dela podobne ale pouziva to napriklad debugger. Muzu tim vypsat cely objekt
    def __repr__(self):
        return f"{self.name},{self.age}." 
    # vola se pro praci s atributy tridy - types
  
    @classmethod
    def class_method(cls):
        print(f"called class method{cls}")
    #Factories  -  pripravuje objekt, ktery pouziva class parametry
    @classmethod
    def Student2(cls,age):
        return Student(age, Student.types[0])
    #obycejna funkce uvnitr tridy bez navaznosti na instance
    @staticmethod
    def static_method():
        print("called static")   
student = Student("19",'ttrouba')        
print(student.name,student.age)
print(student)
Student.class_method()
Student.static_method()
karel = Student.Student2(19)
print(karel)
#dedeni
#class Nova(Puvodni)
#   def __init__( self a vsechny puvodni atributy + nove)
#       super().__init__( seznam atributu ) -- vycet atributu ktere chci inicializovat z puvodni tridy abych nemusel prirazovat self.pvuodni = puvodni
        #self.novej1 = novej1
        #self.novej2 = novej2
    #def __str__ (self):
    #return f"{super().__str__()} ({self.novej1, self.novej2}"