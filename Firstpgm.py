"""Question Set 1
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
1. Try to reverse a list
2. Try to access 234 out of this list
3. Try to access 456
4. Try to extract only a list collection from list l
5. Try to extract "sudh"
6. Try to list all the key in dict element available in list
7. Try to extract all the value element from dict available in list
Question Set 2
l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":"kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]
1. Try to extract all the list entity 
2. Try to extract all the dict entities
3. Try to extract all the tuples entities
4. Try to extract all the numerical data it may b a part of dict key and values 
5. Try to give summation of all the numeric data 
6. Try to filter out all the odd values out all numeric data which is a part of a list 
7. Try to extract "ineuron" out of this data
8. Try to find out a number of occurrences of all the data 
9. Try to find out number of keys in dict element
10. Try to filter out all the string data 
11. Try to Find  out alphanum in data
12. Try to find out multiplication of all numeric value in  the individual collection inside dataset 
13. Try to unwrap all the collection inside collection and create a flat list """
import logging
logging.basicConfig(filename='test.log',level=logging.INFO,format='%(levelname)s %(asctime)s  %(name)s  %(message)s')
def inp(): # Function to get input from user
    while True:
        try:
            i = eval(input("Enter the Input :  "))
            print("The input obtained is :  ", i)
            return i
            break
        except Exception as e:
            print("Not a valid input")
            logging.error(e)
            continue
