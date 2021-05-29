text = input("Enter A sentence: ")


bad_words = [BADWORDSHERE]

for words in bad_words:
  if words in text:
    text_length = len(words)
    hide_word = "*" * text_length
    text = text.replace(words, hide_word)
print(text)
