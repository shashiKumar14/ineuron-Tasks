import file1

l=[1,2,3,45,"shashi"]
# print("om")
l1=file1.listClass(l)
print(l1.returnFirstElement())
print(l1.returnLastElement())
print(l1.lengthOfList())
print(l1.reverseTheList())
print(l1.appendOfList(["kumar"]))
print(l1.ExtendOfList("kumar"))
print(l1.indexNumberinAList())
print(l1.insertValueAtPerticularindex(1,["my name is shashi kumar"]))
print(l1.removeTheValueUsingIndex(1))
print(l1.removeThePerticularValue(1))


l=(1,2,3,45,"shashi")
print("om")
l1=file1.tupleClass(l)
print(l1.returnFirstElement())
print(l1.returnLastElement())
print(l1.lengthOfList())
print(l1.reverseTheList())
print(l1.indexNumberinAList())
print(l1.countOfPerticularValue(1))

s='shashi kumar'
s1=file1.stringClass(s)
print(s1.lengthOfString())
print(s1.MultiplyWithNumber())
print(s1.splitString())
print(s1.stringUpper())
print(s1.stringLower())
print(s1.stringTitle())
print(s1.stringCapitalize())
print(s1.stringSwapcase())
print(s1.stringisUpper())
print(s1.stringisLower())

set1={1,2,3,4,5,6}
se=file1.setClass(set1)
print(se.returnsSet())
print(se.addSet(2))
print(se.removeSet(2))
print(se.discardSet(11))


dict1={"name":"shashi kumar" ,"course":"DataScience" ,"sir":"sudhanshu kumar"}
dc=file1.DictClass(dict1)
print(dc.dictKeys())
print(dc.dictValues())
print(dc.dictItems())
