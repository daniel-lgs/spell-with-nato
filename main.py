import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
npq_dic = {row["letter"]: row["code"] for (index, row) in nato_phonetic_alphabet.iterrows()}
text = input("Enter a word: ").upper()
corresponding_words = [npq_dic[letter] for letter in text]
print(corresponding_words)
