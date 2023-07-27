# Budget Planner CLI

The Budget Planner CLI is a command-line tool designed to help you manage your monthly budget, track expenses, and monitor your income. It allows you to set budget categories, record expenses, and track your financial progress as it relates to your monthly budget.

## Getting Started

### Prerequisites

Before using the Budget Planner CLI, ensure you have the following prerequisites installed on your system:

- Python (version 3.6 or higher)
- SQLite (or any other supported database system)

### Installation

1. Clone the project from the GitHub repository:
`$ git clone https://github.com/AspenWilson/p3-project-budget-planner.git` 

2. Navigate to the project directory:
`$ cd p3-project-budget-planner`

3. Install the required Python dependencies:
`$ pip install -r requirements.txt`

4. Set up the database by running the following command:
`$ python lib/db/database.py`


## Usage/Examples

To start using the Budget Planner CLI, open a terminal or command prompt and navigate to the project directory by entering the below:

`$ cd lib/db`

All commands can be called by entering:
`$ python cli.py` and then providing the command prompt
### Available Commands

W - Welcome message: 
- Use: Display a list of all available commands
- Code: `$ python cli.py w`

1 - View expenses:
- Use: View your current budget
- Code: `$ python cli.py 1`

2 - Set budget:
- Use: Set your monthly budget by expense category
- Code: `$ python cli.py 2`

3 - Monthly summary:
- Use: View a high level summary of your monthly income, expenses, budget, and variance
- Code: `$ python cli.py 3`

A1 - Add expense :
- Use: Add a new expense entry
- Code: `$ python cli.py a1`

A2 - Add income:
- Use: Add a new income entry
- Code: `$ python cli.py a2`

A3 - Add expense category:
- Use: Add a new expense category
- Code: `$ python cli.py a3`

A4 - Add income type:
- Use: Add a new income type
- Code: `$ python cli.py a4`

U1 - Update expense:
- Use: Update a current expense entry
- Code: `$ python cli.py u1`

U2 - Update income:
- Use: Update a current income entry
- Code: `$ python cli.py u2`

U3 - Update actuals and variances: 
- Use: Update the actuals and variances for Budget and Monthly Income
- Code: `$ python cli.py u3`

U4 - Update expected monthly income:
- Use: Update your expected monthly income 
- Code: `$ python cli.py u4`

D1 - Delete expense:
- Use: Delete an expense entry
- Code: `$ python cli.py d1`

D2 - Delete income:
- Use: Delete an income entry
- Code: `$ python cli.py d2`

D3 - Delete expense category:
- Use: Delete an expense category
- Code: `$ python cli.py d3`

D4 - Delete income type:
- Use: Delete an income type
- Code: `$ python cli.py d4`

E1 - Export all data:
- Use: Export all data in xlsx files
- Code: `$ python cli.py e1`

E2 - Export current year data:
- Use: Export current year data into xlsx files
- Code: `$ python cli.py e2`

E3 - Export current month data:
- Use: Export current month data into xlsx files
- Code: `$ python cli.py e3`

X - Delte all data:
- Use: Delete all current data in your CLI
- Code: `$ python cli.py x`


## Documentation

This CLI uses multiple files. You should not need to update these in order for your CLI to function properly, but below is a brief summary of what each file in the lib/db folder contains:

### Add_Data.py 
This contains all code related to the add commands. 
### Budget.py 
This contains code for setting your monthly budget. 
### CLI.py 
This contains the CLI commands. 
### Database.py 
This code sets up your database. 
### DeBug.py 
This contains code that allows you to enter the ipdb shell. 
### Delete_Data.py 
This contains all code related to deleting data. 
### Export_Data.py 
This contains all code for exporting your data to xlsx files. 
### Helpers.py 
This contains helper functions that are used in multiple different files. 
### Models.py 
This contains the models (classes) for the database. 
### Seed.py 
This contains the code to generate seed data. 
### Summaries.py 
This contains the code related to generating summaries based on your data. 
### Update_Data.py 
This contains all code related to updating your data. 
### Variances.py 
This contains all the code responsible for updating your actuals and variances, based on your entries. 
### Welcome.py
This contains all the print() lines for the Welcome message. 

## Support

To exit out of any command, enter Control+C in your terminal. 

If you encounter any issues or have questions related to the Budget Planner CLI, please feel free to create an issue on the project's GitHub repository.
