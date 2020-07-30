import json #import json
import difflib #this libray is used to compare text


dictionary=json.load(open("data.json"))#load json data into a dictionary

def searchWord():
    word = input("Type word to search...\n").lower()
    return word

def showDefinition(word):

    if word in dictionary:
        # definition=str(dictionary[word]).strip("[]")
        definition = dictionary[word]
        for item in definition:#because definition is a list so we are looping through the list
            print(item)

    elif word =="":
        print("Please insert a word")
        showDefinition(searchWord())
    else:
        close_match=difflib.get_close_matches(word, dictionary.keys())#comparing the given word with all the keys in the dictionary
        #this returns a list of close matches

        if close_match.__len__() > 0:#check if the list is not empty and carry out below operations
            print("Showing definition for "+close_match[0]+" instead of "+ word)
            for item in dictionary[close_match[0]]:
                print("\t"+item)
        else:
            print(word+" not found!")



showDefinition(searchWord())