class List1: #Class created for list related functions
    def rev_list(self): #Function to reverse a given list
        self.inpu = i
        while True:
            try:
                logging.info("Processing the Input")
                if type(i) == list:
                    print("The Reversed List :  ", i[::-1])
                    logging.info("Output generated")
                    break
                else:
                    print("Wrong Input ! Not a List ! Try again !")
                    continue
            except Exception as e:
                print("Please try again! Not a List Input ")
                logging.error(e)
                continue
    def access_element(self): #Function to access any element within a list
        self.inpu = i
        a = eval(input("Enter value to be accessed:"))
        z=0
        try:
            logging.info("Analyzing the Input !")
            for b in i:
                if b == a:
                    print("The value is present at index :", i.index(b))
                    logging.info("Output generated")
                    z = 1
                elif type(b) == tuple or type(b) == list or type(b) == set:
                    for c in b:
                        if c == a:
                            print("The value is present at index :", i.index(b))
                            logging.info("Output generated")
                            z = 1
                elif type(b) == dict:
                    for d, e in b.items():
                        if (d == a) or (e == a):
                            print("The value is present at index :", i.index(b))
                            logging.info("Output generated")
                            z = 1
                        elif type(d) == list or type(d) == set or type(d) == tuple:
                            for f in d:
                                if f == a:
                                    print("The value is present at index :", i.index(b))
                                    logging.info("Output generated")
                                    z = 1
                        elif type(e) == list or type(e) == set or type(e) == tuple:
                            for g in e:
                                if g == a:
                                    print("The value is present at index :", i.index(b))
                                    logging.info("Output generated")
                                    z = 1
            if z == 0:
                print("Value is not found")
        except Exception as e:
            print("Please try again! Not a List Input ")
            logging.error(e)
    def access_listcollection(self):#Function to access list collections within a list
        self.inpu = i
        logging.info("Trying to gather the list collections from input list !")
        try:
            i1 = []
            for s in i:
                if type(s) == list:
                    i1.append(s)
            print("The list collections from the input list are : ", i1)
            logging.info("Output Generated")
        except Exception as e :
            print("Not a valid input")
            logging.error(e)
    def access_dictcollection(self): #Function to access Dict collections (items,keys and values) within a list
        self.inpu = i
        logging.info("Trying to gather the dict collections from input list !")
        try:
            i2 = []
            i3 = []
            i4 = []
            for s in i:
                if type(s) == dict:
                    i2.append(s.keys())
                    i3.append(s.values())
                    i4.append(s.items())
            print("The dictionary items in the given list :", i4)
            print("The keys of dict from the input list : ", i2)
            print("Count of keys in dict from input list : ",len(i2))
            print("The values of dict from the input list : ", i3)
            print("Count of values in dict from input list : ",len(i3))
        except Exception as e :
            print("Not a valid input")
            logging.error(e)
    def access_tuplecollection(self):  # Function to access tuple collections within a list
        self.inpu = i
        logging.info("Trying to gather the tuple collections from input list !")
        try:
            i5 = []
            for s in i:
                if type(s) == tuple:
                    i5.append(s)
            print("The tuple collections from the input list are : ", i5)
            logging.info("Output Generated")
        except Exception as e:
            print("Not a valid input")
            logging.error(e)
    def access_numericaldata(self):  # Function to access numerical elements within a list with sum,product,odd and even numbers
        self.inpu = i
        logging.info("Trying to gather the numerical elements from input list !")
        try:
            i6 = []
            i7 = []
            i8 = []
            for b in i:
                if type(b) == int:
                    i6.append(b)
                elif type(b) == tuple or type(b) == list or type(b) == set:
                    for c in b:
                        if type(c) == int:
                            i6.append(c)
                elif type(b) == dict:
                    for d, e in b.items():
                        if (type(d) == int) or (type(e) == int):
                            i6.append(d)
                            i6.append(e)
                        elif type(d) == list or type(d) == set or type(d) == tuple:
                            for f in d:
                                if type(f) == int:
                                    i6.append(f)
                        elif type(e) == list or type(e) == set or type(e) == tuple:
                            for g in e:
                                if type(g) == int:
                                    i6.append(g)
            print("The Numerical Values in the list : ", i6)
            print("Summation of all numerical values in List : ", sum(i6))
            for s in i6:
                if (s % 2) == 0:
                    i7.append(s)
                else:
                    i8.append(s)
            p = 1
            for s in i6:
                p = p * s
            print("Product of all numerical values in the given list : ", p)
            print("Even Values in the given list : ", i7)
            print("Odd Values in the given list : ", i8)
            logging.info("Output Generated")
        except Exception as e:
            print("Not a valid input")
            logging.error(e)
    def ele_occurence(self):  # Function to find the occurrence of each element within a list
        self.inpu = i
        logging.info("Trying to gather the occurrence of each element from input list !")
        try:
            i9 = []
            for m in i:
                if type(m) == list:
                    for j in m:
                        i9.append(j)
                if type(m) == dict:
                    for a, b in m.items():
                        i9.append(a)
                        i9.append(b)
                if type(m) == tuple:
                    for k in m:
                        i9.append(k)
                if type(m) == set:
                    for r in m:
                        i9.append(r)
            print("element" + " " * 4, "occurence")
            for m in set(i9):
                print(m, "----------", i9.count(m))
            logging.info("Output Generated")
        except Exception as e:
            print("Not a valid input")
            logging.error(e)
    def st_alphnum(self):  # Function to find the string and alphanum elements within a list
        self.inpu = i
        logging.info("Trying to gather the string elements from input list !")
        try:
            ls = []
            lan = []
            for l in i:
                if type(l) == list:
                    for j in l:
                        if type(j) == str:
                            ls.append(j)
                if type(l) == dict:
                    for a, b in l.items():
                        if type(a) == str or type(b) == str:
                            ls.append(a)
                            ls.append(b)
                if type(l) == tuple:
                    for j in l:
                        if type(j) == str:
                            ls.append(j)
                if type(l) == set:
                    for j in l:
                        if type(j) == str:
                            ls.append(j)
            print("The string elements within the given list : ", ls)
            for j in ls:
                if (j.isalnum() == True):
                    lan.append(j)
            print("The alpha numeric elements within the given list : ", lan)
            logging.info("Output Generated")
        except Exception as e:
            print("Not a valid input")
            logging.error(e)
    def flat_list(self):  # Function to create flat list from the given list
        self.inpu = i
        logging.info("Trying to gather the all the elements from input list !")
        try:
            l1 = []
            for o in i:
                if type(o) == list:
                    for j in o:
                        l1.append(j)
                if type(o) == dict:
                    for a, b in o.items():
                        l1.append(a)
                        l1.append(b)
                if type(o) == tuple:
                    for k in o:
                        l1.append(k)
                if type(o) == set:
                    for r in o:
                        l1.append(r)
            print("The flat list generated from given list :",l1)
            logging.info("Output Generated")
        except Exception as e:
            print("Not a valid input")
            logging.error(e)
    def ind_prod(self):  # Function to get the product of numerical values in individual collection from the given list
        self.inpu = i
        logging.info("Trying to gather the individual collections from input list !")
        try:
            for l in i:
                m = 1
                if type(l) == list or type(l) == tuple or type(l) == set:
                    for j in l:
                        if type(j) == int:
                            m = m * j
                    print(type(l), m)
                if type(l) == dict:
                    for k in l.items():
                        for n in k:
                            if type(n) == int:
                                m = m * n
                    print(type(l), m)
            logging.info("Output Generated")
        except Exception as e:
            print("Not a valid input")
            logging.error(e)
i=inp()
l = List1().rev_list()
n=List1().access_element()
o=List1().access_listcollection()
p=List1().access_dictcollection()
q=List1().access_tuplecollection()
h=List1().access_numericaldata()
j=List1().ele_occurence()
x=List1().st_alphnum()
y=List1().flat_list()
w=List1().ind_prod()

