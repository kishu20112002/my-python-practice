                                #data type 
# int     (immutable)
# float    (immutable)
# bool      (immutable)
# complex   (immutable)
# str     (immutable)
# byte.    (immutable)
# bytearray. (mutable)
# rang      (immutable)
# list   (mutable)
# tuple.  (immutable)
# set 
# frozenset
# dict 
# none type 



            #fundamental cattegory data type.......
# the purpose of fundamental cattegory data type is that "to store sinagle value"
#the python programming we have 4 data type in fundamental cattegory . they are 
    #int
    #float
    #bool
    #complex
    



                         
             #int    ex : 1,2,3,4,5,6,7,8,9
# properties ; int is one of the pre defined class name and treated as fundamental data
       #decimal number system.......

#base:10 digits:0,1,2,3,4,5,6,7,8,9


#binary number system.......
#base:2 digits:0,1
a=0b1101
print(a,type(a))
a=0b1111
print(a,type(a))
a=0b101110
print(a,type(a))


#octal number system.....
#base:8 digits:0,1,2,3,4,5,6,7
a=0o33
print(a,type(a))
a=0o123
print(a,type(a))


#hexa decimal number system.....
#base:16 digits:1,2,3,4,5,6,7,8,9,a(11),b(12),c(13),d(14),e(15)
a=0xac
print(a,type(a))
a=0xbee
print(a)
a=0xface
print(a)
a=0xbee
print(a)





#convertion from binary to octual....
a=0b1010
b=oct(a)
print(b,type(b))

#convertion from hexa decimal to octual....
a=0xf
b=oct(a)
print(b,type(b))

#convertion from decimal to octual.....
a=23
b=oct(a)
print(b,type(b))


#convertion from octual to binary....
a=0o12
b=bin(a)
print(b,type(b))


#convertion from hexa decimal to binary....
a=0xe
b=bin(a)
print(b,type(b))


#convertion from decimal to binary....
a=7
b=bin(a)
print(b,type(b))


#convertion from binary to hexa decimal.....
a=0b10110
b=hex(a)
print(b)


#convert from octual to hexa decimal.....
a=0o17
b=hex(a)
print(b)


#convert from to decimal to hexa decimal....
a=14
b=hex(a)
print(b)





                         #float  ex : 2.3,4.5,67.65

#float is one of the pre defined class name and treated as fundement
#the purpose of float data is that to store real constnt value or float or double pointing (number with decimal places)

a=12.34
print(a,type(a))

a=34.13
print(a,type(a))

            #scientific notation

a=3e2
print(a)
type(a)

a=4e2
print(a,type(a))                







                                             #bool    ex: True,False       
 
a=True
print(a,type(a))
#output True <class 'bool'>

b=False
print(a,type(a))
 #output False <class 'bool'>

 #. a=true 
#output nameerror: name 'true' is not defined. Did you mean: 'True'?
 #  b=false 
#output nameerror: name 'true' is not defined. Did you mean: 'True'?


i=True
j=False
print(a+b)
#1
i=True
j=False
print(a-b)
#1

print(2+True+True+False)
#output 2

print(2+True*3+False)
# output 5

print(0b1010-True+2*True)
#output 11

print(True/True)
#output 1.0                

