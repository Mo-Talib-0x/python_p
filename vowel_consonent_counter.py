string= input("Enter sommething: ")
string= string.lower()
vowels='aeiou'
vowel_count=0
consonent_count=0
letters_count=0
for char in  string:
    if char.isalpha():
        letters_count+=1
        if char in vowels:
            vowel_count+=1
    else:
        consonent_count+=1
print("Total number of letters,",letters_count)
print("The number of vowels is", vowel_count)
print("The number of consonent is",consonent_count)

