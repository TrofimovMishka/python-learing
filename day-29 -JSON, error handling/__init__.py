# with open("no_existing_file.txt") as file:
#     file.read()  # FileNotFoundError will throw

# How handle:

try:
    # pass  # here exception can ocurres
    file = open("no_existing_file.txt")
# except: # catch ALL errors
except FileNotFoundError as errorMessage:  # catch only FileNotFoundError errors => best practice!! We can use a lot of except block!
    # pass  # do if in try was exceptional situation
    print(f"IN except block - error ocurre:  {errorMessage} ")
    file = open("no_existing_file.txt", "w")  # open if no exist - create it
    file.write("Hello")
else:
    # pass  # do this ONLY if there NO exception
    print("IN else block - error no ocurres")
    content = file.read()
    print(content)
finally:
    # pass  # do this no matter what happen
    print("In finally block")
    file.close()
    raise TypeError("Custom message")

# raise => key word to throw new exception

