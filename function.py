#function  is a block of code it is executed 
#when it is called in python to create fonction def keyword is used
"""syntax: def functionname():
               statements/function body
            function calling()
 """ 
 def suresh():#functiondefinition
     print("goodmorning")
 suresh()
 """note:the value that was passed into fuction defintion is called parameters
 the value that was passed into function caling is called argumrnts"""
 #passing parameters&arguments to a function
 def function (a):
    print("this is value",a)
function(100)#functioncalling
#single parameter function:passing a single or 1 parameter to a function is called single parameter
def function2(c):#parameter
    print(c)
function2(100)
#multiple parameter function:passing a multiple values to a function called as multiple parameters function
def function3(a,b):
    print("the value:",a+b)
function3(4,5)#arguments
"""task:
1.perform a float division operation using functionname it is multiple
2.write a program to wish a person using the python functions
"""
#1.
def fuction4(c,d):
    print("the value",c+d)
function4(1.0,5.5)
#2.
def mohana():
    print("hello")
mohana()
#arbitary argument():arbitary argument is an argument which is denoted by (*)which takes multiple argument for a single parameter
#returns  the result in the form of tuple
def function(a):
    print(a)
function(10,15,20)
#parameter error of positional argument
def function(*a):
    print(a)
function(10,15,20)
#key args():keyword args is a function which takes single parameter for mutiple argument in the form of key value pairs so that the
#  output is dictionary format
def function2(**name):
    print("hi",name)
function2(name="mohana",place="nadipudi")
#nested function:A function is called nested function
def outerfunction(): 
    print("outerfunction statement")
    def innerfunction():
        print("innerfunction statement")
    innerfunction()
outerfunction()