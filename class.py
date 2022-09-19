#Lists
list1=["page","view",205,26.05,"studio",2510,"virtual",False]
list2=["android",True,100]
print("1=",list1)
print("2=",list2)

#adding two lists
list3=list1+list2
print("sum=",list3)
print(len(list3))

#indexing
print("\nIndexing")
print("1.",list3[3])
print("2.",list2[-2])
print("3.",list3[-6])

#Slicing
print("\nSlicing")
print("1.",list3[1:5])
print("2.",list1[-4:-1])
print("3.",list2[:2])
print("4.",list3[5:])
print("5.",list3[:-5])

#Step Indexing
print("\nStep Indexing")
print("1.",list3[1:6:2])
print("2.",list3[-7::3])
print("3.",list3[::4])
print("4.",list3[:6:2])
