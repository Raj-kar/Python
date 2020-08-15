# Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ °C to °F	Divide by 5, then multiply by 9, then add 32
#   °F to °C	Deduct 32, then multiply by 5, then divide by 9 ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius


fahrenheit = lambda cel : (cel/ 5) * 9 + 32
celsius = lambda far : round((far- 32) * 5 / 9)

print(f"60°C is {fahrenheit(60)}° in Fahrenheit")	# 60°C is 140.0° in Fahrenheit
print(f"45°F is {celsius(45)}° in Celsius")			# 45°F is 7° in Celsius

print(f"40°C is {fahrenheit(40)}° in Fahrenheit")	# 40°C is 104.0° in Fahrenheit
print(f"86°F is {celsius(140)}° in Celsius")		# 86°F is 60° in Celsius