
# Mandatory Assignment 2


The aim of this project is to create a packeage that generates a messages and automatically sends the reminder to the student. The modules are already created but need to be excuted in the man.py file. 


## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform


## Package Structure
```
Mandatory-assignment-2/
│
├── study_reminders/
│   ├── __init__.py
│   ├── students.py
│   ├── reminder_generator.py
│   ├── reminder_sender.py
│   ├── logger.py
│   ├── students_manager.py
│   └── scheduler_.py
│
├── main.py
├── students.json
├── reminder_log.txt
├── setup.py
└── README.md
```
## Installation

To install follow these steps

1. Clone the repository

```bash
  git clone https://github.com/dananvaro/Mandatory-assignment-2.git
  cd Mandatory-assignment
```

2. Install the package

```bash
  pip install -e .
```
    
## Usage/Examples
After installation you can run this line in the terminal to run the reminder
```python
schedule-reminder

```