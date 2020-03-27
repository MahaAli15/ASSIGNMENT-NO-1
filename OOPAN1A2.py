#!/usr/bin/env python
# coding: utf-8

# In[1]:


#question 2: perform the following task:
#1. create a class dinner having dishes inside the dinner class such as soup, salad, course, dessert, juice.
#2. create methods that can print these dishes inside the dinner such as soup, salad, course, dessert, juice.
#3. create objects of your friends and change the parameters accourding to each friend.
class dinner():
    def __init__(self, soup, salad, course, dessert, juice):
        self.soup = soup
        self.salad = salad
        self.course = course
        self.dessert = dessert
        self.juice = juice
p1 = dinner("sour_soup", "vegetable_salad", "pizza", "cake","lemon_juice")
print(p1.soup)
print(p1.salad)
print(p1.course)
print(p1.dessert)
print(p1.juice)
print("!!!!!!")
print("my friends")
print("friend 1")
p1 = dinner("vegetable_soup", "corn_salad", "burger", "brownie", "apple_juice")
print(p1.soup)
print(p1.salad)
print(p1.course)
print(p1.dessert)
print(p1.juice)
print("!!!!!!")
print("friend 2")
p1 = dinner("hot_soup", "mushroom_salad", "bbq", "biscuit", "pineapple_juice")
print(p1.soup)
print(p1.salad)
print(p1.course)
print(p1.dessert)
print(p1.juice)
print("!!!!!!")
print("friend 3")
p1 = dinner("tomato_soup", "olive_salad", "chinese", "custard", "orange_juice")
print(p1.soup)
print(p1.salad)
print(p1.course)
print(p1.dessert)
print(p1.juice)
print("!!!!!!")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

