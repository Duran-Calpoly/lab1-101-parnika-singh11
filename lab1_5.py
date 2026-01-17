def check_multiple(number):
    if number%3 == 0 and number%5==0:
        return True
    else:
        return False
    
def check_password(input_string):
    password = "Python123"
    if input_string == password:
        return "access granted"
    else:
        return "access denied"
    
def calculate_federal_tax(salary):
    if salary<=11000:
        return(10/100*salary)
    elif salary<=44725:
        return(12/100*salary)
    elif salary<=95375:
        return(22/100*salary)
    else:
        return(24/100*salary)
