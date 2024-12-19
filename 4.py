def reverse_each_word(sentence):
    words = sentence.split() 
    reversed_words = [word[::-1] for word in words]  
    reversed_sentence = ' '.join(reversed_words)  
    return reversed_sentence
sentence = "My Name Is Raju"
reversed_sentence = reverse_each_word(sentence)
print(f"Original Sentence: {sentence}")
print(f"Reversed Words Sentence: {reversed_sentence}")
