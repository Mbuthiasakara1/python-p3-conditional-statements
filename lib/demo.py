# age = 1

# is_baby = 'baby' if age < 2 else 'not  a baby'
# print(is_baby)

# def divide (num1,num2):
#     try:
#         quotient = num1 / num2
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error:num2 cannot be equal to 0")    
#     except TypeError:
#         print("Error: input must be of type int or float")   
#     finally:
#         print("isn't divison fun?")     

# print(divide(0,6))        

course_teacher_mapper = {
    "software engineering" : "Mercy Nazau",
    "data science" : "Antony Muiko",
    "cyber security" : "Francis KIpchumba",
    "devops":"Samuel akadima"
}

course_teacher=course_teacher_mapper.get("data science")
print(course_teacher)

dog = "cuddly"

dict_map = {
    "hungry":"Refiling food bowl",
    "thirsty":"REfilling water bowl",
    "playful" : "PLaying tug-of-war",
    "cuddly" : "snuggling",
}
owner = dict_map.get("thirsty")
print(owner)