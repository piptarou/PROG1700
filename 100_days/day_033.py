import day_033_functions as d33f


todos = []
print("---To Do List---\n")

while True:
  choice = input("What would you like to do? View / Add / Remove: ").lower()
  match choice:
    case "add":
      d33f.add_item(todos)
    case "remove":
      d33f.remove_item(todos)
      d33f.view_list(todos)
    case "view":
      d33f.view_list(todos)
    case _:
      print("I don't recognize your input.")
