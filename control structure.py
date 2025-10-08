# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =     
#   class 34        
#                            Flow control statements in python
#                                          OR
#                           Control Structrues in python

#=  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =
# Index
#-------
#=> Purpose of flow control stetements in python
#=> Type of flow control statements in python 

#       1) Conditional OR Selection OR Branching Statement
#               a) Simple if statements
#               b) if....else statements
#               c) if....elif....else statment
#               d) match.....case
#             => Programming Example

#       2) Looping OR iterative OR Repetative Statements
#               a) while loop OR   while...else loop
#               b) for loop     OR  for....else loop
#            => Programming Example
#
#       3) Transfer Flow control statements
#               a) break
#               b) continue
#               c) pass
#               d) return
#             => Programming Example
#              => combined programming example on conditional looping and transfer flow control stetements
#=  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =

#=> Nested OR Inner loops 
#                           a) while loop in while loop 
#                           b) for loop in for loop
#                            c) while loop in for loop
#                            d) for loop in while loop
#                                            => Programming Example













# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =     
#           
#                            Flow control statements in python
#                                          OR
#                                Control Structrues in python

#=  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =

#=> The purpose of flow control statements in python is that "to perform certain opertaion X of opertain Y opertain ") onlyonce (depends on cond True of False ) OR cond True or False ) OR to perform certain operation Repeatedly for finite number of time until condition becomes false." 
#=> Python programming we have 3 type of flow control statements they are 

#=>                             1) Conditional OR Selection OR Branching Statement              
#                               2) Looping OR iterative OR Repetative Statements
#                               3) Transfer Flow control statements

# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =     

#=>                             1) Conditional OR Selection OR Branching Statement              
#=> The purpose of Conditional OR Selection OR Branching Statement   is that "to perform certain opertaion X of opertain in the case of True of perform  Y opertain in case of False only once ") 
#=> In python programming we have 4 type of Conditional satements . they are 

#                                   a) Simple if statements
#                                   b) if....else statements
#                                   c) if....elif....else statment
#                                   d) match.....case
#                                          => Programming Example

# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    
#               a) Simple if statements
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    
# 
# syntax :   if ( Test cond ) :             # : means Indentation symbol
#                  (statement 1)              
#                  (statement 2)            # indentation block of stmts
#                   ...........               
#                  (statement n)
#  
#           other statements in program 
# 
#      Explanation:
#                       => hence if a keyword
#                       => hence Test cond can be either True or False 
#                       => if the test cond is False 



# Examples
#ex1: movie ticket
tkt=input("Do you have ticket (yes/no)::")
if tkt=="yes" :
    print("enter to the show ")
    print("enjoy the moments of the movie ")
    print("enjoy by pop")
print("goto home and bye ticket next time ")


#ex2: program for deciding wether the number is even or odd
#Evenodd if 
num=int(input("enter the a number"))
if num%2==0:
    print("even no")
#  print("Odd no")
if num%2!=0:
    print("odd no")
print("program executed is completed")

#ex3: # program for deciding weather the give number is +ve -ve 0
n=int(input("enter the no: "))
if n>0:
    print("it is a positive number")
if n<0:
    print("it is a negative number")
if n==0:
    print("it is a zero number")
print("program executed is completed")

#ex4: #wap to check its palindrome or not in simple if statement
str=input("enter a word or a number")
if str==str[::-1]:
    print("it is a palindrome")
if str!=str[::-1]:
    print("it is not a palindrome")


# class 35
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    
#                 b) if....else statements
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    






#Examples
#ex1 #program for acccepting whether a given number of +ve or -ve zero#
#IfElseEx1
num=int(input("enter a number:"))
if num<0:
    print("negative number",num)
else:
    print("positive number",num)



n=int(input("enter a number"))
if n>0:
    print("positive number",n)
else:
    if n<0:
        print("negative number",n)
    else:
        print("zero number",n)


#ex2 wap to check its a vowel word or not
#ifelse
word=input("enter the word:")
if ('a'in word.lower() or 'e' in word.lower() or 'i' in word.lower() or 'o'in word.lower() or 'u' in word.lower() ):
    print("it is a vowel word")
else:
    print("it is not a vowel word")


