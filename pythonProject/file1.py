import logging
logging.basicConfig(filename="class.log",level=logging.INFO,format='%(asctime)s %(message)s')

class listClass:
    ''' In this class list related functions is available '''
    logging.info("entered into listClass")
    def __init__(self,l):
        self.l=l

    def returnFirstElement(self):
        ''' This function returns the first element of list'''
        logging.info("entered into returnFirstElement function")
        try:
            return self.l[0]
        except Exception as msg:
            print(msg)

    def returnLastElement(self):
        ''' This function returns the last element of list'''
        logging.info("entered into returnLastElement function")
        try:
            return self.l[-1]
        except Exception as msg:
            print(msg)

    def lengthOfList(self):
        ''' This function returns the  length of list'''
        logging.info("entered into lengthOfList function")
        try:
            return len(self.l)
        except Exception as msg:
            print(msg)

    def reverseTheList(self):
        ''' This function returns the reverse  of list'''
        logging.info("entered into reverseTheList function")
        try:
            return self.l[::-1]
        except Exception as msg:
            print(msg)

    def appendOfList(self,value):
        ''' This function returns the after appending  gives the  list eg:l=[1,2,3]
        l.append([3,4]
        o/p:[1,2,3,[3,4]]
        '''
        logging.info("entered into appendOfList function")
        try:
            self.l.append(value)
            return self.l
        except Exception as msg:
            print(msg)

    def ExtendOfList(self,value):
        ''' This function returns the after extending  gives the  list eg:l=[1,2,3]
        l.extend([3,4]
        o/p:[1,2,3,3,4]
        '''
        logging.info("entered into ExtendOfList function")
        try:
            self.l.extend(value)
            return self.l
        except Exception as msg:
            print(msg)

    def indexNumberinAList(self):
        ''' This function returns the index number in of perticular value in  list'''
        logging.info("entered into indexNumberinAList function")
        try:
            return self.l.index(1)
        except Exception as msg:
            print(msg)

    def insertValueAtPerticularindex(self,indexNo,Value):
        ''' This function returns the inserting a value at perticular index  of list'''
        logging.info("entered into insertValueAtPerticularindex function")
        try:
            self.l.insert(indexNo, Value)
            return self.l
        except Exception as msg:
            print(msg)

    def removeTheValueUsingIndex(self,value):
        ''' This function returns the value after removing the value using index from  list'''
        logging.info("entered into removeTheValueUsingIndex function")
        try:
            self.l.pop(value)
            return self.l
        except Exception as msg:
            print(msg)

    def removeThePerticularValue(self,value):
        ''' This function returns the value remove the perticular value from a  list'''
        logging.info("entered into removeThePerticularValue function")
        try:
            self.l.remove(value)
            return self.l
        except Exception as msg:
            print(msg)

class tupleClass:
    ''' In this class tuple related functions is available '''
    logging.info("entered into tupleClass")

    def __init__(self,t):
        self.t=t

    def returnFirstElement(self):
        ''' This function returns the first element of list'''
        logging.info("entered into returnFirstElement function")
        try:
            return self.t[0]
        except Exception as msg:
            print(msg)

    def returnLastElement(self):
        ''' This function returns the last element of list'''
        logging.info("entered into returnLastElement function")
        try:
            return self.t[-1]
        except Exception as msg:
            print(msg)

    def lengthOfList(self):
        ''' This function returns the  length of list'''
        logging.info("entered into lengthOfList function")
        try:
            return len(self.t)
        except Exception as msg:
            print(msg)

    def reverseTheList(self):
        ''' This function returns the reverse  of list'''
        logging.info("entered into reverseTheList function")
        try:
            return self.t[::-1]
        except Exception as msg:
            print(msg)

    def indexNumberinAList(self):
        ''' This function returns the index number in of perticular value in  list'''
        logging.info("entered into indexNumberinAList function")
        try:
            return self.t.index(1)
        except Exception as msg:
            print(msg)

    def countOfPerticularValue(self,value):
        ''' This function returns the count of perticular value in  a list'''
        logging.info("entered into countOfPerticularValue function")
        try:
            return self.t.count(value)
        except Exception as msg:
            print(msg)


