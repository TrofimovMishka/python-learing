import files

a = 3
print(a)
# a = input("What the a is: ")
print(a)

# Read and write file:

path = "files/here.txt"
#
# file = open(path) # prepare to read - open tunel to file
#
# print(file.read(5))
# # file.read(5) -> read 5 chars from file
#
# print(file.read())
# file.close() # close tunel to file


with open(path) as file:  # autocloseable read file
    print(file.read())

with open(path, mode="w") as file:  # autocloseable mode="w" means overwrite file
    file.write("GGGGG")

with open(path, mode="a") as file:  # autocloseable mode="a" means append to file
    file.write("\nGGGGG")

with open("new_file.txt", mode="w") as file:  # autocloseable mode="w" means overwrite file,
                                              # if file doesn't exist - file will be created
    file.write("No existing file")