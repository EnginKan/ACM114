#to define class in python we need to use keyword class
#let us create a Student class

class Student:
    __s_id=None #stands for student id
    #to change accessabilityo of attribute put (__) char before variable name
    #this makes this variable private to class
    __s_name=None #stands for student Name
    __s_sname=None #student's surname
    #__init__(self):init method define how object from class goiing to be defined
    def __init__(self,s_code,name,surname):
        self.__s_id=s_code
        self.__s_name=name
        self.__s_sname=surname
        
    def __str__(self):
        return "ID:"+self.__s_id+" Name:"+self.__s_name+" Surname:"+self.__s_sname
    
    #Accesors(getters) to get value of data attribute
    def getS_id(self):
        return self.__s_id
    def getSname(self):
        return self.__s_name
    def getSsname(self):
        return self.__s_sname
    #Mutator methods(setters)
    def setS_id(self,new_id):
        self.__s_id=new_id
    def setSname(self,new_name):
        self.__s_name=new_name
    def setSsname(self,new_sname):
        self.__s_sname=new_sname