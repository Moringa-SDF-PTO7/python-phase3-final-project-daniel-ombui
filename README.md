# Phase 3 CLI+ORM Project Template

## Learning Goals

- Discuss the basic directory structure of a CLI.
- Outline the first steps in building a CLI.

---

## Introduction

You now have a basic idea of what constitutes a CLI. Fork and clone this lesson
for a project template for your CLI.

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── model_1.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

Note: The directory also includes two files named `CONTRIBUTING.md` and
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard or
delete the files if you want.

---

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```

You can run the template CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. The template CLI will ask for input, do
some work, and accomplish some sort of task.

Past that, CLIs can be whatever you'd like, as long as you follow the project
requirements.

Of course, you will update `lib/cli.py` with prompts that are appropriate for
your application, and you will update `lib/helpers.py` to replace `helper_1()`
with a useful function based on the specific problem domain you decide to
implement, along with adding other helper functions to the module.

In the `lib/models` folder, you should rename `model_1.py` with the name of a
data model class from your specific problem domain, and add other classes to the
folder as needed. The file `lib/models/__init__.py` has been initialized to
create the necessary database constants. You need to add import statements to
the various data model classes in order to use the database constants.

You are also welcome to implement a different module and directory structure.
However, your project should be well organized, modular, and follow the design
principal of separation of concerns, which means you should separate code
related to:

- User interface
- Data persistence
- Problem domain rules and logic

---

### **Getting Started**

Overview of what the project is and what users need to know to begin.

### Installation

Instructions for setting up the project, including environment and dependency setup. Include commands where necessary.

```bash
# Example setup commands
pipenv install
pipenv shell

## Usage
- How to run the main program, what it does, and any options or  arguments it takes.

## Files & Functionality
- cli.py - Main CLI script that provides an interface to the user. Includes detailed functionality of commands and options available.
- main.py - Core logic that powers the CLI.
- models.py - Contains data models and their relationships.
- config.py - Manages configuration details like database connection and environment variables.
- utils.py - Utility functions used across the project.

## Commands & Functions
- Each command (if it’s a CLI) and major function should get a brief description. Here’s an example:

run(): Main entry function for the application.
load_data(): Loads data from the specified file and prepares it for processing.
analyze_results(): Analyzes data based on the input parameters.

## Models
List and describe any database models, including relationships if applicable.

- Employee Model: Represents an employee, with attributes for name, department_id, and salary.
- Review Model: Stores an annual review for an employee, including year, summary, and employee_id.



## Resources

- [Setting up a respository - Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
