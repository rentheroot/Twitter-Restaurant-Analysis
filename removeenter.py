with open ('restaurantlist.txt', 'r') as f:
    wordlist = f.read()
    wordlist2 = wordlist.replace('\n', ' ')
    f.close()

with open ('restaurantlist2.txt', 'w') as f:
    f.write(wordlist2)
    f.close
    
    