#ex 3#wap for accepting any digits and print its name
n=int(input("enter the number:"))
if n==0:
    print("zero",n)
else:
    if(n==1):
        print("one",n)
    else:
        if(n==2):
            print("two",n)
        else:
            if(n==3):
                print("three",n)
            else:
                if(n==4):
                    print("four",n)
                else:
                    if(n==5):
                        print("five",n)
                    else:
                        if(n==6):
                            print("six",n)
                        else:
                            if(n==7):
                                print("seven",n)
                            else:
                                if(n==8):
                                    print("eight",n)
                                else:
                                    if(n==9):
                                        print("nine",n)
                                    else:
                                        print("its a number",n)
print("program execution end")


# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    
#                c) if....elif....else statment
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    
#
#
#
#Examples:

#ex1 : wap for accepting any digits and print its name
#n=int(input("enter a number"))
if n==0:
    print("zero",n)
elif n==1:
    print("one",n)
elif n==2:
    print("two",n)
elif n==3:
    print("three",n)
elif n==4:
    print("four",n)
elif n==5:
    print("four",n)
elif n==6:
    print("five",n)
elif n==7:
    print("five",n)
elif n==8:
    print("six",n)
elif n==9:
    print("six",n)
elif n in [-1,-2,-3,-4,-5,-6]:

    print("negative no'")
else:
    print("its a number ")
print("excution end")


#ex2: # program for deciding weather the give number is +ve -ve 0
num=int(input("enter a number"))
if num<=0:
    print("invalid input")
else:
    if num%2==0:
        print("even no ")
    else:
        print("odd no ")


#class 36
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    
#               d) match.....case
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    















# class 37
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =   
#  
#           2) Looping OR iterative OR Repetative Statements
#
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    

#=> The purpose of looping OR iterative OR Repetative statements " to perform certain.operation repeatedly for finite number of times untile condition becomes False."
#
#   ex         An sms to 100 people 
#               i=1  #initization
#              while  i<=100 :   # test cond
#               print("send sms to i")
#               i=i+1. #updation part
#
# ex 1 program to printe 1 to 10 number in while loop
#i=1
while i<11:
     print(i)
     i=i+1
     
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


i=1
while i<=10:
     print(i)
     i=i+1
     
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


#=> At the time of dealing with looping statements programmer must ensure 3. point they are 
#                           1) inilization part (from where to start)
#                           2) condtional part (where to stop)
 #       3) updatetion part ( Increment or Decrement )


#ex 2   write a program to in 10 to 1 
i=10
while i>0:
     print(i)
     i=i-1
     
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

#=> In python we have two type of looping statements they are.

#                       a) while loop   OR   while...else loop
#                       b) for loop     OR  for....else loop
#
#
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    
#           a) while loop   OR   while...else loop
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    
#
#   syntax-1
#
#
#
#
#       while(Test cond):
#               statements-1
#               statements-2
#               ------------
#               statements-n
#-   -   -   --  -   -   --  -   --  -
#   Other statements in prog
#-   -   -   --  -   -   --  -   --  -
#--    -   -   --  -   -   --  -   --  -
#
#
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    
#                       OR
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    
#
#   while(Test cond):
#               statements-1
#               statements-2
#               ------------
#               statements-n
#   else
#           ------------------------
#           else block of statements
#           ------------------------
#
# Explantion  note in 23:25
#
# Ex1. #program for generating 1 to n number where n is +ve number
num=int(input("enter how many numbers you want to generate"))
i=1
while i<=num:
    print(i)
    i=i+1
#enter how many numbers you want to generate: 10
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


#Ex1 level 1
num=int(input("enter how many numbers you want to generate: "))
if num<=0:
    print("invalid input")
else:
    i=1                 #initization
    while i<=num:       # test cond
        print(i)        #updation 
        i=i+1
print("program is done ")

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

#Ex 1 level 3
#num=int(input("enter number"))
if num<=0:
    print("invaild input")
else:
    i=1
    while i<=num:
        print(i)
        i=i+1
    else:
        print("i am from else part of while loop")
    print("program end")
   

#enter number: 10
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
# i am from else part of while loop
#program end



#ex 2 #program for generating mul table for given +ve number
n=int(input("enter a number"))
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i=i+1

#enter a number5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

