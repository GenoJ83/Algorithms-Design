from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Task class definition
class Task:
    def __init__(self, name, task_type, deadline, priority, duration):
        self.name = name
        self.task_type = task_type  # "personal" or "academic"
        self.deadline = deadline  # datetime object
        self.priority = priority  # Integer priority level
        self.duration = duration  # Duration in minutes

    def __repr__(self):
        return f"{self.name} ({self.task_type}) - Priority: {self.priority}, Due: {self.deadline.strftime('%Y-%m-%d %H:%M')}, Duration: {self.duration} min"

# Quick Sort for sorting tasks by a given attribute
def quick_sort(tasks, key):
    if len(tasks) <= 1:
        return tasks
    pivot = tasks[0]
    less = [task for task in tasks[1:] if getattr(task, key) <= getattr(pivot, key)]
    greater = [task for task in tasks[1:] if getattr(task, key) > getattr(pivot, key)]
    return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

# Binary search for finding tasks by deadline
def binary_search(tasks, target_deadline):
    """Binary search to find the task with a specific deadline or the closest."""
    low, high = 0, len(tasks) - 1
    closest_task = None
    min_diff = float('inf')
    
    while low <= high:
        mid = (low + high) // 2
        mid_task = tasks[mid]
        
        # Check if the deadline matches
        if mid_task.deadline == target_deadline:
            return mid_task
        
        # Update closest task if the difference is smaller
        diff = abs((mid_task.deadline - target_deadline).total_seconds())
        if diff < min_diff:
            min_diff = diff
            closest_task = mid_task

        # Adjust search range based on deadline comparison
        if mid_task.deadline < target_deadline:
            low = mid + 1
        else:
            high = mid - 1

    return closest_task

# TaskManager class with scheduling and retrieval methods
class TaskManager:
    def __init__(self):
        self.tasks = []  # List to hold tasks
        self.schedule = []  # List of scheduled tasks

    def add_task(self, task):
        self.tasks.append(task)

    def get_upcoming_tasks(self):
        """Retrieve tasks sorted by deadline."""
        self.tasks = quick_sort(self.tasks, 'deadline')
        return self.tasks

    def find_task_by_deadline(self, target_deadline):
        """Find task by exact or closest deadline."""
        sorted_tasks = quick_sort(self.tasks, 'deadline')  # Ensure tasks are sorted
        return binary_search(sorted_tasks, target_deadline)

    def schedule_tasks(self):
        """Uses a greedy method to schedule tasks by priority and deadline."""
        current_time = datetime.now()
        scheduled_tasks = []
        
        # Sort tasks by priority first, then deadline
        sorted_tasks = quick_sort(self.tasks, 'priority')
        
        for task in sorted_tasks:
            if current_time + timedelta(minutes=task.duration) <= task.deadline:
                scheduled_tasks.append(task)
                current_time += timedelta(minutes=task.duration)
        
        self.schedule = scheduled_tasks
        return self.schedule

# Gantt chart visualization for tasks
def plot_gantt_chart(tasks):
    fig, gnt = plt.subplots()
    gnt.set_ylim(0, 50)
    gnt.set_xlim(min(task.deadline for task in tasks), max(task.deadline for task in tasks) + timedelta(minutes=60))
    gnt.set_yticks([15, 25])
    gnt.set_yticklabels(['Academic', 'Personal'])
    gnt.set_xlabel('Time')
    gnt.set_title('Task Schedule Gantt Chart')
    
    for task in tasks:
        start = task.deadline - timedelta(minutes=task.duration)
        gnt.broken_barh([(start, timedelta(minutes=task.duration))], (15 if task.task_type == "academic" else 25, 9),
                        facecolors=('tab:blue' if task.task_type == "academic" else 'tab:orange'))
    
    plt.show()

# Function to prompt the user to input tasks
def get_user_input(manager):
    print("Enter your tasks. Type 'done' when finished.")
    
    while True:
        name = input("Task name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break

        task_type = input("Task type (academic/personal): ").strip().lower()
        while task_type not in ['academic', 'personal']:
            task_type = input("Please enter a valid task type (academic/personal): ").strip().lower()

        # Deadline input with error handling
        while True:
            deadline_str = input("Deadline (YYYY-MM-DD HH:MM): ")
            try:
                deadline = datetime.strptime(deadline_str, '%Y-%m-%d %H:%M')
                break
            except ValueError:
                print("Invalid format. Please enter the deadline in the format YYYY-MM-DD HH:MM")

        priority = int(input("Priority (1 for highest priority): "))
        duration = int(input("Duration in minutes: "))

        # Create a task object and add it to the manager
        task = Task(name, task_type, deadline, priority, duration)
        manager.add_task(task)
        print(f"Task '{name}' added.\n")

# Menu function for user interaction
def display_menu(manager):
    while True:
        print("\n--- Personal Scheduling Assistant ---")
        print("1. Add Task")
        print("2. View Upcoming Tasks")
        print("3. Schedule Tasks")
        print("4. Find Task by Deadline")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            get_user_input(manager)
        elif choice == '2':
            upcoming_tasks = manager.get_upcoming_tasks()
            print("\nUpcoming Tasks:")
            for task in upcoming_tasks:
                print(task)
        elif choice == '3':
            scheduled_tasks = manager.schedule_tasks()
            print("\nScheduled Tasks:")
            for task in scheduled_tasks:
                print(task)
            plot_gantt_chart(scheduled_tasks)
        elif choice == '4':
            deadline_str = input("Enter deadline to search for (YYYY-MM-DD HH:MM): ")
            try:
                target_deadline = datetime.strptime(deadline_str, '%Y-%m-%d %H:%M')
                task = manager.find_task_by_deadline(target_deadline)
                if task:
                    print("\nTask found or closest to the deadline:")
                    print(task)
                else:
                    print("No tasks found for this deadline.")
            except ValueError:
                print("Invalid format. Please enter the deadline in the format YYYY-MM-DD HH:MM")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Main function to run the scheduling assistant
def main():
    manager = TaskManager()
    display_menu(manager)

# Run the main function
if __name__ == "__main__":
    main()
