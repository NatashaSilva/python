def mean(value): 
    if isinstance(value, dict):  # same as if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:    
        the_mean = sum(value) / len(value)

    return the_mean

print(mean([1, 4, 5]))

student_grades = { "Mary": 9.1, "Sim":  8.8, "John": 7.5}
print(mean(student_grades))

# || in python is or && in python is and