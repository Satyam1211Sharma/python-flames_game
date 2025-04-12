# 🔥 FLAMES Game in Python

def remove_common_letters(name1_list, name2_list):
    for letter in name1_list[:]:  # iterate on a copy of list
        if letter in name2_list:
            name1_list.remove(letter)
            name2_list.remove(letter)
    return name1_list + name2_list

def flames_game(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    name1_list = list(name1)
    name2_list = list(name2)
    
    remaining_letters = remove_common_letters(name1_list, name2_list)
    count = len(remaining_letters)

    flames = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']

    while len(flames) > 1:
        split = count % len(flames)
        index = split - 1

        if index >= 0:
            flames = flames[index+1:] + flames[:index]
        else:
            flames = flames[:len(flames)-1]

    return flames[0]

# 👇 Input
name1 = input("Enter your name: ")
name2 = input("Enter your partner's name: ")

# 💬 Output
result = flames_game(name1, name2)
print(f"\n🔥 Relationship Status between {name1} and {name2}: {result}")
