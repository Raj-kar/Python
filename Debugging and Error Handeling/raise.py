def colorize(text, color):
    if type(text) is not str:
        raise TypeError("Text must be a string ")
    if type(color) is not str:
        raise TypeError("Color must be a string ")
    if color not in ("red", "yellow", "green", "blue", "white", "black"):
        raise ValueError("Invalid color ")

    print(f"print {text} in {color} color")


# colorize(1, "blue")
    # TypeError: Text must be a string

# colorize("Hello", 2)
    # TypeError: Color must be a string

# colorize("Hello", "purple")
    # ValueError: Invalid color

colorize("Hello Python", "green")
	# print Hello Python in green color
