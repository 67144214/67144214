letters = ["A" , "B" , "C" , "D"]
a = letters[0]
d = letters[3]

letters[0] = d
letters[3] = a

print(letters)


numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.remove(5)
numbers.insert(0, -1)

print(numbers)


fruits = ["มะนาว", "มะม่วง", "ลำไย", "ส้ม", "แก้วมังกร"]
fruits.insert(3, "มะเขือเทศ")
fruits.insert(0, "Shinchan")
fruits[2] = "Ultraman"
a = fruits[2]
b = fruits[4]
fruits[2] = b
fruits[4] = a

print(fruits)