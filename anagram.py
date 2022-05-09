def anagramWords(words):
    
    words = list(set(words))
    print(words)
    anagram_words = [''.join(sorted(x)) for x in words]
    print(anagram_words)
    fin_out=[]
    for i in set(anagram_words):
        idx = [x for x,y in enumerate(anagram_words) if y == i]
        
        temp_out = []
        for i in idx:
            temp_out.append(words[i])
        fin_out.append(set(temp_out))
    print(fin_out)
            
anagramWords(['cat', 'dog', 'cat', 'god'])
