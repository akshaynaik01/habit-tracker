import json
import os
from datetime import datetime
from typing import List, Dict

class HabitTracker:
    """A simple habit tracker to track daily habits and progress."""
    
    def __init__(self, data_file='habits.json'):
        self.data_file = data_file
        self.habits = self.load_habits()
    
    def load_habits(self) -> Dict:
        """Load habits from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}
    
    def save_habits(self) -> None:
        """Save habits to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.habits, f, indent=2)
    
    def add_habit(self, habit_name: str) -> bool:
        """Add a new habit to track."""
        if habit_name in self.habits:
            print(f"Habit '{habit_name}' already exists!")
            return False
        
        self.habits[habit_name] = {
            'created_date': datetime.now().strftime('%Y-%m-%d'),
            'completed_dates': []
        }
        self.save_habits()
        print(f"Habit '{habit_name}' added successfully!")
        return True
    
    def log_habit(self, habit_name: str, date: str = None) -> bool:
        """Log completion of a habit for a specific date."""
        if habit_name not in self.habits:
            print(f"Habit '{habit_name}' not found!")
            return False
        
        date = date or datetime.now().strftime('%Y-%m-%d')
        
        if date in self.habits[habit_name]['completed_dates']:
            print(f"Habit '{habit_name}' already logged for {date}!")
            return False
        
        self.habits[habit_name]['completed_dates'].append(date)
        self.save_habits()
        print(f"Habit '{habit_name}' logged for {date}!")
        return True
    
    def get_streak(self, habit_name: str) -> int:
        """Get current streak for a habit."""
        if habit_name not in self.habits:
            return 0
        
        completed_dates = sorted(self.habits[habit_name]['completed_dates'])
        if not completed_dates:
            return 0
        
        streak = 0
        today = datetime.now().date()
        
        for i in range(len(completed_dates) - 1, -1, -1):
            date = datetime.strptime(completed_dates[i], '%Y-%m-%d').date()
            if (today - date).days == streak:
                streak += 1
            else:
                break
        
        return streak
    
    def list_habits(self) -> None:
        """Display all habits and their stats."""
        if not self.habits:
            print("No habits to display!")
            return
        
        print("\n=== Your Habits ===")
        for habit_name, data in self.habits.items():
            streak = self.get_streak(habit_name)
            completed_count = len(data['completed_dates'])
            print(f"\n  {habit_name}")
            print(f"    Created: {data['created_date']}")
            print(f"    Completed: {completed_count} times")
            print(f"    Current Streak: {streak} days")
    
    def delete_habit(self, habit_name: str) -> bool:
        """Delete a habit."""
        if habit_name not in self.habits:
            print(f"Habit '{habit_name}' not found!")
            return False
        
        del self.habits[habit_name]
        self.save_habits()
        print(f"Habit '{habit_name}' deleted!")
        return True


def main():
    tracker = HabitTracker()
    
    while True:
        print("\n=== Habit Tracker Menu ===")
        print("1. Add a new habit")
        print("2. Log a habit")
        print("3. View all habits")
        print("4. Delete a habit")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            habit_name = input("Enter habit name: ").strip()
            tracker.add_habit(habit_name)
        
        elif choice == '2':
            habit_name = input("Enter habit name to log: ").strip()
            tracker.log_habit(habit_name)
        
        elif choice == '3':
            tracker.list_habits()
        
        elif choice == '4':
            habit_name = input("Enter habit name to delete: ").strip()
            tracker.delete_habit(habit_name)
        
        elif choice == '5':
            print("Thank you for using Habit Tracker!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
