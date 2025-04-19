# Task Manager Application

Task Manager is a robust command-line application designed and developed by Zeshan Noor. Built with Python, this tool empowers users to efficiently manage their tasks by adding, completing, deleting, and categorizing them, with persistent storage in a JSON file. Its intuitive interface and error handling make it a reliable choice for personal and professional task management.

## Features

- **Add Tasks**: Create tasks with descriptions, categories (e.g., Work, Personal), and timestamps.
- **Mark Tasks Completed**: Update task status to reflect completion.
- **Delete Tasks**: Remove tasks no longer needed.
- **View Tasks**: Display all tasks or filter to show only incomplete ones.
- **Task Categories**: Organize tasks by category for better clarity.
- **Persistent Storage**: Save tasks to a `tasks.json` file for data persistence.
- **Error Handling**: Gracefully manage invalid inputs and file operations.

## Setup Instructions

1. **Prerequisites**:

   - Python 3.6 or higher.
   - Standard Python libraries (`json`, `os`, `datetime`)—no external dependencies required.

2. **Installation**:

   - Download the `todo_app.py` script to a directory.
   - Ensure the directory has write permissions to create and modify `tasks.json`.

3. **Running the Application**:

   - Open a terminal and navigate to the script’s directory.

   - Execute:

     ```bash
     python todo_app.py
     ```

## Usage Guide

1. **Launch the Application**:

   ```bash
   python todo_app.py
   ```

   A welcome message will display:

   ```
   ==========================================
         Task Manager by Zeshan Noor
   ==========================================
   Welcome to a streamlined task management experience.
   ```

2. **Menu Options**:

   ```
   === Task Manager Menu ===
   1. Add Task
   2. Mark Task Completed
   3. Delete Task
   4. View All Tasks
   5. View Incomplete Tasks
   6. Exit
   ```

3. **Example Workflow**:

   - **Add a Task**: Select `1`, enter a description (e.g., “Complete Upwork proposal”), and specify a category (e.g., “Work”).

     ```
     Task added: Complete Upwork proposal (Category: Work)
     ```

   - **View All Tasks**: Select `4` to see:

     ```
     [ ] ID: 1 | Complete Upwork proposal | Category: Work | Created: 2025-04-18 21:57:00
     ```

   - **View Incomplete Tasks**: Select `5` to filter incomplete tasks only.

   - **Mark Completed**: Select `2`, enter ID `1`:

     ```
     Task 1 marked as completed.
     ```

   - **Delete a Task**: Select `3`, enter ID `1`:

     ```
     Task 1 deleted: Complete Upwork proposal
     ```

   - **Exit**: Select `6` to close the application.

## File Structure

- `todo_app.py`: Core application script.
- `tasks.json`: Auto-generated file for task storage (avoid manual edits).

## About the Developer

I’m Zeshan Noor, a passionate software developer dedicated to creating practical, user-focused solutions. With a keen eye for detail and a commitment to clean code, I built Task Manager to streamline productivity while showcasing my ability to deliver robust applications. My expertise in Python and problem-solving drives me to craft tools that make a difference. Connect with me on Upwork to collaborate on your next project!

## Notes

- Tasks are automatically saved after each operation.
- Corrupted `tasks.json` files trigger a fresh task list to ensure stability.
- Invalid inputs (e.g., non-numeric IDs) are handled with clear error messages.

## License

MIT License—free to use and adapt for personal or professional purposes.

Developed by Zeshan Noor, 2025