#.  ex2 level 2
##program for generating mul table for given +ve number
n=int(input("enter number"))
if n<=0:
    print("invalid input")
else:
    i=1
    while i<=10:
        print(n,"x",i,"=",n*i)
        i=i+1



#
#
###.  ex2 level 4
n=int(input("enter number for generator mul table: "))
if n<=0:
    print("invalid input".format(n))
else:
    print("_"*50)
    print("mul table for : {}".format(n))
    print("_"*50)
    i=1
    while i<=10:
        print("\t{} x {}={}".format(n,i,n*i) )
        i+=1
    else:
        print("*"*50)



#ex3  level 1 program for finding sum of first numbers
n=int(input("enter a number"))
if n<=0:
    print("invalid input")
else:
    s=0
    i=1
    while i<=n:
        print(i)
        s=s+i
        i=i+1
    else:
        print("="*50)
        print("sum",s)

#enter a number10
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
#==================================================
#sum 55
#==================================================
#


#ex 3 level 2 
n=int(input("enter a number"))
if n<=0:
    print("invalid input")
else:
    print("="*50)
    print("{} sum natural numbers".format(n))
    print("="*50)
    s=0
    i=1
    while i<=n:
        print(i)
        s=s+i
        i=i+1
    else:
        print("="*50)
        print("{} sum ".format(s))


#ex4 program of squres of natural number 
n=int(input("enter a number"))
if n<=0:
    print("invalid input")
else:
    print("="*50)
    i=1

    while i<=n:
        print(i,i*i)

        i+=1
    else:
        print("="*50)
#enter a number5
#==================================================
# 1 1
# 2 4
# 3 9
# 4 16
# 5 25
#==================================================

#ex5 # program for finding sum of squres of first natuaral numbers
n=int(input("enter a number"))
if n<=0:
    print("invalid input")
else:
    i=1
    s=0
    while i<=n:
        print(i,i*i)
        s=s+i**2
        i+=1

    else:
        print("sum",s)
       

#enter a number : 5

# 1 1
# 2 4
# 3 9
# 4 16
# 5 25

# sum 55                 


#Ex 5 level 2 
n=int(input("enter a number"))
if n<=0:
    print("{} is invalid input".format(n))
else:
    print("{} is first natural number".format(n))
    print("*"*50)
    i=1
    s=0
    while i<=n:
        print("\t{}\t{}".format(i,i**2))
        s=s+i**2
        i+=1
    else:
        print("*"*50)
        print("squares sum",s)
        print("*"*50)




#Ex 5 # program for finding sum of squres and sum first natural numbers

n=int(input("enter a number"))
if n<=0:
    print("invalid input")
else:
    i=1
    s=0
    ss=0
    while i<=n:
        print(i,i*i)
        s=s+i
        ss=ss+i**2
        i=i+1
    else:
        print("*"*50)
        print("sum",s,ss)
        print("*"*50)


#  enter a number5
# 1 1
# 2 4
# 3 9
# 4 16
# 5 25
# **************************************************
# sum 15 55
# **************************************************


#ex 5 level 2
n=int(input("enter a number"))
if n<=0:
    print("invalid input")
else:
    print("*"*50)
    print("\tNatnul\tsquares")
    print("*"*50)
    i=1
    s=0
    ss=0
    while i<=n:
        print(i,i*i)
        s=s+i
        ss=ss+i**2
        i=i+1
    else:
        print("*"*50)
        print("\t{}\t{}".format(s,ss))
        print("*"*50)

#enter a number5
#**************************************************
#	Natnul	squares
#*************************************************
# 1 1
# 2 4
# 3 9
# 4 16
# 5 25
#**************************************************
#	15	55
#**************************************************



#ex6 write a program print squre and its total and cupe and its total
n=int(input("enter a number"))
if n<=0:
    print("invaild input")
else:
    i=1
    c=0
    s=0
    ss=0
    cs=0
    while i<=n:
        print("\t{}\t{}\t{}".format(i,i**2,i**3,))
        s=s+i
        c=c+i
        ss=ss+i**2
        cs=cs+i**3
        i+=1
    else:
        print("*"*50)
        print("sum",s,ss,cs)

        print("*"*50)

