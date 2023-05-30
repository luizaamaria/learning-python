def greet():
    message = "Hello"
    new_message = message.capitalize()
    print("hey")
    return new_message  # when don't have a return, the definitin of function return the object "none"


greeting = greet()
print(greeting)
