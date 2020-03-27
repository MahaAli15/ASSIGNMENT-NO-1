#!/usr/bin/env python
# coding: utf-8

# In[1]:


#question 1: perform the following task:
#1. create a class having personal information, hobbies.
#2. create methods that can print these information and hobbies.
#3. create object of your friends and change the parameters accourding to each friend.
class personal_information():
    def __init__(self, first_name, middle_name, last_name, age, birthday, grade, institute, mother_name, father_name,
                 address, phone_number, hobby_one, hobby_two, hobby_three, hobby_four):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age
        self.birthday = birthday
        self.grade = grade
        self.institute = institute
        self.mother_name = mother_name
        self.father_name = father_name
        self.address = address
        self.phone_number = phone_number
        self.hobby_one = hobby_one
        self.hobby_two = hobby_two
        self.hobby_three = hobby_three
        self.hobby_four = hobby_four
p1 = personal_information("syeda", "maha", "ali", "19", "15/5/2000", "13", "usman institute of technology", "samina munawar", 
                         "munawar ali", "a-156 yousuf plaza fb area block 16 karachi,pakistan", "03152324461", "reading",
                         "singing", "vlogging", "cooking")
print(p1.first_name)
print(p1.middle_name)
print(p1.last_name)
print(p1.age)
print(p1.birthday)
print(p1.grade)
print(p1.institute)
print(p1.mother_name)
print(p1.father_name)
print(p1.address)
print(p1.phone_number)
print(p1.hobby_one)
print(p1.hobby_two)
print(p1.hobby_three)
print(p1.hobby_four)
print("!!!!!!!!!!!")
print("my friends")
print("friend 1")
p1 = personal_information("syeda", "beenish", "fatima", "28", "8/2/1992", "graduated", "science and commerce college", 
                          "nishat fatima", "mohammad ali", "a-156 yousuf plaza fb area block 16 karachi, pakistan", 
                          "03353888509", "reading", "drawing", "sketching", "cooking")
print(p1.first_name)
print(p1.middle_name)
print(p1.last_name)
print(p1.age)
print(p1.birthday)
print(p1.grade)
print(p1.institute)
print(p1.mother_name)
print(p1.father_name)
print(p1.address)
print(p1.phone_number)
print(p1.hobby_one)
print(p1.hobby_two)
print(p1.hobby_three)
print(p1.hobby_four)
print("!!!!!!!!!!!!")
print("friend 2")
p1 = personal_information("syeda", "rida", "fatima", "27", "14/2/1993", "graduated", "science and commerce college", 
                          "nishat fatima", "mohammad ali", "a-156 yousuf plaza fb area block karachi, pakistan", 
                          "03302250701", "reading", "writing", "drawing", "sketching")
print(p1.first_name)
print(p1.middle_name)
print(p1.last_name)
print(p1.age)
print(p1.birthday)
print(p1.grade)
print(p1.institute)
print(p1.mother_name)
print(p1.father_name)
print(p1.address)
print(p1.phone_number)
print(p1.hobby_one)
print(p1.hobby_two)
print(p1.hobby_three)
print(p1.hobby_four)
print("!!!!!!!!!!!!")
print("friend 3")
p1 = personal_information("syed", "hassan", "ali", "26", "5/9/1994", "graduated", "science and commerce college",
                         "nishat fatima", "mohammad ali", "a-156 yousuf plaza fb area block 16 karachi, pakistan", 
                         "03243407361", "writing", "drawing", "playing", "watching")
print(p1.first_name)
print(p1.middle_name)
print(p1.last_name)
print(p1.age)
print(p1.birthday)
print(p1.grade)
print(p1.institute)
print(p1.mother_name)
print(p1.father_name)
print(p1.address)
print(p1.phone_number)
print(p1.hobby_one)
print(p1.hobby_two)
print(p1.hobby_three)
print(p1.hobby_four)
print("!!!!!!!!!!!!")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

