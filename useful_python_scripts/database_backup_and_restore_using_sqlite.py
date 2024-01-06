import sqlite3
import shutil

# Database file paths
source_db_file = 'source.db'
backup_db_file = 'backup.db'


# Function to create a backup of the SQLite database
def backup_database():
    try:
        shutil.copy2(source_db_file, backup_db_file)
        print("Backup successful.")
    except Exception as e:
        print(f"Backup failed: {str(e)}")


# Function to restore the SQLite database from a backup
def restore_database():
    try:
        shutil.copy2(backup_db_file, source_db_file)
        print("Restore successful.")
    except Exception as e:
        print(f"Restore failed: {str(e)}")


# Usage
while True:
    print("Options:")
    print("1. Backup Database")
    print("2. Restore Database")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        backup_database()
    elif choice == '2':
        restore_database()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

"""
In this code:

1. backup_database() function makes a copy of the source SQLite database file
and names it as the backup file. You can run this function to create backup
of your database.

2. restore_database() function copies the backup file back to the source file,
effectively restoring the database to the state it was when the backup was created.

3. The user is presented with options to either backup the database,
restore it, or quit the program.

4. You can adjust the source_db_file and backup_db_file variables to specify 
the paths to your SQLite source and backup database files.
"""
