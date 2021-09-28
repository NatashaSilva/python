day_hours = 24
week_days = 7
week_hours = day_hours * week_days

print (week_hours)

# You can create a list of numbers automatically using a range. For example:
# list(range(1, 10))
# rage(start, end, step) or rage(start, end) or rage(end) *end not included!

#dir(str) -> gives you all strings methods. You can do this for any object type
# help(str.upper) -> explain what this method can do.

#to check the built in function you can use: dir(__builtins__)

monday_temperature = [9.1, 8.8, 7.5] # list type
# monday_temperature = [9.1, 8.8, 7.5] # tuple type -> it is immutable 
student_grades = { "Mary": 9.1, "Sim":  8.8, "John": 7.5} #dictionary type Mary is key, 9.1 is value

mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum / length

print(mean)


students_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(students_grades.count(10.0))
students_grades[1:4] # [ 8.8, 10.0, 7.7] slice method that creates a new list/ You can also do that with strings!!
students_grades[:4] # [ 9.1, 8.8, 10.0, 7.7]
students_grades[3:] # [ 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
students_grades[-5] # 8.0
students_grades[-5:] # [ 8.0, 10.0, 8.1, 10.0, 9.9]
students_grades[-4:-2] # [10.0, 8.1]

username = "Python3"
print(username.lower())

# data = [["name", "John"], ["surname", "smith"]]
# dict(data)
# {'name': 'John', 'surname': 'smith'}