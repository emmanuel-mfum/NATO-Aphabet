import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")  # read and converts the csv file into a data frame

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}  # loops over every row in the data frame a


def generate_phonetic():
    user_input = input("Enter a word: ").upper()  # makes all the character of a word into capital
    try:
        result = [nato_dict[letter] for letter in user_input]  # makes a list that is made up of the definitions
    except KeyError:
        print("Sorry, only letters of the alphabet please")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
