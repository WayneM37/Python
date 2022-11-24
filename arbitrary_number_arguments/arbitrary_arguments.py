# arbitrary numbers slices lists as odd and even elements. 
def slicer(*a):
  even_list= []
  odd_list= []
  for i in a:
    if i %2 == 0:
      even_list.append(i)
    else:
      odd_list.append(i)
  print("even: ",even_list, "odd list: ", odd_list)

slicer(1, 2, 3, 4, 5, 6,)

# arbitrary numbers with list comprehensiyon 
def org(** data):
  nam= [i for i in data.keys()]
  age = [i for i in data.values()]
  print("names: ", nam)
  print("ages: ", age)
org(beth=26, tak=34, tik=45, tok=34,fat=43)

# arbitrary number of arguments **kwargs
def animals(**ahanda):
  for key, value in ahanda.items():
    print(value, "are", key)

animals(carnivores ="lions", omnivores ="bears", herbivores="Deers", nimnivores="human")

#arbitrary number of arguments **kwargs
def organizer(**ahanda):
  names=[]
  ages= []
  for key, values in ahanda.items():
    names.append(key)
    ages.append(values)
  print(names, ages, sep="\n")

organizer (beth=26, tak=34, tik=45, tok=34,fat=43)