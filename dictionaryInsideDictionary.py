timeSchedulingProblem
=====================

#supermyDict{key:LocationID(String),Value:myDict(myDictionary)}

#supermyDict{key:TimeStamp(Integer),Value:ListofContent(list)}
myDict = {}


def addTomyDict(Key,Value,loc) :
	if loc in myDict : 
		if Key in myDict[loc] :
			if ((len(myDict[loc][Key]) < 3) and (Value not in myDict[loc][Key])):
				myDict[loc][Key].append(Value)
				return True
			else : 
				return False 
		else :
			myDict[loc][Key] = [Value]
			return True
	else :
		 myDict[loc] = {Key:[Value]}
		 return True





print addTomyDict(6,'C001',1)
print addTomyDict(3,'C002',1)
print addTomyDict(2,'C002',1)
print addTomyDict(5,'C002',1)
print addTomyDict(6,'C003',1)
print addTomyDict(6,'C006',1)
print addTomyDict(6,'C007',1)
print addTomyDict(6,'C008',1)
print addTomyDict(5,'C002',2)
print addTomyDict(6,'C003',2)
print addTomyDict(6,'C006',2)
print addTomyDict(6,'C007',2)
print addTomyDict(6,'C008',2)


print myDictx
