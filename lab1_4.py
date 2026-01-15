'''| Function Name | Arguments | Description |
| --- | --- | --- |
| `calculate_average` | `num1, num2, num3` | Calculate the mathematical average of three different numbers. |
| `add_tax` | `bill_total` | Given a dollar amount, return the total after adding a **10%** sales tax. |
| `greet_user` | `name` | Accept a string and return a greeting that says "Hello" followed by that name. |

**Verify:** Run `python3 test_4.py` in the terminal.'''

def calculate_average(num1:float,num2:float,num3:float) -> float:
    avg = (num1+num2+num3)/3
    return(avg)
def add_tax(bill_total:int) -> float:
    total = bill_total+ (bill_total*10/100)
    return total
def greet_user(name:str)-> str:
    greeting = "Hello"+' '+name
    return greeting


