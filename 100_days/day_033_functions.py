def view_list(list):
  for index,todo in enumerate(list):
    print(f"{index+1}: {todo}")

def add_item(list):
  item = input("What would you like to add? ").capitalize() 
  list.append(item)
  
def remove_item(list):
  change = int(input("What number would you like to remove? "))-1
  replace = input("What would you like to replace it with? ").capitalize() 
  for index,todo in enumerate(list):
    if index == change:
      list.remove(todo)
      list.insert(index,replace)
  return list