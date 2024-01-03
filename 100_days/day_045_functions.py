def view_list(list):
  """ Accepts a list and prints it for end user."""
  choice = input("1: View all tasks\n2: View by priority\n ")
  if choice == "1":
    for index,row in enumerate(list):
      print(f"{index+1}: ", row, end = "\n")
  elif choice == "2":
      priority = input("What priority? ").capitalize()
      filtered_tasks = [row for row in list if priority in row]
      for index, row in enumerate(filtered_tasks):
          print(f"{index+1}: ", row, end="\n")
      print()
  else:
    print("Invalid choice")

def add_item(list):
  """ Accepts a list, asks user to input new item, appends new item, and returns list """
  task = input("Task: ").capitalize()
  date = input("Due Date: ")
  priority = input("Priority: ").capitalize()
  row = [task, date, priority]
  list.append(row)
  return list

def edit_item(list):
  """ Accepts a list, asks user what to edit, asks user for new item, 
  replaces old with new, and returns list  """
  view_list(list)
  edit = int(input("What number would you like to edit? "))-1 
  replace = input("What would you like to replace it with? ").capitalize() 
  for index,todo in enumerate(list):
    if index == edit:
      list.remove(todo)
      list.insert(index,replace)
  
def remove_item(list):
  """ Accepts a list, prints it for end user, asks user what item to remove, removes item, and returns list """
  view_list(list)
  change = int(input("What number would you like to remove? "))-1
  for index,todo in enumerate(list):
    if index == change:
        list.remove(todo)
        return list

def clear_list(list):
  """ Accepts a list and clears it """
  list.clear()
  return list

if __name__ == "__main__":
  print("This is a function file, not meant to be run independently.")