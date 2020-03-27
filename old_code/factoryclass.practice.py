from Account import Account 

Main_Account= type("Main_Account",(),{"user_name","email","account_type","balance" : 0,"account_number" : 0})






#-------------------------------------------------------
BaseClass = type("BaseClass",(object,),{})

@classmethod
def Check1(self,myStr):
	return myStr == "ham"

def Check2(self,myStr):
	return myStr == "sanwich"


C1 = type("C1",(BaseClass,),{"x" : 1})

C2 = type("C2",(BaseClass,),{"x" : 30})


def MyFacotry(myStr):
	for cls in BaseClass.__subclasses__():
		if cls.Check(myStr):
			return cls()
	 

m = MyFactory("ham")
v = MyFactory("sandwich")

print m.x,v.x

#------------------------------------------------------



