import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
npq_dic = {row["letter"]: row["code"] for (index, row) in nato_phonetic_alphabet.iterrows()}
while True:
    try:
        text = input("Enter a word: ").upper()
        corresponding_words = [npq_dic[letter] for letter in text]
    except KeyError:
        print("Just letters and a single word, please.")
    else:
        print(corresponding_words)
