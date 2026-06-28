"""
Student Record Management System
Demonstrates: CSV/JSON file I/O, custom exceptions, logging, input validation.
"""

import csv
import json
import logging
import os
from datetime import datetime

# File paths
CSV_FILE  = "students.csv"
JSON_FILE = "students.json"
LOG_FILE  = "student_system.log"

# CSV columns
CSV_FIELDS = ["reg_number", "name", "age", "course"]

# Logging setup
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def log(msg: str, level: str = "info") -> None:
    """Write to log file and optionally print nothing (silent logging)."""
    getattr(logging, level)(msg)


# Custom exceptions
class StudentNotFoundError(Exception):
    """Raised when a student registration number does not exist."""

class DuplicateStudentError(Exception):
    """Raised when adding a student whose registration number already exists."""

class InvalidInputError(Exception):
    """Raised when user input fails validation."""


# CSV helpers
def _load_csv() -> list[dict]:
    """Return all rows from the CSV file as a list of dicts."""
    if not os.path.exists(CSV_FILE):
        return []
    try:
        with open(CSV_FILE, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except Exception as e:
        log(f"Failed to read CSV: {e}", "error")
        raise

def _save_csv(students: list[dict]) -> None:
    """Overwrite the CSV file with the given list of student dicts."""
    try:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            writer.writeheader()
            writer.writerows(students)
    except Exception as e:
        log(f"Failed to write CSV: {e}", "error")
        raise


# JSON helpers
def _load_json() -> dict:
    """Return the JSON store as a dict keyed by reg_number."""
    if not os.path.exists(JSON_FILE):
        return {}
    try:
        with open(JSON_FILE, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        log(f"Corrupt JSON file: {e}", "error")
        return {}
    except Exception as e:
        log(f"Failed to read JSON: {e}", "error")
        raise

def _save_json(data: dict) -> None:
    """Overwrite the JSON file with the given dict."""
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        log(f"Failed to write JSON: {e}", "error")
        raise


# Input helpers
def _input(prompt: str) -> str:
    """Strip and return user input; raise InvalidInputError if blank."""
    value = input(prompt).strip()
    if not value:
        raise InvalidInputError("Input cannot be empty.")
    return value

def _input_int(prompt: str, min_val: int = 1, max_val: int = 200) -> int:
    """Prompt for an integer within [min_val, max_val]."""
    raw = _input(prompt)
    if not raw.isdigit():
        raise InvalidInputError(f"'{raw}' is not a valid number.")
    val = int(raw)
    if not (min_val <= val <= max_val):
        raise InvalidInputError(f"Value must be between {min_val} and {max_val}.")
    return val


# Core operations
def add_student() -> None:
    """Add a new student to CSV and JSON stores."""
    print("\n--- Add New Student ---")
    try:
        reg    = _input("Registration number : ")
        name   = _input("Full name           : ")
        age    = _input_int("Age                 : ", 10, 100)
        course = _input("Course              : ")

        # Extra details → JSON
        address = _input("Address             : ")
        contact = _input("Contact number      : ")
        program = _input("Program (e.g. BSc)  : ")

        students = _load_csv()
        if any(s["reg_number"] == reg for s in students):
            raise DuplicateStudentError(f"Student '{reg}' already exists.")

        students.append({"reg_number": reg, "name": name, "age": age, "course": course})
        _save_csv(students)

        details = _load_json()
        details[reg] = {
            "address": address,
            "contact": contact,
            "program": program,
            "enrolled": datetime.now().strftime("%Y-%m-%d"),
        }
        _save_json(details)

        log(f"Added student: {reg} – {name}")
        print(f"\n✓ Student '{name}' ({reg}) added successfully.")

    except (InvalidInputError, DuplicateStudentError) as e:
        log(f"Add failed: {e}", "warning")
        print(f"  Error: {e}")
    except Exception as e:
        log(f"Unexpected error in add_student: {e}", "error")
        print(f"  Unexpected error: {e}")
    finally:
        log("add_student() action completed.")


def view_all_students() -> None:
    """Display all students from the CSV file."""
    print("\n--- All Students ---")
    try:
        students = _load_csv()
        if not students:
            print("  No student records found.")
            log("view_all: no records.")
            return

        print(f"  {'Reg No':<12} {'Name':<25} {'Age':<5} {'Course'}")
        print("  " + "-" * 60)
        for s in students:
            print(f"  {s['reg_number']:<12} {s['name']:<25} {s['age']:<5} {s['course']}")

        log(f"view_all: displayed {len(students)} record(s).")

    except Exception as e:
        log(f"view_all failed: {e}", "error")
        print(f"  Error reading records: {e}")
    finally:
        log("view_all_students() action completed.")


def search_student() -> None:
    """Search for a student by registration number and show full details."""
    print("\n--- Search Student ---")
    try:
        reg = _input("Enter registration number: ")

        students = _load_csv()
        match = next((s for s in students if s["reg_number"] == reg), None)
        if match is None:
            raise StudentNotFoundError(f"No student with registration number '{reg}'.")

        details = _load_json().get(reg, {})

        print(f"\n  Registration : {match['reg_number']}")
        print(f"  Name         : {match['name']}")
        print(f"  Age          : {match['age']}")
        print(f"  Course       : {match['course']}")
        print(f"  Program      : {details.get('program', 'N/A')}")
        print(f"  Address      : {details.get('address', 'N/A')}")
        print(f"  Contact      : {details.get('contact', 'N/A')}")
        print(f"  Enrolled     : {details.get('enrolled', 'N/A')}")

        log(f"search: found student {reg}.")

    except (InvalidInputError, StudentNotFoundError) as e:
        log(f"search failed: {e}", "warning")
        print(f"  Error: {e}")
    except Exception as e:
        log(f"Unexpected error in search_student: {e}", "error")
        print(f"  Unexpected error: {e}")
    finally:
        log("search_student() action completed.")


def update_student() -> None:
    """Update a student's name, age, course, or extra details."""
    print("\n--- Update Student ---")
    try:
        reg = _input("Enter registration number to update: ")

        students = _load_csv()
        index = next((i for i, s in enumerate(students) if s["reg_number"] == reg), None)
        if index is None:
            raise StudentNotFoundError(f"No student with registration number '{reg}'.")

        student = students[index]
        details = _load_json()
        extra   = details.get(reg, {})

        print(f"\n  Updating record for: {student['name']} ({reg})")
        print("  Leave blank to keep the current value.\n")

        # Update CSV fields
        name = input(f"  Name [{student['name']}]: ").strip()
        if name:
            student["name"] = name

        age_raw = input(f"  Age [{student['age']}]: ").strip()
        if age_raw:
            if not age_raw.isdigit() or not (10 <= int(age_raw) <= 100):
                raise InvalidInputError("Age must be a number between 10 and 100.")
            student["age"] = age_raw

        course = input(f"  Course [{student['course']}]: ").strip()
        if course:
            student["course"] = course

        # Update JSON fields
        address = input(f"  Address [{extra.get('address', '')}]: ").strip()
        if address:
            extra["address"] = address

        contact = input(f"  Contact [{extra.get('contact', '')}]: ").strip()
        if contact:
            extra["contact"] = contact

        program = input(f"  Program [{extra.get('program', '')}]: ").strip()
        if program:
            extra["program"] = program

        students[index] = student
        _save_csv(students)

        details[reg] = extra
        _save_json(details)

        log(f"Updated student: {reg}")
        print(f"\n  ✓ Student '{reg}' updated successfully.")

    except (InvalidInputError, StudentNotFoundError) as e:
        log(f"update failed: {e}", "warning")
        print(f"  Error: {e}")
    except Exception as e:
        log(f"Unexpected error in update_student: {e}", "error")
        print(f"  Unexpected error: {e}")
    finally:
        log("update_student() action completed.")


def delete_student() -> None:
    """Delete a student record from both CSV and JSON stores."""
    print("\n--- Delete Student ---")
    try:
        reg = _input("Enter registration number to delete: ")

        students = _load_csv()
        original_count = len(students)
        updated = [s for s in students if s["reg_number"] != reg]

        if len(updated) == original_count:
            raise StudentNotFoundError(f"No student with registration number '{reg}'.")

        confirm = input(f"  Are you sure you want to delete '{reg}'? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("  Deletion cancelled.")
            log(f"delete cancelled for {reg}.")
            return

        _save_csv(updated)

        details = _load_json()
        details.pop(reg, None)
        _save_json(details)

        log(f"Deleted student: {reg}")
        print(f"  ✓ Student '{reg}' deleted successfully.")

    except (InvalidInputError, StudentNotFoundError) as e:
        log(f"delete failed: {e}", "warning")
        print(f"  Error: {e}")
    except Exception as e:
        log(f"Unexpected error in delete_student: {e}", "error")
        print(f"  Unexpected error: {e}")
    finally:
        log("delete_student() action completed.")


# Menu
def show_menu() -> None:
    print("\n" + "=" * 45)
    print("   STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 45)
    print("  1. Add a new student")
    print("  2. View all students")
    print("  3. Search student by registration number")
    print("  4. Update student details")
    print("  5. Delete a student record")
    print("  6. Exit")
    print("=" * 45)


def main() -> None:
    log("=== System started ===")
    print("\nWelcome to the Student Record Management System")

    ACTIONS = {
        "1": add_student,
        "2": view_all_students,
        "3": search_student,
        "4": update_student,
        "5": delete_student,
    }

    while True:
        show_menu()
        try:
            choice = _input("Enter your choice (1-6): ")
        except InvalidInputError:
            print("  Please enter a number from 1 to 6.")
            continue

        if choice == "6":
            log("=== System exited by user ===")
            print("\nGoodbye!\n")
            break
        elif choice in ACTIONS:
            ACTIONS[choice]()
        else:
            print("  Invalid choice. Please enter a number from 1 to 6.")
            log(f"Invalid menu choice: '{choice}'", "warning")


if __name__ == "__main__":
    main()