class stringClass:
    ''' In this class string related functions is available '''
    logging.info("entered into stringClass")

    def __init__(self,s):
        self.s=s

    def lengthOfString(self):
        ''' This function returns the length of a string'''
        logging.info("entered into lengthOfString function")
        try:
            return len(self.s)
        except Exception as msg:
            print(msg)

    def MultiplyWithNumber(self):
        ''' This function returns the after multiplying with some number returns some result'''
        logging.info("entered into MultiplyWithNumber function")
        try:
            return  self.s*3
        except Exception as msg:
            print(msg)

    def splitString(self):
        '''This function returns the after splitting a string eg:"shashi kumar o/p ['shashi','kumar']'''
        logging.info("entered into splitString function")
        try:
            return self.s.split("i")
        except Exception as msg:
            print(msg)

    def stringUpper(self):
        ''' This function returns the total string in uppercase'''
        logging.info("entered into stringUpper function")
        try:
            return self.s.upper()
        except Exception as msg:
            print(msg)

    def stringLower(self):
        ''' This function returns the total string in lowercase'''
        logging.info("entered into stringLower function")
        try:
            return self.s.lower()
        except Exception as msg:
            print(msg)

    def stringTitle(self):
        ''' This function returns the starting word of a string in upper case'''
        logging.info("entered into stringTitle function")
        try:
            return self.s.title()
        except Exception as msg:
            print(msg)

    def stringCapitalize(self):
        ''' This function returns the uppercase of first letter in a sentence'''
        logging.info("entered into stringCapitalize function")
        try:
            return self.s.capitalize()
        except Exception as msg:
            print(msg)

    def stringSwapcase(self):
        ''' This function returns the uppercase will lowercase and lower case will be uppercase  in a sentence'''
        logging.info("entered into stringSwapcase function")
        try:
            return self.s.swapcase()
        except Exception as msg:
            print(msg)

    def stringisUpper(self):
        '''This function returns boolean value after checking the string is upper or not'''
        logging.info("entered into stringisUpper function")
        try:
            return self.s.isupper()
        except Exception as msg:
            print(msg)

    def stringisLower(self):
        '''This function returns boolean value after checking the string is lower or not'''
        logging.info("entered into stringisLower function")
        try:
            return self.s.islower()
        except Exception as msg:
            print(msg)


class setClass:
    ''' In this class set related functions is available '''
    logging.info("entered into setClass")

    def __init__(self,st):
        self.st=st

    def returnsSet(self):
        '''This function returns the set after type casting'''
        logging.info("entered into returnsSet function")
        try:
            return set(self.st)
        except Exception as msg:
            print(msg)

    def addSet(self,value):
        '''This function returns after adding a value to the set'''
        logging.info("entered into addSet function")
        try:
            self.st.add(value)
            return self.st
        except Exception as msg:
            print(msg)

    def removeSet(self,value):
        '''This function returns after removing a value from  the set'''
        logging.info("entered into removeSet function")
        try:
            self.st.remove(value)
            return self.st
        except Exception as msg:
            print(msg)

    def discardSet(self,value):
        '''This function does not give any error when we give not an element in set'''
        logging.info("entered into discardSet function")
        try:
            self.st.discard(value)
            return self.st
        except Exception as msg:
            print(msg)


class DictClass:
    ''' In this class dict related functions is available '''
    logging.info("entered into DictClass")

    def __init__(self,dt):
        self.dt=dt

    def dictKeys(self):
        '''This function returns the keys from a dictionary'''
        logging.info("entered into dictKeys function")
        try:
            return self.dt.keys()
        except Exception as msg:
            print(msg)

    def dictValues(self):
        '''This function returns the values from a dictionary'''
        logging.info("entered into dictValues function")
        try:
            return self.dt.values()
        except Exception as msg:
            print(msg)

    def dictItems(self):
        '''This function returns the items  from a dictionary'''
        logging.info("entered into dictItems function")
        try:
            return self.dt.items()
        except Exception as msg:
            print(msg)

