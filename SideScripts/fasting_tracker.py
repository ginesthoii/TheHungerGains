import csv
from datetime import datetime, timedelta
import os

CSV_FILE = 'fasting_log.csv'

def setup_csv():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Date', 
                'Fast Type', 
                'Fast Start', 
                'Fast End', 
                'Fast Duration (hours)', 
                'Energy Level (1-5)', 
                'Exercise', 
                'Notes'
            ])

def log_fast():
    """Prompt the user for log data and write it to the CSV."""
    date_str = input("Enter date (YYYY-MM-DD, e.g., 2025-09-11): ")
    fast_type = input("Enter fast type (e.g., 16:8, OMAD): ")
    
    start_time_str = input("Enter fast start time (HH:MM, e.g., 20:00): ")
    end_time_str = input("Enter fast end time (HH:MM, e.g., 12:00 next day): ")
    
    energy = input("Enter energy level (1-5): ")
    exercise = input("Enter exercise (e.g., '30-min walk'): ")
    notes = input("Enter notes: ")

    # Calculate fast duration
    try:
        start_datetime = datetime.strptime(f"{date_str} {start_time_str}", "%Y-%m-%d %H:%M")
        end_datetime = datetime.strptime(f"{date_str} {end_time_str}", "%Y-%m-%d %H:%M")
        # Handle fasts that cross midnight
        if end_datetime < start_datetime:
            end_datetime += timedelta(days=1)
        
        duration = (end_datetime - start_datetime).total_seconds() / 3600
        duration = round(duration, 2)
    except ValueError:
        print("Invalid time format. Fast duration will be listed as N/A.")
        duration = "N/A"

    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            date_str, 
            fast_type, 
            start_time_str, 
            end_time_str, 
            duration, 
            energy, 
            exercise, 
            notes
        ])
    print("Log added successfully!")

def view_log():
    """Display the entire fasting log."""
    if not os.path.exists(CSV_FILE):
        print("No log file found. Please add an entry first.")
        return

    with open(CSV_FILE, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))

def main():
    """Main function to run the script."""
    setup_csv()
    while True:
        print("\nIntermittent Fasting Tracker")
        print("1. Log a new fast")
        print("2. View all fasts")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            log_fast()
        elif choice == '2':
            view_log()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()