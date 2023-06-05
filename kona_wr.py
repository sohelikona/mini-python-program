def replace_word():
    sentence = "Twinkle Twinkle little star, How I wonder what you are! Up above the world so high. Like a diamond in the sky. I love my country, I love my land. Green Bangladesh. My homeland. I love coding. I love to learn new Technology. I love cats. I love birds. I love my mum. I love me as well."
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word you wanna replace with: ")
    print(sentence.replace(word_to_replace, word_replacement))

replace_word()