#        enter a number5
#	1	1	1
#	2	4	8
#	3	9	27
#	4	16	64
#	5	25	125
#**************************************************
#sum 15 55 225
# **************************************************
#



##Ex 7  program for finding product first natural number


#n=int(input("Enter the number of products: "))
if n<=0:
    print("invaild number")
else:
    i=1
    p=1
    while i<=n:
        print(i)
        p=p*i
        i+=1
    else:
        print("*"*50)
        print("product number is",p)



#Ex 8 my code  line of words to find its len of words
line=input("enter a line of text")
print("Given{}",format(line))
print("*"*50)
words=line.split()
print(words)
i=0
while i<len(words):
    print(words[i],len(words[i]))
    i+=1
else:
    print("*"*50)

# enter a line of text: kishan firoj pika raja
# Given{} kishan firoj pika raja
# **************************************************
# given words :  ['kishan', 'firoj', 'pika', 'raja']
# kishan 6
# firoj 5
# pika 4
# raja 4
# **************************************************
#
#ex 9
s=input("enter any word of charter")
l=len(s)
i=0
while i<=l:
    print(s[i],i)
    i=i+1  






# class 38
# enter any word of charterkishan
# k 0
# i 1
# s 2
# h 3
# a 4
# n 5



## =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =    
#             b) for loop     OR  for....else loop
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =   

# 
s="python" #s is called interble object
for k in s:
    print(k) 

#p
#y
#t
#h
#o
#n



#  for varname in iterable object 
# =  =   =   =   ==  ==  =   ==  =   ==  ==  =   =   ==  =   ==  =   =   ==  =       === =   =   =   =   ==      =   
#.  statement1
#.  statement2
#   statement n
#
#
#syntax 1:  
#               for varname in iterable object
#                   indentation block of stmts
#                   other elements in program
#synatx 2:                 
#                              
#              for varname in iterable object  
#                   indentation block of stmts
#              else:
#                   else block of stmts
#              other statments in python 
#



#Explantation 
#=> here 'for' 'in' and 'else' are keywords
#=> here interable object can be sequence (bytes,bytes,rang,str)
# list(list,tuple),set(set,frozenset)and dict
#=> the execution processs of loop is that "each of element of iterable_object selected , placed in varname and executes indentation block of stmts ". THis process will be repeated until all elements of iterable_object completed 
#=> when all the elements of iterable object completed then PVM comes out of for loop and executes else block  of stmts which are written under else block 
#=> writing else block is optional


#Ex 1 program for enerting mul table for a given +ve no
n=int(input("enter a number to how much you habe to gen"))
if n<=0:
    print("\t{} invaild input".format(n))
else:
    print("*",50)
    print("\t{} given number".format(n))
    print("*", 50)
    for i in range(0,11):
        print("\t{} x {} ={}".format(n,i,n*i))

#enter a number to how much you habe to gen4
#**************************************************
#	4 given number
#*************************************************
#	4 x 0 =0
#	4 x 1 =4
#	4 x 2 =8
#	4 x 3 =12
#	4 x 4 =16
#	4 x 5 =20
#	4 x 6 =24
#	4 x 7 =28
#	4 x 8 =32
#	4 x 9 =36
#	4 x 10 =40



#Ex 2 print squres and cube in for loop

s=0
c=0
for i in range(1,6):
    print(i,i**2,i**3)
    s=s+i**2
    c=c+i**3
    print(sum,s,c)

#  1 1
# <built-in function sum> 1 1
# 2 4 8
# <built-in function sum> 5 9
# 3 9 27
# <built-in function sum> 14 36
# 4 16 64
# <built-in function sum> 30 100
# 5 25 125
# <built-in function sum> 55 225


#logic in vd 25.40 you can see it 

#Ex 3 cal a the sum of fatorial
n=int(input("enter a number for cal factorical : "))
if n<0:
    print("invalid input")
else:
    f=1
    i=n
    while i>0:
        f=f*i
        i=i-1
    else:
        print("factorical ({}) = {}".format(n,f))


# 5!=120

# ex3 but in different wave by using while loop
n=int(input("enter a number for cal factorial:"))
if n<0:
    print("invaild input")
else:
    f=1
    i=1
    while i<=n:
        f=f*i
        i=i+1
    else:
        print("factorial is ({})={}".format(n,f))


