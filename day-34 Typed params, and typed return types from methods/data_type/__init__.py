age: int
name: str
height: float

age = "Hello" # error from IDE

def ogog(age: int, name: str):
    print(f"age: {age}, name = {name}")

ogog("Helo", 12) # error from IDE but in this point interpreter work

def return_type(age: int, name: str) -> bool: # function with return type
    return "Hello"