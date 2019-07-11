# program for count the words,lines,chracter in text files
#!/usr/bin/python3
num_lines=0
num_words=0
num_chracter=0
with open('text.txt','r') as f:
 for line in f:
   wordlist=line.split()
   num_lines +=1
   num_words +=len(wordlist)
   num_chracter +=len(line)
print("number of lines:")
print(num_lines)
print("number of words:")
print(num_words)
print("number of chracter")
print(num_chracter)
