# Lawyer Coffee Analysis

This mini-project explores how lawyers' coffee consumption changes as deadlines approach, and how it relates to the number of hours worked. It demonstrates foundational skills in **Python**, **Pandas**, and **Matplotlib**, which meet the “prior programming experience” requirement for Imperial College’s Machine Learning & AI programme.


## Project Files

- `lawyer_project.py` - Main Python script  
- `lawyer_coffee.csv` - Dataset used for analysis  
- Two generated charts:
  - Coffee Consumption vs Days to Deadline (Line Chart)
  - Coffee Consumption vs Hours Worked (Scatter Plot)


## Project Overview

This project uses a synthetic dataset representing three lawyers working toward case deadlines.  
Each day tracks:

- `days_to_deadline`
- `coffee_cups`
- `hours_worked`

The script loads the data using **Pandas**, explores it with `.head()`, `.info()`, and `.describe()`, and visualises relationships using **Matplotlib**.


## Key Insights

### Coffee Consumption vs Deadline  
As deadlines approach (`days_to_deadline` decreases), lawyers tend to drink more coffee.  
This may reflect increased workload and pressure.

### Coffee Consumption vs Hours Worked  
There is a positive correlation between hours worked and coffee consumed.  
Higher workload → Higher caffeine intake.

## Skills Demonstrated

- Writing and running Python scripts  
- Debugging errors in VS Code  
- Using Pandas for data loading and analysis  
- Creating visualisations with Matplotlib  
- Interpreting real-world data  
- Structuring a reproducible project for GitHub
