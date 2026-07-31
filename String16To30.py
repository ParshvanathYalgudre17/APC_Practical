#Character Frequency
#Display the frequency of every character in a string
string=input("enter a string: ")
checked=""
for ch in string:
    if ch not in checked:
        count=0
        for c in string:
            if ch==c:
                count+=1
        print(ch,":",count)
        checked+=ch


#Anagram Check
#Check whether two strings are anagrams.   
str1=input("enter first string: ")
str2=input("enter second string: ")
s1=sorted(str1.lower())
s2=sorted(str2.lower())
if s1==s2:
    print("strings are anagrams")
else:
    print("strings are not anagrams")



#Remove Duplicate Characters
#Remove duplicate characters while maintaining the original order
string=input("enter a string: ")
result=""
for ch in string:
    if ch not in result:
        result += ch
print("after removing duplicates:",result)



#Substring Search
#Check whether a given substring exists in the main string
mstring=input("enter the main string:")
substring=input("enter the substring:")
if substring in mstring:
    print("Substring found")
else:
    print("Substring not found")


#Count Occurences of Words
#Count how many times a specific word appears in a sentence.   
sentence=input("enter a sentence:")
word=input("enter the word to search:")
words=sentence.split()
count=0
for w in words:
    if w==word:
        count+=1
print("The word",word,"appears",count,"time(s).")



#Password Validator
password=input("enter a password:")
upper=lower=digit=special=0
for ch in password:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
    elif ch.isdigit():
        digit+=1
    else:
        special+=1
if len(password)>=8 and upper>=1 and lower>=1 and digit>=1 and special>=1:
    print("password is valid")
else:
    print("password is invalid")



#Run-Length Encoding 
# Program to compress a string using Run-Length Encoding
string=input("enter a string:")
result=""
count=1
for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        count+=1
    else:
        result = result + string[i] + str(count)
        count=1
print("compressed string:",result)


#String Compression
#Compress repeated characters and return the original string if compression does not reduce the length
string=input("Enter a string:")
compressed=""
count=1
for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        count+=1
    else:
        compressed = compressed + string[i] + str(count)
        count=1
if len(compressed) < len(string):
    print("compressed string:",compressed)
else:
    print("original string:",string)


#Most Frequent Character
#Find the character with the highest frequency     
string = input("enter a string:")
max_char=""
max_count=0
for ch in string:
    count=0
    for c in string:
        if ch==c:
            count+=1
    if count>max_count:
        max_count=count
        max_char=ch
print("character with highest freq:",max_char)
print("frequency:",max_count)



#Second Most Frequent Character
#Find the second most frequently occurring character. 
text=input("Enter a string: ")
freq={}
for ch in text:
    if ch!=" ":
        freq[ch]=freq.get(ch,0)+1
items=sorted(freq.items(),key=lambda x:x[1],reverse=True)
if len(items)>=2:
    print("Second most frequent character:",items[1][0])
else:
    print("No second most frequent character")



#Encrypt and decrypt a message using the Caesar Cipher algorithm. 
text=input("Enter the message:")
shift=int(input("Enter the shift value:"))
e=""
d=""
for ch in text:
    if ch.isalpha():
        if ch.isupper():
            e+=chr((ord(ch)-65+shift)%26+65)
        else:
            e+=chr((ord(ch)-97+shift)%26+97)
    else:
        e+=ch
print("encrypted message:", e)
for ch in e:
    if ch.isalpha():
        if ch.isupper():
            d+=chr((ord(ch)-65-shift)%6+65)
        else:
            d+=chr((ord(ch)-97-shift)%26+97)
    else:
        d+=ch
print("decrypted message:", d)



#Email Validator
#Validate whether a given email address follows a valid format. 
import re
email=input("Enter email: ")
pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
if re.match(pattern,email):
    print("Valid Email")
else:
    print("Invalid Email")


#Word Frequency Dictionary
#Count the frequency of every word in a paragraph.  
text=input("Enter a paragraph: ")
words=text.lower().split()
freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
for word,count in freq.items():
    print(word,":",count)

#Sentence Reversal 
#Reverse the order of words in a sentence without changing the words themselves. 
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_s = ""
for i in range(len(words) - 1, -1, -1):
    reversed_sentence += words[i] + " "
print("Reversed sentence:",reversed_s.strip())


#String Rotation
# Program to check whether one string is a rotation of another
str1=input("Enter first string:")
str2=input("Enter second string:")
if len(str1)==len(str2) and str2 in (str1+str1):
    print("String is a rotation")
else:
    print("String is not a rotation")
