# Student Record Management System — Report


## 1. Program Design

The system is a menu-driven command-line application that manages student records using two persistent storage files:

- **`students.csv`** — stores core fields: registration number, name, age, and course.
- **`students.json`** — stores extended details per student: address, contact number, academic program, and enrollment date.

Both files are keyed by `reg_number`, which acts as the unique identifier linking a student's CSV row to their JSON entry. This separation keeps the CSV clean and easy to export while allowing the JSON to hold flexible nested data.

All user actions and system errors are recorded in **`student_system.log`** using Python's built-in `logging` module.

### Structure Overview

| Section | Purpose |
|---|---|
| File path constants | Central place to change file names |
| Logging setup | Configures the log file, format, and level |
| Custom exceptions | Three domain-specific error classes |
| CSV helpers | `_load_csv()` and `_save_csv()` |
| JSON helpers | `_load_json()` and `_save_json()` |
| Input helpers | `_input()` and `_input_int()` for validated input |
| Core operations | Five CRUD functions |
| Menu | `show_menu()` and `main()` loop |

---

## 2. Key Functions

### `add_student()`
Prompts for all fields, checks for duplicate registration numbers, appends the new row to the CSV, and writes extended details to the JSON. Records the enrollment date automatically using `datetime.now()`.

### `view_all_students()`
Loads all CSV rows and prints them in an aligned table. Reports if no records exist.

### `search_student()`
Finds a student by registration number in the CSV, then looks up their extended details from the JSON and prints a full profile.

### `update_student()`
Loads the student's current values and prompts for new ones, leaving any blank field unchanged. Saves updates back to both the CSV and JSON.

### `delete_student()`
Filters the student out of the CSV list and removes their JSON entry. Asks for a `yes/no` confirmation before deleting to prevent accidental data loss.

### Helper functions
- `_input(prompt)` — strips whitespace and raises `InvalidInputError` if the result is empty.
- `_input_int(prompt, min_val, max_val)` — calls `_input()` then validates that the value is a digit within the allowed range.

---

## 3. Exception Handling Strategy

Three custom exceptions were defined to represent specific error conditions:

| Exception | When raised |
|---|---|
| `StudentNotFoundError` | Search, update, or delete on a reg number that does not exist |
| `DuplicateStudentError` | Adding a student whose reg number is already in the CSV |
| `InvalidInputError` | Blank input or a value that fails numeric/range validation |

Each core function follows this pattern:

```python
try:
    # main logic
except (InvalidInputError, DuplicateStudentError, StudentNotFoundError) as e:
    log(f"...: {e}", "warning")
    print(f"  Error: {e}")
except Exception as e:
    log(f"Unexpected error: {e}", "error")
    print(f"  Unexpected error: {e}")
finally:
    log("function() action completed.")
```

- **`except` (known errors)** — catches expected domain errors and shows a user-friendly message without crashing.
- **`except Exception` (catch-all)** — catches unexpected errors (e.g., disk full, permission denied) and logs them at `ERROR` level.
- **`finally`** — always runs, ensuring every action is recorded in the log regardless of success or failure.

---

## 4. Testing Results

| Test Case | Expected Result | Outcome |
|---|---|---|
| Add a new student with valid inputs | Student saved to CSV and JSON | Pass |
| Add a student with an existing reg number | `DuplicateStudentError` shown | Pass |
| Leave a required field blank on add | `InvalidInputError` shown | Pass |
| Enter a non-numeric value for age | `InvalidInputError` shown | Pass |
| View all students with records present | Table printed correctly | Pass |
| View all students with empty CSV | "No records found" message | Pass |
| Search with a valid reg number | Full profile displayed | Pass |
| Search with an unknown reg number | `StudentNotFoundError` shown | Pass |
| Update a student, leaving some fields blank | Only changed fields updated | Pass |
| Delete a student with confirmation `yes` | Record removed from both files | Pass |
| Delete a student with confirmation `no` | Deletion cancelled, record kept | Pass |
| Delete with an unknown reg number | `StudentNotFoundError` shown | Pass |
| All actions logged | Entries appear in `student_system.log` | Pass |

All test cases passed. The program handles invalid input gracefully at every menu option and never crashes on user error.