# ex3 same example but in diffent wave by using for loop 

n=int(input("enter no for cal factorial."))
if n<0:
    print("invaild input")
else:
    f=1
    for i in range(1,n+1):
        f=f*i
    else:
        print("\t{}!={}".format(n,f))

#ex 4 wap to generate how much numbers of even number you have to generate 

n=int(input("enter a how much no you have input"))
if n<=0:
    print("invaild input")
else:
    for i in range(2,n+1)[::2]:
        print("even no",i)

# even no 2
# even no 4
# even no 6
# even no 8
# even no 10





# ex 5  find the factors of a given number n where n is +ve no
n=int(input("enter the number "))
if n<=0:
    print("invaild input ")
else:
    for i in range(1,n+1):
        if n%i==0:
            print(i)

#enter the number 12
1
2
3
4
6
12
           
#ex same 

n=int(input("enter the number "))
if n<=0:
    print("invaild input ")
else:
    for i in range(1,(n//2)+1):
        if n%i==0:
            print(i)


#enter the number 12
1
2
3
4
6


# Ex5 which will find the sum of digits of the given number

n=int(input("enter the number"))
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
else:
    print("sum of the digits is",s)


#    enter the number123
#    sum of the digits is 6




# ex same q but diffent output 

n=int(input("enter the number"))
s=0
while n>0:
    s=s+n%10
    n=n//10
    print("the sum of the digits is",s)


# enter the number123
# the sum of the digits is 3
# the sum of the digits is 5
# the sum of the digits is 6



#.= =   =   =   ==  ==  ==  === ==  =   ==  ==  =   ==  =   =   === =   =   =       ==  =   ==  =   =   =

#.                      Transfer flow control statements 

#=  ==  =   =   =   =   =   =   =   =   =   =   ==  =       =   ==  =       ==      =   ==  =   =       ==  ==  
#
#=> The purpose of transfer flow control statements in python is that " to change the control of PVM from one part of the prgram another part of program."
#=> In python programming we have 4 types of transfer flow control statements. they are
#                               =>1.break
#                               =>2.continue
#                               =>3.pass
#                               =>4.retun
#
#.= =   =   =   ==  ==  ==  === ==  =   ==  ==  =   ==  =   =   === =   =   =       ==  =   ==  =   =   =
#
#.= =   =   =   ==  ==  ==  === ==  =   ==  ==  =   ==  =   =   === =   =   =       ==  =   ==  =   =   =
#
#                   =>1. break

#.= =   =   =   ==  ==  ==  === ==  =   ==  ==  =   ==  =   =   === =   =   =       ==  =   ==  =   =   =
#
#=>break is a key word
#=>The purpose of break statement is that "To terminate the execution of loop logically when certain condition is satisfied and PVM control comes of corresponding loop and executes other statements in the program".
#=>when break statement takes place inside for loop or while loop then PVM will not execute corresponding else block(bcoz loop is not becming False) but it executes other statements in the program
#
#=>Syntax1: 
#                      for varname in Iterable_object:
#                   --------------  -   -   -   -   -   -   --
#                           if(test cond):      
#                               break
#                       --- --      --- --  --  -
#                           -   -   -   -   -   -   --  -
#
#=>Syntax2:  

#                           while(test cond -1)
#                           --      -   -   -   -   -   
#                               if (test cond -2)
#                                   break
#                           -   --  -   -   -   -   -    
#                           -   -   -   -   -   --      -   
#
# ex 1 using in for loop
##prgram for dennostrating break staements
# breakex1.py

s="PYTHON"
#display all the letter of s part 1
for ch in s:
    print(ch)
else:
    print(" i am from else of for loop")
print("*"*50)



#want to display PVT without using slicing and indexing part 2

for ch in s:
    if ch=="H":
        break
    else:
        print(ch)
else:
    print("i am from else of for loop")
print("*"*50)


# P
# Y
# T
# H
# O
# N
# i am from else of for loop
#**************************************************
# P
# Y
# T
#**************************************************
#
#
#ex2 using while loop
#
##prgram for dennostrating break staements
# breakex1.py
s="PYTHON"
# display all the letter of s part 1
i=0
while i<len(s):
    print(s[i])
    i+=1
else:
    print("i am from the else part")
print("program execution part")
print("*"*50)

i=0
while i<len(s):
    if s[i]=="H":
        break
    else:
        print(s[i])
        i+=1
else:
    print("i am from the else part 2")
print("prgram execution  complete")

# P
# Y
# T
# H
# O
# N
# i am from else of for loop
#**************************************************
# P
# Y
# T
#**************************************************
#


# ex3 check it is prime no or not 

#n=int(input("enter the number :"))
if n<0:
    print("invaild input")
else:
    res="PRIME"
    for i in range(2,n):
        if n%i==0:
            res="NOT PRIME"
            break
    if res=="PRIME":
        print("{} is {}".format(n,res))
    else:
        print("{} is NOT PRIME".format(n))

#

#    enter the number :5
#   5 is PRIME
#
#   enter the number :9
#   9  is NOT PRIME
#
#
#
#
#
#**************************************************
#
#
#
##.= =   =   =   ==  ==  ==  === ==  =   ==  ==  =   ==  =   =   === =   =   =       ==  =   ==  =   =   =
#
#                   =>2.continue

#.= =   =   =   ==  ==  ==  === ==  =   ==  ==  =   ==  =   =   === =   =   =       ==  =   ==  =   =   =
#
#
#
#
#   Ex1.  using for loop
s="PYTHON"
#display all the letter of s part 1
for ch in s:
    print("\t{}".format(ch))
else:
    print("i am from the of the loop")
print("prgram execution  completed")
print("*"*50)

#want to display pyhon

for ch in s:
    if ch=="T":
        continue
    else:
        print("\t{}".format(ch))


#  P
#	Y
#	T
#	H
#	O
#	N
#i am from the of the loop
#prgram execution  completed
#**************************************************#
#	P
#	Y
#	H
#	O
#	N
#



# ex 2 same q but using while loop

s="PYTHON"
# display all the letter of s part 1
i=0
while i<len(s):
    print("\t{}".format(s[i]))
    i+=1
else:
    print("i am from else of while part")
print("program exercise compled ")
print("*"*50)

#want to display pyhon
i=0
while i<len(s):
    if s[i]=="T":
        i=i+1
        continue

    else:
        print("\t{}".format(s[i]))
        i=i+1

else:
    print("i am from else of while part 2")
print("program exercise completed ")


#	P
#	T
#	H
#	O
#	N
#i am from else of while part
#program exercise compled 
#**************************************************
#	P
#	Y
#	H
#	O
#	N
# i am from else of while part 2
#program exercise completed 




#   ex3 same q but this time two conditions

# continue ex 3
s="PYTHON"
# want to display PTON

i=0
while i<len(s):
    if s[i]=="Y" or s[i]=="H":
        i=i+1
        continue
    else:
        print("\t{}".format(s[i]))
        i=i+1
else:
    print(" i am from the else of while loop")
print("program completed")

#	P
#	T
#	O
#	N
# i am from the else of while loop
#program completed


#   ex 4

##Programme for demonstrating continuous statement
# continue example.py
s="PYTHON"
i=0
while i<len(s):
    if s[i] in ["T","O","N"]:
        i=i+1
        continue
    else:
        print(s[i])
        i=i+1

# P
# Y
# H

# Ex 5 list have given you have to print only the +ve no 

lis=[12,-12,34,-34,65,84,-2,-4]
print("given number:{} ".format(lis))
print('*'*50)
print("list of +ve values")
print("*"*50)
i=0
for val in lis:
    if val<=0:
        continue
    print("{}".format(val))
print("*"*50)

#   given number:[12, -12, 34, -34, 65, 84, -2, -4] 
#   *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#   list of +ve values
#   *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#   12
#   34
#   65
#   84
#   *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#   
#   ex 6 print -ve no from the list 

lis=[12,-12,34,-34,65,84,-2,-4]
print("given number:{} ".format(lis))
print('*'*50)
print("list of -ve values")
print("*"*50)
i=0
for val in lis:
    if val>=0:
        continue
    print("{}".format(val))
print("*"*50)



#**************************************************
-12
-34
-2
-4
#**************************************************
#
#
# ex 8 write a python program accpect the list of values from the keyboard
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#






#           class 40
#


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#




#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#