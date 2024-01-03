import day_035_functions as d35f

# #
#     Create a menu where the user can view, add, or remove an item.
#     The user should be able to edit the text of an item on the list too.
#     Don't allow the user to add duplicates.
#     Double check with the user they want to remove an item from the list before it is actually removed. (Is this the item they really want to remove?)
#     Give the user the option to completely erase the to do list. (You should be able to do this in one line of code!)


todos = []
print("---To Do List---\n")

while True:
  choice = input("What would you like to do? View / Add / Edit / Remove / Clear: ").lower()
  match choice:
    case "add":
      d35f.add_item(todos)
    case "remove":
      d35f.remove_item(todos)
      d35f.view_list(todos)
    case "view":
      d35f.view_list(todos)
    case "edit":
      d35f.edit_item(todos)
      d35f.view_list(todos)
    case "clear":
      d35f.clear_list(todos)
    case _:
      print("I don't recognize your input.")
