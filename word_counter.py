user_input=input("Enter the sentence: ")
word=user_input.strip() #to remove the leading & trailing white spaces
words=word.split() #to split the string from white spaces
count_words=len(words) #to count the number of words
print("Word Count:",count_words) #to print the output