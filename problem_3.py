"""
3. Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text.
"""
#  "".join(sorted("isTh"))
sample_paragraph = "This is isTh or manish hsinma ro si or snmiah"
word_from_paragraph = sample_paragraph.split(" ")
unique_words = list(set(word_from_paragraph))
for i in range(len(unique_words)):
    anagram_list = []
    # anagram_list.append(unique_words[i])
    word_sort = "".join(sorted(unique_words[i]))
    count = 0
    for j in range(i+1, len(unique_words)):
        next_word_sort = "".join(sorted(unique_words[j]))
        if (word_sort == next_word_sort):
            count = count+1
            anagram_list.append(unique_words[j])
    if count>0:
        anagram_list.append(unique_words[i])
    if(len(anagram_list)>=1):
        print(f"The anagram of word is: {anagram_list}")
