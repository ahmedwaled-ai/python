done_tasks = []
ongoing_tasks = []

tasks = input("Enter your tasks separated by commas:").split(", " )

for task in tasks:
    print(task)

    finished = input(f"Did you finish the {task} already? Yes/No:")

    if finished.capitalize() == "Yes":
        print(f"Great job on finishing the {task}!")
        done_tasks.append(task)
    else:
        print(f"Keep working on the {task}, you can do it")
        ongoing_tasks.append(task)

    print("------")

progress = input("Did you want to see your progress? Yes/No:")

if progress == "no":
        print("please hit enter to exit")    
else:
     print("Done tasks 🎉:")
     print(done_tasks)

     print("Ongoing tasks 🕓:")
     print(ongoing_tasks)
     
   



