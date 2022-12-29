
text = 'mississippi'


def make_dict(x):
    dict1 = dict()
    for letter in x:
        dict1[letter] = 1 + dict1.get(letter, 0)
    return dict1


def most_frequent(text):
    letters = [letter.lower() for letter in text]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print (count,letter)
    

most_frequent(text)


        
        
      
