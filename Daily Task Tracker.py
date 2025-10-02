# Ask user to enter tasks
tasks = input("Enter your tasks for today separated by a comma: ").split(", ")
done_tasks = []
ongoing_tasks = []

# Check each task
for work in tasks:
    print(f"\nTask: {work}")
    print("-------")
    completed = input(f"Did you finish '{work}' already? (yes / no) ").lower()
    
    if completed == "yes":
        print("Nice job!")
        done_tasks.append(work)
    else:
        print("Keep working on it!")
        ongoing_tasks.append(work)

# Optionally, show today's progress
progress = input("\nDo you want to see your today's progress? (yes / no) ").lower()
if progress == "yes":
    print("\n****** Done Tasks *****")
    for task in done_tasks:
        print(f"- {task}")
    
    print("\n******* Ongoing Tasks ********")
    for task in ongoing_tasks:
        print(f"- {task}")
