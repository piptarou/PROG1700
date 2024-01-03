import day_045_functions as d45f

todos = []
print("---To Do List---\n")

while True:
  choice = input("What would you like to do? View / Add / Edit / Remove / Clear: ").lower()
  match choice:
    case "add":
      d45f.add_item(todos)
    case "remove":
      d45f.remove_item(todos)
      d45f.view_list(todos)
    case "view":
      d45f.view_list(todos)
    case "edit":
      d45f.edit_item(todos)
      d45f.view_list(todos)
    case "clear":
      d45f.clear_list(todos)
    case _:
      print("I don't recognize your input.")
