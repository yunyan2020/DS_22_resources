import requests
from api import Todo


def url(route: str):
    return f"http://127.0.0.1:8000{route}"


print("Hello from todo app")


def print_menu():
    print(
        """
    1: Add Todo
    2: Get Todo
    3: Delete Todo
    4: Update Todo
    5: Exit program
    """
    )
    pass


def add_todo():
    print("Add todo")
    title = input("Todo title: ")
    description = input("Todo description: ")
    new_todo = Todo(title = title,description = description)
  
    res = requests.post(url("/add_todo"),json=new_todo.dict())
    print(res.json())
    pass


def get_todo():
    print("Get todo")
    res = requests.get(url("/todos"))
    if not res.status_code == 200:
        return
    data = res.json()
    for todo in data:
        todo = Todo(**todo)  # Är samma sak som dodo = Todo(title= todo)
        # todo = Todo(id = todo["id"],title = todo["title"],description = todo["description"])
        print("_________________")
        print(f"Id:{todo.id}")
        print(f"Title:{todo.title}")
        print(f"Details:{todo.description}")

def delete_todo():
    print("Delete todo")
    todo_to_delete = input("Id of todo you wish to delete: ")
    if not str.isdigit(todo_to_delete):
        print("Ids are integers")
        return
    res = requests.delete(url(f"/delete_todo/{todo_to_delete}"))
    print(res.json())
    pass


def update_todo():
    print("Update todo")
    res = requests.put(url("/update_todo/1"))
    print(res.json())
    pass


    
 

def main():
    print_menu()
    choice = input("Please choose your action: ")
    choice = choice.strip()
    if not str.isdigit(choice):
        print("Please enter a valid option")
        return

    match int(choice):
        case 1:
            add_todo()
        case 2:
            get_todo()
        case 3:
            delete_todo()
        case 4:
            update_todo()
        case 5:
            exit()
        case _:
            print("Please enter a valid choice")
    pass


while __name__ == "__main__":
    main()