print(True//True)
#output 1

print(False//True)
#output 0            

print(True//False)
#output zerodivisionerror: integer division or modulo by zero...
 







                #complex.    ex:  2+3j,  4+5j,  4.3+5.6j
#the purpose of complex data type is that "to store complex values / imaginary values".

import cmath
cmath.sqrt(-25)
5j
 
 # a+bj.    or    a-bj
 # here "a" is called as real part
 # here "b" is called as imaginary part 
a=2+3j 
print(a,type(a))
#output(2+3j) <class 'type'> (2+3j)

b=-2-4j
print(b,type(b))
#output (-2-4j) <class 'complex'>

a=1.2+3.4j
print(a,type(a))
#output (1.2+3.4j) <class 'complex'>

b=-2.3-4.5j
print(b,type(b))
#output (-2.3-4.5j) <class 'complex'>

a=12+4.5j
print(a,type(a))
#output (12+4.5j) <class 'complex'>

a=-12+5.4j
print(a,type(a))
#output (-12+5.4j) <class 'complex'>


a=2j
print(a,type(a))
#output 2j <class 'complex'

b=-5j
print(b,type(b))
#output (-0-5j) <class 'complex'>

               # internally real and imgainary parts of complex ocject are treated as float data type 



a=2.3j
print(a,type(a))
#output 2.3j <class 'complex'>

b=-2-6j
print(b,type(b))
#output (-2-6j) <class 'complex'>



               # to extract the real and imginary part of complex object we have 2 pre-defined attributes they are 

a=10+3j
print(a,type(a))
#output (10+3j) <class 'complex'>
print(a.real)
#output  10.0
print(a.imag)
#output  3.0

     


a=2.5+5.2j
print(a,type(a))
# output (2.5+5.2j) <class 'complex'>
print(a.real)
#output  2.5
 
print(a.imag)
#output 5.2

a=-3-5j
print(a,type(a))
#output (-3-5j) <class 'complex'>
print(a.real)
#output -3.0


          

a=-3.5j
print(a.real)
#output -0.0
print(a.imag)
#output -3.5


a=2.5j
print(a,type(a))
#output 2.5j <class 'complex'>
print(a.real)
#output 0.0

a=1+4.5j
print(a,type(a))
#output  (1+4.5j) <class 'complex'>
print(a.real)
#output 1.0










           #sequence cuttegary data type 
# thr purpose of sequence cuttegary data type is "to store in sequenceof values"
 #the pythone programming we have 4 type of swquence cuttgary data
           #i) str
           #ii) byte
           #iii)bytearry
           #iiii)rang





   #string 


#the purpose of str data type is "to stor texual data"
     #string  are tw0 type i) single line string     ex=. "",''
                          #ii) multi line string.  ex=. """",'''


      #single line string data 
s1="python"
print(s1,type(s1))
# output python <class 'str'>


s2='a'
print(s2,type(s2))
#output a <class 'str'>


s3="1"
print(s3,type(s3))
#output 1 <class 'str'>


a="20.78"
print(a,type(a))
#output 20.78 <class 'str'>



a="@#$%^^&"
print(a,type(a))
#output  #$%^^& <class 'str'>



     #operation on str
     #i) indexing
     #ii) slicing

#i) idexing 
#the peocess of obtatng sinagle value from given main str is called indexing 
#example


a="python"
print(a,type(a))
 #output  python <class 'str'>

print(a[0])
 #output p
print(a[-6])
 #output p
print(a[-1])
 #output n
print(a[-5])
 #output y
print(a[-3])
 #output h

s="PYTHON"
print(s,type(s))
  #output  PYTHON <class 'str'>
s[1]
 #output  'Y'
s[2]
 #output  'T'
s[2]
 #output 'T'
s[3]
 #output 'H'
s[4]
 #output 'O'
s[5]
 #output 'N'
s[6]
 #output    indexerror: string index out of range


s[-1]
#output  'N'
s[-2]
#output  'O'
s[-3]
#output  'H'
s[-4]
#output  'T'
s[-5]
#output  'Y'
s[-6]
#output  'P'

s[-7]
#output  indexerror: string index out of range




s="123453456"
print(s,type(s))
 #output 123453456 <class 'str'>
s[2]
 #output '3'
s[-1]
 #output '6'
s[0]
 #output '1'
s[len(s)-1]
 #output '6'


s="JAVA"
print(s,type(s))

#output JAVA <class 'str'>
s[len(s)-1]
#output. 'A'
s[-len(s)]
#output  'J'
s[len(s)-len(s)]
#output. 'J'
s[-2]
#output.   'V'
s[2]
#output.   'V'



    #ii).  silicing
#the purpose of obtaining rang of ualues or sub string from given main str object is called silicing



#syntax1: strobj[BEGIN:END]
                #the syntax genertes rang of value or sub string from BEGIN index to END - 1 index provid BEGIN <END> otherwise we never get any result or space or " as a result


s="PYTHON"
s[0:3]
#output.'PYT'
print(s[0:3])
#output. PYT

                 #+ve
s[2:6]
#output. 'THON'
s[1:6]
#output. 'YTHON'
s[2:1]
#output. ''
s[0:6]
#output. 'PYTHON'
                 #-ve

s="PYTHON"
s[-6:-2]
#output. 'PYTH'
s[-3:-1]
#output. 'HO'
s[-6:-3]
#output. 'PYT'
 
s[-3:-6]
#output. ''
s[-6:-1]
#output. 'PYTHO'

#.   sub rule



s="PYTHON"
print(s,type(s))
#output. PYTHON <class 'str'>
s[1:-2]
#output. 'YTH'
s[2:-1]
#output. 'THO'
s[-3:1]
#output. ''

           #syntax2:  strobj[BEGIN:]
# if we don't specify END index then PVM takes END index len(strobj) or BEGIN index charactor to last

s="PYTHON"
print(s,type(s))
#output. PYTHON <class 'str'>

#+ve

s[2:]
#output. 'THON'
s[0:]
#output. 'PYTHON'
s[3:]
#output. 'HON'
s[5:]
#output. 'N'
s[1:]
#output. 'YTHON'


#-ve

s="PYTHON"
print(s,type(s))
#output. PYTHON <class 'str'>

s[-6:]
#output. 'PYTHON'
s[-5:]
#output. 'YTHON'
s[-4:]
#output. 'THON'
s[-3:]
#output. 'HON'
s[-2:]
#output. 'ON'
s[-1:]
#output. 'N'


               #special points

s="python"
print(s,type(s))
#output. python <class 'str'>

s[-12:]
#output. 'python'

s[-23:]
#output. 'python'

s[23:]
#output. ''

s[2:4]
#output. 'th'

s[12:44]
#output. ''

s[-64:-1]
#output. 'pytho'

s[2:122]
#output. 'thon'

s[2:-122]
#output. ''

s[2:-1]
#output. 'tho'

s[2:22]
#output. 'thon'




          #syntax:   [:END]
#if we don't specify BEGIN index then PVM takes firts character to END -1 index
s="PYTHON"
print(s,type(s))
#output. PYTHON <class 'str'>
         #+ve
s[:3]
#output. 'PYT'
s[:6]
#output. 'PYTHON'
s[:4]
#output. 'PYTH'
s[:5]
#output. 'PYTHO'


         #-ve
s[:-6]
#output. ''
s[:-5]
#output. 'P'
s[:-2]
#output. 'PYTH'
s[:-3]
#output. 'PYT'
s[:-1]
#output. 'PYTHO'


                  #syntax 4: strobj[ : ]
#if we don't specify BEGIN index then PVM takes first character to END -1 index
print(s,type(s))
#output. python <class 'str'>
s[:]
#output. 'python'
s[:]
#output. 'python'
#output. s[0:]
'python'
s[:len(s)]
#output. 'python'
s[-len(s)]
#output. 'p'
s[:-len(s)]
#output. ''
s[-len(s):]
#output. 'python'


           
           #syntax 5: strobj[BEGIN:END:STEP]


 #example rule  2


s="PYTHON"
print(s,type(s))
 #output.  PYTHON <class 'str'>
 
#        +ve
s[0:4]
#output. 'PYTH'
s[0:4:1]
  #output. 'PYTH'
s[2:6:1]
 #output.  'THON'
s[0:6:2]
 #output.  'PTO'
s[0:6:3]
#output.   'PH'
s[0:6:3]
#output.   'PH'
s[ : : ]
#output.   'PYTHON'
s[ : : 2]
#output.   'PTO'
s[ : : 3]
#output.   'PH'

          #-ve


s[ -6:-1 : 2]
#output.  'PTO'
s[ -6: : ]
#output.   'PYTHON'
s[ 6:  ]
#output.   ''
s[ :6 : ]
#output.   'PYTHON'
s[ :-1 : ]
#output.   'PYTHO'


#example. rule 3

s="PYTHON"
s[5:]
#output. 'N'
s[0:6]
#output. 'PYTHON'
s[5:6]
#output. 'N'
s[::-1]
#output. 'NOHTYP'
s[0:6:-1]
#output. ''
s[5:0:-1]
#output. 'NOHTY'
s[::-3]
#output. 'NT'
s[4::-2]
#output. 'OTP'
s[::2][::-1]
#output. 'OTP'
s[::2]
#output. 'PTO'
s[-1:7:-1]
#output. ''
s[-1:-7:-1]
#output. 'NOHTYP'
s[-1:-7:-2]
#output. 'NHY'
s[-1::-1]
#output. 'NOHTYP'
s[-1::-2]
#output. 'NHY'
s[-2::-2]
#output. 'OTP'
s[:-1:]
#output. 'PYTHO'


             #RULE  4
s="PYTHON"
print(s)
  #output.PYTHON
s="JAVA PROG"
s[:0:1]
#output.  ''
s[:0]
#output.  ''
s[:0:3]
  #output.''

              #RULE  5
s="PYTHON"
s[::-1]
#output.'NOHTYP'
s[:-1:]
#output.'PYTHO'
s[:-1:-1]
''
s[:-1:-3]
#output.''
s[:-1:-4]
#output.''
  

          #speical points
"PYTHON"[::1]
#output.'PYTHON'
"PYTHON"[::1]=="PYTHON"
#output.True
"PYTHON"[::2]=="PYTHON"[::1][::2]
#output.False
#output.True 
"MOM"[::1]=="MOM"[::]
#output.True
"LIRIL"[::1]=="lIRIL"[::1]
#output.False




      # ## bytes
           # => Bytes is one of the pre defined class name and treated as sequence data type 
           # => The purpose of bytes data type is that "to organize the numerrical integer values ranges from (0,256) for the implementation of End - End eneryption 
          

x=[]
print(x,type(x))
#output [] <class 'list'>
x={}
print(x,type(x))
#output {} <class 'dict'>
x=()
print(x,type(x))
#output () <class 'tuple'>
x=set()
print(x,type(x))
#output set() <class 'set'>
          
  # =>  bytes data types does not contains any symbolic notation for organzing (0,256) data but we can convert any type of value(s) into bytes type using bytes()
  # syntax => Varname=bytes(object)       

  # example ;-
lst=[10,34,56,100,256,0,102]
print(lst,type(lst))
#output 10, 34, 56, 100, 256, 0, 102] <class 'list'>
b=bytes(lst)
#output ValueError: bytes must be in range(0, 256)

lst=[10,-34,56,100,255,0,102]
print(lst,type(lst))
#output 10, -34, 56, 100, 255, 0, 102] <class 'list'>
b=bytes(lst)
b=bytes(lst)
#output ValueError: bytes must be in range(0, 256)


lst=[10,34,56,100,255,0,102]
print(lst,type(lst))
#output [10, 34, 56, 100, 255, 0, 102] <class 'list'>
b=bytes(lst)
print(b,type(b))
#output  b'\n"8d\xff\x00f' <class 'bytes'>

for val in b:
   print(val)
#output  ...     
10
34
56
100
255
0
102 

print(b[1])
#output 34
print(b[-1])
#output 102
print(b[0:4])
#output b'\n"8d'

for val in b[0:4]:
     print(val)
#output ...     
10
34
56
100
b[0]
#output 10
b[0]=123
#output. typeerror: 'bytes' object does not support item assignment

# => An object of bytes belongs to immutable bcoz bytes object does not support items Assigment 
# => On the object of bytes, we can perform both Indexing and slicing Operations.
# =>  An object of bytes maintains insertion order (which is nothing but ,whatever the order we order we insert the data in the same order data will be displayed  )







     ##.  7 .  bytearray
           # => Bytearray is one of the pre defined class name and treated as sequence data type 
           # => The purpose of bytearray data type is that "to organize the numerrical integer values ranges from (0,256) for the implementation of End - End eneryption 
           # =>  bytearray data types does not contains any symbolic notation for organzing (0,256) data but we can convert any type of value(s) into bytearray type using bytearrya()
          # syntax => Varname=bytearraya(object)   
         # => An object of bytearray belongs to immutable bcoz bytearrya object does not support items Assigment 
        # => On the object of bytearrya , we can perform both Indexing and slicing Operations.
         # =>  An object of bytearrya  maintains insertion order (which is nothing but ,whatever the order we order we insert the data in the same order data will be displayed     
         # --------------
         # Note :- The Functionality of bytes and bytearray are exaclty same but bytes object belongs to immutable bcoz bytes object does not supports item asssigment where bytearray object blongs to Mutable bcoz bytearray object supports items Assigment 

# example :- 

tpl=(10,34,56,199,255,0,102)
print(tpl,type(tpl))
#output.  (10, 34, 56, 199, 255, 0, 102) <class 'tuple'>
b=bytearray(tpl)
print(b)
#output.   bytearray(b'\n"8\xc7\xff\x00f')


tpl=(10,34,56,199,256,0,102)
tpl=[10,34,56,199,255,0,102]
print(tpl,type(tpl))
print(tpl,type(tpl))
#output. (10, 34, 56, 199, 256, 0, 102) <class 'tuple'>'
b=bytearray(tpl)
#output.   valueerror: byte must be in range(0, 256)


tpl=(10,-34,56,199,255,0,102)
print(tpl,type(tpl))
#output.  (10, -34, 56, 199, 255, 0, 102) <class 'tuple'>
b=bytearray(tpl)
#output.   valueerror: byte must be in range(0, 256)



tpl=(10,34,56,199,255,0,102)
(tpl,type(tpl))
#output. (10, 34, 56, 199, 255, 0, 102) <class 'tuple'>
b=bytearray(tpl)
print(b,type(b))
#output. bytearray(b'\n"8\xc7\xff\x00f') <class 'bytearray'>
for val in b :
    print(val)
#output. ...     
10
34
56
199
255
0
102

for val in b[::-1] :
    print(val)
#output. ...     
102
0
255
199
56
34
10





#output. [10, 34, 56, 199, 255, 0, 102] <class 'list'>
b=bytearray(tpl)
print(b)
#output. bytearray(b'\n"8\xc7\xff\x00f')
for val in b:
    print(val)
#output. ...     
10
34
56
199
255
0
102


for val in b[::-1]:
     print(val)
#output. ...     
102
0
255
199
56
34
10


b[0]
#output. 10


for val in b : 
     print(val)
#output.     
10
34
56
199
255
0
102


b[0]=123
for val in b :
     print(val)
#output....     
123
34
56
199
255
0
102




tpl=[10,34,56,199,255,0,102]
print(tpl,type(tpl))
#output. [10, 34, 56, 199, 255, 0, 102] <class 'list'>
b=bytearray(tpl)
print(b,type(b),id(b))
#output. bytearray(b'\n"8\xc7\xff\x00f') <class 'bytearray'> 4357784816.   ###3 here you can see the id last number is 816 after see if we change then what will be happen 

for val in b :
     print(val)
#output. ...     
10
34
56
199
255
0
102






b[0]=102
for val in b :
     print(val)
#output....     
102
34
56
199
255
0
102
print(b,type(b),id(b))
#output.  bytearray(b'f"8\xc7\xff\x00f') <class 'bytearray'> 4357784816  ## here you can see after the changeing the value the address of the tuple is same as before 816 


## coverting into bytearray into bytes

b=bytearray(tpl)
print(b,type(b))
#output. bytearray(b'\n"8\xc7\xff\x00f') <class 'bytearray'>
print(b,type(b),id(b))
#output. bytearray(b'\n"8\xc7\xff\x00f') <class 'bytearray'> 4326766640
for val in b:
    print(val)
#output....     
10
34
56
199
255
0
102

b[0]=123
for val in b:
     print(val)
#output. ...     
123
34
56
199
255
0
102




        ##### converting bytearray into bytes 
c=bytes(b)        
print(c,type(c))
#output. b'{"8\xc7\xff\x00f' <class 'bytes'>
for val in c :
    print(val)
#output. ...     
123
34
56
199
255
0
102




      ####### converting bytes into bytearrya

x=bytearray(c)
print(x,type(x))
#output. bytearray(b'{"8\xc7\xff\x00f') <class 'bytearray'>
for val in x :
    print(val)
#output. ...     
123
34
56
199
255
0
102


print(x,type(x),id(x))
#output. bytearray(b'{"8\xc7\xff\x00f') <class 'bytearray'> 4326767984

x[0]
 #output. 123
x[0]=10
for val in x :
     print(val)
#output. ...     
10
34
56
199
255
0
102

# class 17
                              ########. 8. Range
                              
 # Properties
 #=> 'range' is one of the pre - defined class and treated as sequence data type 


 #Ex Example sheet of range data type 
#Q1) 0 1 2 3 4 5 6 7 8 9 10.  # range of value in forward  direction with interval 1
#Q2) 10 11 12 13 14 15 16 17 18  #range of value in forward  direction with interval 1
#Q3) 100 102 103 104 105 range of value in forward  direction with interval 1

#--  -    -    -    -    -    -    --   -         --   -    -    -    -    -    -    -

#Q4) 10 20 30 40 50 range of value in forward  direction with interval 10
#Q5) 100 110 120 130 140 150  # range of value in forward  direction with interval 10

#     -    --   -    -    -    -    -    -    -    --        -    -

#Q6) 10 9 8 7 6 5 4 3 2  1 #range of value in backrward  direction with interval -1
#Q7) 100 90 80 70 60 50 # range of value in backward  direction with interval -10

#-   -    -    -    -    --   -    -    -    -    -    -    -    -    --   -    -    -    -    

#Q8) -10 -11 -12 -13 -14 -15 #range of value in backward  direction with interval -1
#Q9) -100 -90 -80 -70 -60. # range of value in forward  direction with interval 10

#    -    -    --   -    -    -    -    -    -    -    -    --   --   -    -    -    -    -

#Q10) -5 -4 -3 -2 -1 0 1 2 3 4  5 # range of value in forward  direction with interval 1
#-   --   -    -    -    -    --   -    --   -    -    --   -    -    --        --   


 #=> The purpose of range type is that "to store Equence of numberical interger values with equal interval of value"
 #
 #
 #
 #=> range data type contain 3 syntaxes they are :
 #-  -    -    -    --   --   -    -    -    -    -    -    -
 # syntax 1 ==    varname=range(value)
 # => this synatax genertaes range of values from 0 to value -1
 # => exmaple :
# ex1 
r=range(6)
print(r,type(r))
# output range(0, 6) <class 'range'
for v in r :
     print(v)
# output ...# # it will print for 0 5 only bcz 6-1 so thats why 
0
1
2
3
4
5

#ex2 
for val in range(6):
     print(val)
#output      
0
1
2
3
4
5
 
#ex3
for val in range(11):
     print(val)
# output...       # here you can see that we have insert range 11 but have 10 values
0
1
2
3
4
5
6
7
8
9
10


#ex4
for val in range(11)[::-1]:
    print(val)
#output...   

10  
9
8
7
6
5
4
3
2
1
0
# =  = == =    =    =    =    =    =    =    =    =    =    =    =    =    =    =
# syntax 2 :    varname=range(begin,end)
#=> This syntax genrates range of values from Begin to End -1
# example :

# ex 1
r=range(10,16)
print(r,type(r))
# output range(10, 16) <class 'range'>
for val in r :
     print(val)
...     
10
11
12
13
14
15

#ex2 :
for val in range(10,16):
    print(val)
#output     
10
11
12
13
14
15

#ex3:

for val in range(10,16):
     print(val,end=" ")
# output...     
# 10 11 12 13 14 15 >>> 



# note : the syntax 1 and syntax 2 generates range of value in FORWARD DIRECTION  with default interval 1

#    =    =    =    ==   =    =    =    =    =    ==   =    =    ==   =    ===  =    =    =
# syntax 3 :   varname=range(begin,end,step)
# => This syntax genrates range of values from Begin to End -1 by manintaining Equal ineterval values in the form step either in forward direction or backdirection
# exmaple:
#ex1 
r=range(10,20,2)
print(r,type(r))
# output range(10, 20, 2) <class 'range'>
for val in range(10,20,2):
      print(val)
# output ...     
10
12
14
16
18

#=======  =    =    =    =    =    =    ==   =    ==        ==   =    
# implementation of range
#    =    =    =    =    =    =    =   =    =    =    =    =    =    =    ==   
#Q1) 0 1 2 3 4 5 6 7 8 9 10.  # range of value in forward  direction with interval 1

for val in range(0,11):
     print(val)
#output...     
0
1
2
3
4
5
6
7
8
9
10


#Q2) 10 11 12 13 14 15 16 17 18  #range of value in forward  direction with interval 1

for val in range(10,19):
     print(val)
# output ...     
10
11
12
13
14
15
16
17
18



#Q3) 100 102 103 104 105 range of value in forward  direction with interval 1

for val in range(100,105):
    print(val)
#output ...     
100
101
102
103
104


#--  -    -    -    -    -    -    --   -         --   -    -    -    -    -    -    -

#Q4) 10 20 30 40 50 range of value in forward  direction with interval 10

for val in range(10,51,10):
     print(val)
#output...     
10
20
30
40
50


#Q5) 100 110 120 130 140 150  # range of value in forward  direction with interval 10

for val in range(100,151,10):
     print(val)
#output...     
100
110
120
130
140
150





#     -    --   -    -    -    -    -    -    -    --        -    -

#Q6) 10 9 8 7 6 5 4 3 2  1 #range of value in backrward  direction with interval -1

for val in range(10,0,-1):
     print(val)
#output ...     
10
9
8
7
6
5
4
3
2
1




#Q7) 100 90 80 70 60 50 # range of value in backward  direction with interval -10

for val in range(100,49,-10):
     print(val)
#output...     
100
90
80
70
60
50




#-   -    -    -    -    --   -    -    -    -    -    -    -    -    --   -    -    -    -    

#Q8) -10 -11 -12 -13 -14 -15 #range of value in backward  direction with interval -1

for val in range(-10,-16,-1):
     print(val)
#output...     
-10
-11
-12
-13
-14
-15



#Q9) -100 -90 -80 -70 -60. # range of value in forward  direction with interval 10

for val in range(-100,-59,10):
     print(val)
#output...     
-100
-90
-80
-70
-60




#    -    -    --   -    -    -    -    -    -    -    -    --   --   -    -    -    -    -

#Q10) -5 -4 -3 -2 -1 0 1 2 3 4  5 # range of value in forward  direction with interval 1

for val in range(-5,6,1):
     print(val)
#output ...     
-5
-4
-3
-2
-1
0
1
2
3
4
5

# => An object of range belongs to immutable bcoz range object does not support item assignment 

r[0]=2000
#output  typeerror: 'type' object does not support item assignment

#=>On the object of range we can perform both indexing slicing operations
#=>The range of values can be stord either in forward or backward directions

for val in range(10,21,2)[::-1]:
     print(val)
#output...     
20
18
16
14
12
10


### iii)       list category data type (collection or data structures)



#=> The purpose of list category data types is that" To store mulitiple Values either of same type or different type OR both the type in single object with unique and duplicate values.
#=> In python programming we have 2 data type in list category they are
                    #1. list (mutable)
                    #2. tuple(immutable)
#=   =    =    ==   ==   =    =    ==   =    =    =    =    =    =    =    =         =    ==   =    =    ==   =         ==   =    =    =

###            9..     1.) list
     #index
#properties of list 
#              => types of list 
#                 a) emty list
#                 b) non emty list 
# => operations on list
# => pre - defined functions in list  
# => Nested list /inner list  
# => programming Examples


# class 18
#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#                                  => properties of list 

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

# => list is one of predefined class and treated as list data type
# => the purpose of list  data type is that" to store multiple value at same type or different type or both the types in single object with unique and duplicate values
# => the values/ elements of the list must be stored / organised square brackets and values must be separate by comma
#=> an object of list maintains insertion order.

#=> ex 1
l1=[10,20,30,40,30,40,20,10]
print(l1,type(l1))
#output. [10, 20, 30, 40, 30, 40, 20, 10] <class 'list'>
l1=[10,"kishan",48.36,True,'firoj']
print(l1,type(l1))
#output. [10, 'kishan', 48.36, True, 'firoj'] <class 'list'>

#=> on object of list we can perform both Indexing and slicing operations.

l1[0]
#output 10
l1[-1]
#output 'firoj'
l1[1:4]
#output ['kishan', 48.36, True]
l1[::2]
#output [10, 48.36, 'firoj']
l1[::-1]
#output ['firoj', True, 48.36, 'kishan', 10]


l2=[10,"kishan",48.36,True,'firoj']
print(l2,type(l2),id(l2))
#output [10, 'kishan', 48.36, True, 'firoj'] <class 'list'> 4380990208
l2[0]=20
print(l2,type(l2),id(l2))
#output 20, 'kishan', 48.36, True, 'firoj'] <class 'list'> 4380990208
l2[2:4]=[44,45,False]
print(l2,type(l2),id(l2))
#output [20, 'kishan', 44, 45, False, 'firoj'] <class 'list'> 4380990208

#=> An object of list belongs to mutable
#=> w.r.t list class we can create 2 types of list object they are.
               #a) Empty
               #b) non empty

#a) Empty list
# =>An empty list is one which does not contain any elements and whose length is 0
# => syntax          varname=[]
                         #or  varname=list()

#b) non empty list
#=>An non - empty list is one which  contain  elements and whose length is > 0
# => syntax          varname=[val1,val2,.....valn]
                         #or  varname=list(object)

### converting list data type to bytes
l1=[10,20,30,40]
b=bytes(l1)
print(b)
# output b'\n\x14\x1e('
l=list(b)  ### converting bytes data type to list
print(l)
#output [10, 20, 30, 40]

# converting str to list data type 
s="kishankumargouda"
l=list(s)
print(l)
#output ['k', 'i', 's', 'h', 'a', 'n', 'k', 'u', 'm', 'a', 'r', 'g', 'o', 'u', 'd', 'a']

# coverting int into list data type
i=100
l=list(i)
 #output . TypeError: 'int' object is not iterable
 # to slove the above error use th following 
l=list([i])  
print(i)
#output 100

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

                              #=> pre - defined functions in list  

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
#=> we Know that ,on the objet of list we can perform indexing and slicing operations 
#=> Along with indexing and slicing operations we can perform various operations by using pre defined functions present in list object.They are
#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#                        rough work

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
# 1.append()
# 2.insert()
# 3.remove()
# 4.pop(index)
# 5.pop()
                # del operator.   # del is not a function its a operator 
# 6.index()
# 7.copy()
# 8.count()
# 9.reverse()
# 10.extend()
# 11.sort()
# 12.clear()

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
#                   1.append()
#
#syntax  :   lisobj.append(value)

#=> this function is used for adding the value to list object at end
#=> Example

#ex1 
l1=[10,'kishan',49.45,True,2+3j]
print(l1,type(l1),id(l1))
#output [10, 'kishan', 49.45, True, (2+3j)] <class 'list'> 4392275008
l1.append(12)
print(l1,type(l1),id(l1))
#output [10, 'kishan', 49.45, True, (2+3j), 12] <class 'list'> 4392275008

#ex2
l1=[10,'kishan',49.45,True,2+3j]
print(l1,type(l1),id(l1))
#output [10, 'kishan', 49.45, True, (2+3j)] <class 'list'> 4392358336
l1.append("firoj")
l1.append(False)
print(l1,type(l1),id(l1))
#output [10, 'kishan', 49.45, True, (2+3j), 'firoj', False] <class 'list'> 4392358336


#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#                        2.insert()

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#=> syntax : listobj.insert(index,value)
#=> This function is used for adding the value to list object at specified index
#=> when we enter invaild possitive index then value inserted at last/end of list object 
#=> when we enter invaild negative index then value inserted at first of list object

#=> Examples
#ex1
l1=[10,"rossum",44.56]
print(l1,type(l1),id(l1))
#output [10, 'rossum', 44.56] <class 'list'> 4392369216
l1.insert(2,"python")                                             # insert ex 1
print(l1)
#output [10, 'rossum', 'python', 44.56]
l1[3]=100
print(l1,type(l1),id(l1))
#output [10, 'rossum', 'python', 100] <class 'list'> 4392369216
l1[-1]=1000                                                 # changing the list in the index by -ve index
print(l1,type(l1),id(l1))                                        
#output [10, 'rossum', 'python', 1000] <class 'list'> 4392369216
l1.insert(-1,"firoj")                                           # insert ex 2      
print(l1,type(l1),id(l1))
#output [10, 'rossum', 'python', 'firoj', 1000] <class 'list'> 4392369216

#=>most importane exmaple 

#=> when we enter invaild possitive index then value inserted at last/end of list object 
#=> when we enter invaild negative index then value inserted at first of list object

l1=[10,"rossum",34.54]
print(l1,id(l1))
#output [10, 'rossum', 34.54] 4323714368
l1.insert(10,"python")
print(l1,id(l1))
#output [10, 'rossum', 34.54, 'python'] 4323714368
l1.insert(-10,"python")
print(l1,id(l1))
#output ['python', 10, 'rossum', 34.54, 'python'] 4323714368

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

                     # 12.clear()

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
#=> syntax:         listobj.clear()
#=> This function is used for removeing all the elements of non empty list object 
#=> when we clear() on empty list object than we get No output / none 
#example

l1=[10,"rossum",34.54]
print(l1,id(l1),len(l1))
#output[10, 'rossum', 34.54] 4324091264 3
l1.clear()                              # clear the all index or to a empty list
print(l1,id(l1),len(l1))
#output [] 4324091264 0


#=> most imprtance example 
l1.clear()
print(l1.clear())
#output None

l1.clear()
print(l1)
#output []
 
[].clear()
print([].clear())
#output None

print(list().clear())
#output None

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

                    # 3.remove() based on value

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
#Syntax    listobj.remove(value)
#=> This function is used for removing the first occurence of specified element of list object
#=> if this  specified element does not exits in list then we get value error

#example
#ex1
l1=[10,"rossum",34.45,"python"]
print(l1,id(l1),len(l1))
#output [10, 'rossum', 34.45, 'python'] 4351977920 4
l1.remove("python")
print(l1,id(l1),len(l1))
#output [10, 'rossum', 34.45] 4351977920 3
l1.remove("rossum")
print(l1,id(l1),len(l1))
#output [10, 34.45] 4351977920 2
l1.remove(10)
print(l1,id(l1),len(l1))
#output [34.45] 4351977920 1
l1.remove(34.45)
print(l1,id(l1),len(l1))
#output [] 4351977920 0


list.remove(10)
#output typeerror: descriptor 'remove' for 'list' objects doesn't apply to a 'int' object
list().remove(100)
#output valueerror: list.remove(x): x not in list



#ex2 
l1=[10,20,30,10,30,"python",True]
print(l1,id(l1),len(l1))
#output [10, 20, 30, 10, 30, 'python', True] 4351974976 7
l1.remove(10)
print(l1,id(l1),len(l1))
#output [20, 30, 10, 30, 'python', True] 4351974976 6
l1.remove(10)
print(l1,id(l1),len(l1))
#output [20, 30, 30, 'python', True] 4351974976 5

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#                                    4.pop(index)..... Index based

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
#=> syntax => listobj.pop(index)
#=> This function is used for removing the element of listobj based on index
#=> if the index is invaild then we get indexerror



# example

l1=[10,20,30,20,10,"python",True]
print(l1,type(l1),id(l1),len(l1))
#output [10, 20, 30, 20, 10, 'python', True] <class 'list'> 4341398784 7
l1.pop(2)
#output 30
print(l1,len(l1))
#output [10, 20, 20, 10, 'python', True] 6
l1.pop(-3)
#output 10
print(l1,len(l1))
#output [10, 20, 20, 'python', True] 5
l1.pop(0)
#output 10
print(l1,len(l1))
#output [20, 20, 'python', True] 4
 
l1.pop(0)
#output 20
print(l1,len(l1))
#output [20, 'python', True] 3
l1.pop(0)
#output 20
l1.pop(0)
#output 'python'
l1.pop(0)
#output True


l1.pop(0)
#output indexerror: pop from empty list

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#                             5.pop()

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#=> syntax               listobj.pop()
#=> This function is used for removing always last elementes of listobj
#=> if we call pop() on empty list object then we get indexerror


#example 

l1=[10,20,"Hello",30,20,10,"python",True,]
print(l1,len(l1))
#output [10, 20, 'Hello', 30, 20, 10, 'python', True] 8
l1.pop()
#output True
print(l1,len(l1))
#output [10, 20, 'Hello', 30, 20, 10, 'python'] 7
l1.pop()
#output 'python'
print(l1,len(l1))
#output [10, 20, 'Hello', 30, 20, 10] 6
l1.pop()
#output 10
print(l1,len(l1))
#output [10, 20, 'Hello', 30, 20] 5
l1.pop()
#output 20
l1.pop()
#output 30
l1.pop()
#output 'Hello'
l1.pop()
#output 20
l1.pop()
#output 10

l1.pop()
#output indexerror: pop from empty list

list().pop()
#output indexerror: pop from empty list>>> 

[].pop()
#output indexerror: pop from empty list>>>


#class19

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#              Note : del opertor .......most imp

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#=> syntax 1 : del objlist[Index]  ========> removing element baes on index
#=> syntax 2 : del objname[begin:End:step]        ===========> removing the elements based in slicing operations
#=> syntax 3 : del objname                   =========> removing the entir object

#example : 

l1=[10,"kishan",66.66,"oucet","hyd"]
print(l1,type(l1),len(l1),id(l1))
#output [10, 'kishan', 66.66, 'oucet', 'hyd'] <class 'list'> 5 4388015168
del l1[-2]
print(l1,type(l1),len(l1),id(l1))
#output [10, 'kishan', 66.66, 'hyd'] <class 'list'> 4 4388015168
del l1[0:2]
print(l1,type(l1),len(l1),id(l1))
#output [66.66, 'hyd'] <class 'list'> 2 4388015168
l1=[10,"kishan",66.66,"oucet","hyd"]
del l1[::2]
print(l1,type(l1),len(l1),id(l1))
#output ['kishan', 'oucet'] <class 'list'> 2 4388099264



del l1
print(l1,type(l1),len(l1),id(l1))
#output  nameerror: name 'l1' is not defined



s="python"
print(s)
#output  python
del s
print(a)
#output  nameerror: name 'a' is not defined



#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#                        6.index()

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#=> syntax               listobj.index(Value)
#=> This Function is used for finding index of first occurence of specified element in list object
#=>  if the specified element not present in list object then we get valueerror.

#=> Example 
l1=[10,20,30,40,10,60,70,10,30]
print(l1)
#output  [10, 20, 30, 40, 10, 60, 70, 10, 30]
l1.index(10)
#output  0
l1.index(20)
#output  1
l1.index(30)
#output  2


l1.index(300)
#output valueerror: 300 is not in list


l1.index(-12)
#output valueerror: -12 is not in list


list().index(100)
#output valueerror: 100 is not in list

[].index(-11)
#output valueerror: -11 is not in list



#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#                   7.copy()

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
#          #      # # Copy Techniques in pyhton 
#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
# => in python we have two type of copy techniques . they are 
               #1. shallow copy
               #2. Deep copy 
#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
#=>                  1. Shallow copy 
#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
#=>  The Properties of shallow copy are 
          #a) Initial content of both the object are same 
          #b) The memory address of both the object are different
          #c) The modifications are Independent 
#          (whatever the change we do on one object,will not refiect on other object )
#=> To implement shallow copy we use copy()

#=> synatax : Listobj2=Listobj1.copy()

#=> examples
l1=[10,"rossum",45.45]
print(l1,type(l1),id(l1))                        # Initial content of both the object are same.   #The memory address of both the object are different
#output  [10, 'rossum', 45.45] <class 'list'> 4351255424
l2=l1.copy()                                      # Initial content of both the object are same     # The memory address of both the object are different
print(l2,type(l2),id(l2))
#output  [10, 'rossum', 45.45] <class 'list'> 4351627200
l1.append("python")
print(l1,type(l1),id(l1))                         #  The modifications are Independent
#output  [10, 'rossum', 45.45, 'python'] <class 'list'> 4351255424
l2.append("kishan")
print(l2,type(l2),id(l2))                          #  The modifications are Independent
#output  [10, 'rossum', 45.45, 'kishan'] <class 'list'> 4351627200


#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
#              2. Deep copy 
#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
#=>  The Properties of shallow copy are 
          #a) Initial content of both the object are same 
          #b) The memory address of both the object are same
          #c) The modifications are dependent 
#          (whatever the change we do on one object,will refiect on other object )
#=> To implement Deep Copy we use assigment operator (=)

#=>       syntax    listobject1 = listobject2
#=> exmaple 


l1=[10,"rossum",45.45]
l2=l1
print(l1,id(l1))
#output [10, 'rossum', 45.45] 4351637760
print(l2,id(l1))
#output [10, 'rossum', 45.45] 4351637760


l1.append("python")                                # The memory address of both the object are same 
print(l1,id(l1))
#output [10, 'rossum', 45.45, 'python'] 4351637760
print(l2,id(l1))
#output [10, 'rossum', 45.45, 'python'] 4351637760


l1.remove("rossum")
print(l1,id(l1))
#output [10, 45.45, 'python'] 4351637760
print(l2,id(l1))
#output [10, 45.45, 'python'] 4351637760
#   ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
#8)                 copy()...... shallow copy 
#  ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#=> This function is used for copying the content of one object into another object (implements shallow copy)
#=> synatax :   listobj2=listobj1.copy()
#=> example :

1=[10,"rossum",45.45]
print(l1,type(l1),id(l1))                        # Initial content of both the object are same.   #The memory address of both the object are different
#output  [10, 'rossum', 45.45] <class 'list'> 4351255424
l2=l1.copy()                                      # Initial content of both the object are same     # The memory address of both the object are different
print(l2,type(l2),id(l2))
#output  [10, 'rossum', 45.45] <class 'list'> 4351627200
l1.append("python")
print(l1,type(l1),id(l1))                         #  The modifications are Independent
#output  [10, 'rossum', 45.45, 'python'] <class 'list'> 4351255424
l2.append("kishan")
print(l2,type(l2),id(l2))                          #  The modifications are Independent
#output  [10, 'rossum', 45.45, 'kishan'] <class 'list'> 4351627200
#  ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =
#    deep copy  example
#  ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

l1=[10,"rossum",45.45]
l2=l1
print(l1,id(l1))
#output [10, 'rossum', 45.45] 4351637760
print(l2,id(l1))
#output [10, 'rossum', 45.45] 4351637760


l1.append("python")                                # The memory address of both the object are same 
print(l1,id(l1))
#output [10, 'rossum', 45.45, 'python'] 4351637760
print(l2,id(l1))
#output [10, 'rossum', 45.45, 'python'] 4351637760


l1.remove("rossum")
print(l1,id(l1))
#output [10, 45.45, 'python'] 4351637760
print(l2,id(l1))
#output [10, 45.45, 'python'] 4351637760



#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#                   8.count()
#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#=> syntax   listobj1.count(value)
#=> this function is used for finding / counting number of occurence of specified value of list of list object 
#=> if the specified value does not exist in list object then we get 0 as a result 

#=> exmaple

l1=[10,20,30,10,20,50,60,70,10]
l1.count(10)
#output 3
l1.count(20)
#output 2
l1.count(30)
#output 1
l1.count(40)
#output 0
l1.count(50)
#output 1
l1.count("python")
#output 0


list().count(10)
#output 0
[].count(10)
#output 0


#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#                   9.reverse()

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#=> synatax :     listobj.reverse()

#=> THis function is used for reversing (front elements to back and back elements to front) the elements of list object in the same list
#=>exmaple 

l1=[10,20,30,10,20,50,60,70,10,"python",66.56]
(l1,id(l1))
#output [10, 20, 30, 10, 20, 50, 60, 70, 10, 'python', 66.56] 4387063296
l1.reverse()
print(l1,id(l1))
#output [66.56, 'python', 10, 70, 60, 50, 20, 10, 30, 20, 10] 4387063296


l1=[10,20,30,10,20,50,60,70,10,"python",66.56]
l2=l1.reverse()
print(l1)
#output [66.56, 'python', 10, 70, 60, 50, 20, 10, 30, 20, 10]
print(l2)
#output None


#most importances example baise on mcq

list().reverse()
print(list().reverse())
#output None



#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#                   10.extend()

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#=>syntax               listobj.extend(listobj2)
#=> This Function is used for merging / combining the values of listobj2 with listobj1 . Hence l1stoj1 contains its own elements and elements of listobj2.
#=> syntax          lisiobj1=listobj1+lisobj2+listobjn. 
#=> by using + opertor also we can mergee Or  combine multiple elements of list object

#=> example 

l1=[10,20,30,20]
l2=["rossum","python",66.56]
print(l1,id(l1))
#output [10, 20, 30, 20] 4356859904
print(l2,id(l2))
#output ['rossum', 'python', 66.56] 4356859328

l1.extend(l2)
print(l1,id(l1))
#output [10, 20, 30, 20, 'rossum', 'python', 66.56] 4356859904
print(l2,id(l2))
#output ['rossum', 'python', 66.56] 4356859328


l1=[10,20,30]
l2=["python","java"]
l3=["rossum","gosling"]
l1.extend(l2,l3)                   # to slove the error                                                       # we can not do like this in extend
# #output typeerror: list.extend() takes exactly one argument (2 given)

l1.extend(l2)
print(l1,id(l1))
#output[10, 20, 30, 'python', 'java'] 4356860160
l1.extend(l3)
print(l1,id(l1))
#output [10, 20, 30, 'python', 'java', 'rossum', 'gosling'] 4356860160

#               OR


l1=[10,20,30]
l2=["python","java"]
l3=["rossum","gosling"]                 # using + operator for merging
l1=l1+l2+l3                             ##=> by using + opertor also we can mergee Or  combine multiple elements of list object
print(l1)
# #output  [10, 20, 30, 'python', 'java', 'rossum', 'gosling', 'python', 'java', 'rossum', 'gosling']




#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#              11.sort()

#    ==   =    =    =    =    ==        ==   =    =         =    ==   =    =    ==   =    =    ==   =    =    =

#=> syntax1:      listobj.sort()-------> sorts the given list data in ASCending order
#=> syntax2:      listobj.sort(reverse=False)----------> sorts the given list data in ASCending order
#=> syntax2:      listobj.sort(reverse=True)---------->sort the given list data in DESCending order



l1=[10,-2,30,20,10,4,56,20]                       # here the number are converting to ascending order in sort functions
print(l1,id(l1))
#output [10, -2, 30, 20, 10, 4, 56, 20] 4346685632
l1.sort()
print(l1,id(l1))
#output [-2, 4, 10, 10, 20, 20, 30, 56] 4346685632

#-------------

l1=[10,-2,30,20,10,4,56,20]                            # here you can se the we can converting ascending order with help of sort function and descending order with reverse function
print(l1,id(l1))
#output [10, -2, 30, 20, 10, 4, 56, 20] 4346684864
l1.sort()
print(l1,id(l1))
#output [-2, 4, 10, 10, 20, 20, 30, 56] 4346684864
l1.reverse()
print(l1,id(l1))
#output [56, 30, 20, 20, 10, 10, 4, -2] 4346684864

#---------------
 
l1=[10,-2,30,20,10,4,56,20]                           # here you can se the first only we converting into descending with help of listobj.sort(reverse=True) function we can descending order
print(l1,id(l1))
#output [10, -2, 30, 20, 10, 4, 56, 20] 4346686848
l1.sort(reverse=True)
print(l1,id(l1))
#output [56, 30, 20, 20, 10, 10, 4, -2] 4346686848

#----------------

l1=[10,-2,30,20,10,4,56,20]                             # here you can see sorts the given list data in ASCending order
print(l1,id(l1))
#output [10, -2, 30, 20, 10, 4, 56, 20] 4346677632
l1.sort(reverse=False)
print(l1,id(l1))
#output [-2, 4, 10, 10, 20, 20, 30, 56] 4346677632

#--------------------

l1=["Trump","zali","biden","rossum","alen"]                                # he can see capital letter and smaller letter, priority of ascending order. It always capital letter first in ascending and descending.
(l1,id(l1))
#output ['Trump', 'zali', 'biden', 'rossum', 'alen'] 4346689216
l1.sort(reverse=True)
print(l1,id(l1))
#output ['zali', 'rossum', 'biden', 'alen', 'Trump'] 4346689216

l1.sort()
print(l1,id(l1))
#output ['Trump', 'alen', 'biden', 'rossum', 'zali'] 4346689216

l1.sort()
print(l1,id(l1))
#output ['Trump', 'alen', 'biden', 'rossum', 'zali'] 4346689216

 #-------------------------

l1=["trump","zali","biden","rossum","alen"]                           # here, you can see the small capital letters in ascending and descending.
print(l1,id(l1))
#output ['trump', 'zali', 'biden', 'rossum', 'alen'] 4346690112
l1.sort(reverse=True)
print(l1,id(l1))
#output ['zali', 'trump', 'rossum', 'biden', 'alen'] 4346690112
l1.sort()
print(l1,id(l1))
#output ['alen', 'biden', 'rossum', 'trump', 'zali'] 4346690112

 #-----------------------

l1=[10,"rossum",45.67,"kishan",35,"Firoj"]                                            # here you can see the integer and string cannot be ascending and descending in the list type error
print(l1,id(l1))
#output [10, 'rossum', 45.67, 'kishan', 35, 'Firoj'] 4346680832

l1.sort()
#output typeerror: '<' not supported between instances of 'str' and 'int'

l1.sort(reverse=True)
#output TypeError: '<' not supported between instances of 'int' and 'str'









## class 20
######## 10              Tuple.

# properties

# => Tuple is one of predefined class and treated as list data type
# => the purpose of tuple  data type is that" to store multiple value at same type or different type or both the types in single object with unique and duplicate values
#=> the values/ elements of the list must be stored / organised with braces () and values must be separate by comma
# => an object of tuple, maintains insert order
# => on object of tuple can perform both indexing and slicing operation
# => an object of tuple  belongs to mutable 
#=> w.r.t list class, we can create two type of tuple object they are
#=>                     1) empty tuple
#=>                      2) non empty tuple


#1)emty tuple
               # an empty tuple is one of which does not contain any elements and whose  length 0
                    #=> syntax    varname=()
                    #=>            or  varname=tuple()

#2) non empty typle 
               #=> non empty tuple is one which contain elements, and those length is > 0
               #=> synatax varname=(val1,val2,val-n ) 
               #=>            or varname=tuple(object)





# ====    =    =    =    =    =    =    =    =    ==   =    =    =    =    ==   =    =    =    =    =    ==   =    
#  Note : The Funtionality of tuple is exactly similar to functionality of list but list object belong to mutable and tuble object belong to immutable  
#=   =    =    ==   =    =    =    =    ==   =    =    =         =    =    =    =    =    =    =    =    ==   =    =         ==
#
#Example :
#ex 1
t1=(10,20,30,40,50,60,70)
print(t1,type(t1))
# output (10, 20, 30, 40, 50, 60, 70) <class 'tuple'>
t2=(100,"sagar",33.33,"baglo")
print(t2,type(t2))
#output (100, 'sagar', 33.33, 'baglo') <class 'tuple'>
len(t1)
#output 7
len(t2)
#output 4
t3=100,"Rossum",44.44,"python"
print(t3,type(t3))
#output (100, 'Rossum', 44.44, 'python') <class 'tuple'>
#=   =    =    ==   =    =    =    =    ==   =    =    =    
#Ex 2
t1=()
print(t1,type(t1))
#output () <class 'tuple'>
len(t1)
#output 0
t2=tuple()
print(t2,type(t2))
#output() <class 'tuple'>
#=   =    =    ==   =    =    =    =    ==   =    =    =    

t=(100,"rossum",44.45,"python")
print(t,type(t))
#output (100, 'rossum', 44.45, 'python') <class 'tuple'>
t[0]
# output 100
t[1]
#output 'rossum'
t[-1]
#output 'python'
t[0]=200
#output TypeError: 'tuple' object does not support item assignment

#=   =    =    ==   =    =    =    =    ==   =    =    =    


# converting  list into tuple 

l1=[100,"rossum",44.45,"python"]
t1=tuple(l1)
print(t1,type(t1))
#output (100, 'rossum', 44.45, 'python') <class 'tuple'>

# converting tuple into list 

l2=list(l1)
print(l2,type(l2))
# output [100, 'rossum', 44.45, 'python'] <class 'list'>

#=   =    =    ==   =    =    =    =    ==   =    =    =    

t=(100,"rossum",44.45,"python")
print(t,type(t))
#output(100, 'rossum', 44.45, 'python') <class 'tuple'>
t[0]
#output 100
t[0:3]
#output (100, 'rossum', 44.45)
t[::-1]
#output ('python', 44.45, 'rossum', 100)





# class 21
# =  ==   =    =    =    =    =    ==   ==   =    =         ==        =    ==   =         ==   =    =    ==   
               # set category Data type 
#=== ==        =    =    ==   =    =    =    =    =    =    =    ==   =    =    =    ==        ==   =    =    =    
# set = collection of well defined (unique) Elements 
# consider 
   # A={10,20,30}
   # B={15,10,25}. find AUB. union 

   # AUB={10,20,30} U {15,10,25}
   #C={10,20,30,10,15}
   #D={10,20,30,15,}
   #E={20,30,10,15}

#=> THE purpose of set category data type is that " to store multiple values either of same   type or different type or both the type in sinagle object with unique value (no duplicates are allowed)"
#=> we have 2 data type in set category ther are 
               # set
               # fronset

###   # 9 set
#=> properties 
#=> 'set' is one of the pre defined class and treated as set data type 
#=> the purpose of set data type is that  " to store multiple values either of same   type or different type or both the type in sinagle object with unique value (no duplicates are allowed)"
#=> the elements of set must be stord within curly braces {} and the elements must be separated by comma.

#ex1 
s1={10,20,30,10,20,50,30,40}
print(s1,type(s1))
# output {50, 20, 40, 10, 30} <class 'set'>

#ex2
s1={10,"Travia",44.43,True,"numpy"}
print(s1,type(s1))
#output {True, 'numpy', 'Travia', 10, 44.43} <class 'set'>

#=> an object of set does not maintain insertion order bcoz PVM displays any possiblity of set elements.
#=> 
















