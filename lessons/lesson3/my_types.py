from typing import Tuple,List,Dict
from enum import Enum
from datetime import datetime,date,time

#from typing import *
#Tuple #(Vi vet inte var den kommer från)
#import typing
#typing.Tuple

#De vanliga datatyperna finns också



def my_function(a:Tuple[int,str,bool],b:List[int],c:Dict[str,Dict[str,Tuple[int,int]]]):
  print(a,b,c)

my_function((1,"Hello",True),[1,2,3],["Hello",["Hello again",[1,2]]])

def a_new_function(a:int) -> int:
  return a * a


result = a_new_function(5)


print(result)

EmploymentStatus = Enum(
    'EmploymentStatus', ["umemployed", "let_go", "employed", "Retired"])

person:Dict[str,any] = {
  "name":"Anton",
  "Employment_status": EmploymentStatus.let_go,
  "born":date(1992,2,5)}

list_of_employees = [person, person]
print(list_of_employees)

print(list_of_employees[0]["born"])

