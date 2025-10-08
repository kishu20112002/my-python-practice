                   #mutability and immutability object 
      #Immutble

#Immutbale object is one, which will satisfy the following properties.
#. a) The value of Immutable object never allows us to Modify at same address (OR Value of Immutable object can be modified and Modified value can be placed at New
 # Memory Address)
# b) Immutable objects does not support Item Assigment
#. Examples: int, float, complex, bool, str, bytes, range,tuple,set,frozenset


#example :
a=10
print(a,type(a),id(a))
 #output. 10 <class 'int'> 4346309256
a=a+1
print(a,type(a),id(a))
#output.  11 <class 'int'> 4346309288
a=a+1
print(a,type(a),id(a))
#output. 12 <class 'int'> 4346309320
a=1.2
print(a,type(a),id(a))
#output.  1.2 <class 'float'> 434803163
print(a,type(a),id(a))
#output.  2.2 <class 'float'> 4350739600
a=2+3j
print(a,type(a),id(a))
#output.  (2+3j) <class 'complex'> 4355804592




s="python"
print(s,type(a),id(a))
#output. python <class 'complex'> 4355804592
s=s+" prog"
print(s,type(s),id(s))
#output.  python prog <class 'str'> 4355924400




     # Mutable Dbject
  #   =>A Mutbale object is one, Which allows us to Perform the Changes / Modify / Update the values at Same Memory Address
    # Examples:   => bytearray,list,set,dict

#list example

lst=[10,"ROSUM",34.56]
print(lst,type(lst),id(lst))
#output. [10, 'ROSUM', 34.56] <class 'list'> 4315113600
lst.append("kishan")
print(lst,type(lst),id(lst))
#output. [10, 'ROSUM', 34.56, 'kishan'] <class 'list'> 4315113600
lst[0]=100
print(lst,type(lst),id(lst))
#output. [100, 'ROSUM', 34.56, 'kishan'] <class 'list'> 4315113600
lst[0]=1000
print(lst,type(lst),id(lst))
#output. [1000, 'ROSUM', 34.56, 'kishan'] <class 'list'> 4315113600




   #set
s={10,"rossum",34.56}
print(s,type(s),id(s))
#output. {10, 34.56, 'rossum'} <class 'set'> 4311977760
s.add(1000)
print(s,type(s),id(s))
#output.{1000, 10, 34.56, 'rossum'} <class 'set'> 4311977760



