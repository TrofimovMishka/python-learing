list = ["Bob", 'Gray']
new_list = ["White", 'Yellow']

# print(list[4]) # [IndexError: list index out of range] will produced

nested_list = [list, new_list]

print(nested_list)

print(nested_list[0][0]) # accesslike in Java

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]

print(f"{line1}\n{line2}\n{line3}")

position = 'B1'

map_letters = {'A': 0, 'B': 1, 'C': 2}
map[int(position[1])-1][map_letters.get(position[0])] = 'X'

#solution from ...

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)

print(map_letters.get('A'))


print(f"{line1}\n{line2}\n{line3}")
