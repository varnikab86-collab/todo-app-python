# Resume Wala To-Do App - Tasks File Me Save Honge

import os
from datetime import date

FILE = "tasks.txt"

# File se tasks load karo
def load_tasks():
    tasks = []
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    # Format: status | task | date
                    parts = line.split(" | ")
                    if len(parts) == 3:
                        tasks.append(parts)
    return tasks

# Tasks ko file me save karo
def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(" | ".join(t) + "\n")

tasks = load_tasks()

while True:
    print("\n--- MERA TO-DO APP ---")
    print("1. Task Add Karo")
    print("2. Task Dekho")
    print("3. Task Complete Karo")
    print("4. Task Delete Karo")
    print("5. Exit")
    choice = input("Apna choice daalo (1-5): ")

    if choice == "1":
        task = input("Task likho: ")
        aaj = str(date.today())
        tasks.append(["Pending", task, aaj])
        save_tasks(tasks)
        print("Task add ho gaya!")

    elif choice == "2":
        if len(tasks) == 0:
            print("Koi task nahi hai!")
        else:
            print("\nTere Tasks:")
            for i, t in enumerate(tasks, 1):
                status, name, d = t
                icon = "✅" if status == "Done" else "⏳"
                print(f"{i}. {icon} {name} - {status} - {d}")

    elif choice == "3":
        num = int(input("Kaunsa number complete karna hai? "))
        if 1 <= num <= len(tasks):
            tasks[num-1][0] = "Done"
            save_tasks(tasks)
            print("Wah! Task complete ho gaya!")
        else:
            print("Galat number hai!")

    elif choice == "4":
        num = int(input("Kaunsa number delete karna hai? "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            save_tasks(tasks)
            print("Task delete ho gaya!")
        else:
            print("Galat number hai!")

    elif choice == "5":
        print("Bye! Tasks save ho gaye hain.")
        break

    else:
        print("Sahi number daalo 1-5 tak!")