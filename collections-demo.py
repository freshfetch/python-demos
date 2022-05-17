# Collection Types
#contain elements of one or more data types
#order, mutability

#Lists: ordered, mutable
import string
from typing import Tuple


fruits = ["apple", "pear", "cherry", "banana",["Guava","cashew","mango"]];
#fruits.insert(2,'blackcurrant');  #insert 
#fruits.extend(["Guava","cashew","mango"]); #add as list
#fruits.append(["Guava","cashew","mango"]); #it would add list as string

#fruits.remove("apple"); #Remove by value, it will remove the first occurence
#fruits.pop(2); #Remove by index

#fruit1 = fruits.pop(2); #assigning to variable
#fruits[3] = "Melon" #Changing list value
#del fruits[3];
#fruits.sort(key=len, reverse=True) #This will update the fruit list with update element
#list2 = sorted(fruits, key=len, reverse=True) #This will provide new list for the sorted element
#list2 = sorted(fruits, key=fruits.count, reverse=True)
#print(fruits.count("apple")) #to count apple in the list
#print(fruits.index("cherry"));
#print(fruits);

#Tuples: ordered, immutable => It works as thesame as list but cant change or update them
#tuple1 = 1,2,3,4,5
#string1 = "Hello World"
#print(string1[0:6])

# Dictionaries: mutable, ordered => it stores Key-Pairs
# store associations as key-value pairs
# cap_cities = {"UK":"London", "France":"Paris", "Italy":"Rome"}
# cap_cities2 = dict(Belgium="Brussel", Germany="Berlin")
# cap_cities["Italy"] = "";
# cap_cities.update(UK="Manchester", France="Lyon")
# cap_cities.pop("UK")
# print(cap_cities.pop("UK"))
# del cap_cities["France"]
# print(list(cap_cities.keys()))
# print(list(cap_cities.values()))
# print(list(cap_cities.items()))
# print(cap_cities.get("UK", "Not found"));
# print(cap_cities["France"]);
# print(cap_cities2)

#Sets: unordered, mutable => set dnt store duplicate or list
# Can only contain immutable elements
# set1 = {1, 2, 3, 5}
# set2 = set()
# set2.add("Hello")
# set2.add("sample text") 
# set2.add("hello")
# set2.remove("hello")  #Use if sure item is there
# set2.discard("hello") #Use if not sure item is there


books = {"Margaret Atwood":"The Handmaiden's Tale","J.R.R. Tolkien":"The Hobbit", "Roald Dahl":"Charlie and the Chocolate Factory"};

author_name = input("Please enter author name: ");
output = books.get(author_name, "not found");
print(author_name + " : " + output);



