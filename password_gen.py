import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_chosen=[ random.choice(letters)for index in range(random.randint(2,6))]
    numbers_chosen=[ random.choice(numbers)for index in range(random.randint(2,4))]
    symbols_chosen=[ random.choice(symbols)for index in range(random.randint(2,4))]

    password_list = letter_chosen +  numbers_chosen + symbols_chosen
    random.shuffle(password_list)

    password = "".join(password_list)
    return password
    # password_entry.insert(0, password)
    # pyperclip.copy(password)