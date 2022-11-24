"""
This is simple dictionary. When you enter an English word it returns the Turkish \
    translation. If the entered word is not in our dictionary, it asks to enter\
        the Turkish translation. Dict. data is stored in dict_2.json file. 
     """

import json
dict_1 = {"Blue" : "Mavi", "Apple" : "Elma", "Table" : "Masa"}

with open("dict_2.json", "r+", encoding="utf-8") as origin:   #Bu şekilde localde bulunaun "dict_2.json" filini read yaptırıyoruz. 
    temp = json.loads(origin.read())  # json modulunu kullandık. 
    origin.close()
ans=""
new= ""
while True:
  entry = input("Please enter a word to search in dictionary: ").title()
  if entry.isalpha() == True:
    if entry in temp:
        ans= temp[entry]
        print(entry, ":", ans)
    else:
      print(f"The word {entry} is not in our dictionary.")
      new = input(f"Please entter the Turkish translation of the word {entry} : ").title()
      dict_1.update({entry:new})
      with open("dict_2.json", "w", encoding="utf-8") as origin:  # girdiğimiz kelimeleri dict_2.json a kaydetti. 
        origin.write(json.dumps(dict_1))
        origin.close()
    break
  else:
    print("You made an incorrect entry, please try again!")
