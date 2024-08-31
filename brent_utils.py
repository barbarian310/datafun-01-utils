''' ITERATION 3

Module: Foreshadow Intelligence - Reusable Module for My Data Analytics Projects

Here we define more variables to integrate into our company byline

'''

is_student: bool = True
age_in_years: int = 24
names_of_IDEs_installed: list = ['CLion', 'IntelliJ', 'Pycharm', 'VSCode', 'Visual Studio']
ideal_human_temperatures: list = [98.6, 37.0]
byline: str = f"""Foreshadow Intelligence: Your outlook has never been so good.
It is {is_student} that I am still a student at {age_in_years} years old. However, I have a plethora
of tools at my disposal, including {names_of_IDEs_installed}. As a side note, normal human temperatures are {ideal_human_temperatures} in fahrenheit and celsius respectively."""

# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# No parameters are required

#main() function definition
def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(byline)
    
    
#get_byline() definition
def get_byline():
    '''This function returns the byline variable, and does not automatically print it'''
    return byline

#main() is only called if the module __name__ is set to '__main__', not when it is imported

if __name__ == '__main__':
    print(get_byline())
