monday_temperature = [9.1, 8.8, 7.6]

for temperature in monday_temperature:
    print(round(temperature))

student_grades = { "Mary": 9.1, "Sim":  8.8, "John": 7.5}

for grades in student_grades.items():
    print(grades) 
#('Mary', 9.1)
# ('Sim', 8.8)
# ('John', 7.5)

for grades in student_grades.values():
    print(grades)
# 9.1
# 8.8
# 7.5

for grades in student_grades.keys():
    print(grades)
# Mary
# Sim
# John

#You can combine a dictionary for loop with string formatting to create text containing information from the dictionary:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

for pair in phone_numbers.items():
    print("%s: %s" % (pair[0], pair[1]))  #older python versions.

for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")    

for value in phone_numbers.values():
    print (value.replace("+","00"))

username = ""
while username != "pypy":
    username = input ("Enter username: ")

while True:
    username = input ("Enter username: ")
    if username == "pypy":
        break
    else:
        continue