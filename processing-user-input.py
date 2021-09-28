def weather_condition(temp): 
    if temp > 7: 
        return "Warm"
    else: 
        return "Cold"

user_input = float(input("Enter temperature:"))
print(weather_condition(user_input))

#pyton 2 or 3

name = input("Enter your name:")
surname = input("Enter your surname:")
message1 = "Hello %s %s" % (name.title(), surname.title())
message2 = f"Hello {name.title()} {surname.title()}!!!" #only work with python 3.6 onwards
print(message1)
print(message2)