
def count_words(string):    
    return len(string.split())
    #print(f"{word_count} words found in the document")
    
    
def make_char_dict(string):
    char_dict = {}
    for char in string:
        low_char = char.lower()
        if low_char in char_dict:
            char_dict[low_char] += 1
        else:
            char_dict[low_char] = 1
    return char_dict
        
    
def character_count(dictionary):
    count_list = []
    for row in dictionary:
        tmp_dict = {}
        
        #setting up dictionary per line in list
        tmp_dict["char"] = row
        tmp_dict["count"] = dictionary[row]
        #adding dict to list
        count_list.append(tmp_dict)
    
    def sortdict(dict):
        return dict["count"]
    
    #sorting list of dicts from most to least char counts
    count_list.sort(reverse=True, key= sortdict)
    
    #creating final output dictionary
    final_dict = {}
    for i in count_list:
        key = i["char"]
        value = i["count"]
        if key.isalpha():  #only passing alphabetical chars
            final_dict[key] = value
    
    return final_dict

