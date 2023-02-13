#
# James Atkins
# First coded 10-09-2021
#


# Define main function
def main():
    # Ask user for employee name
    print('Enter employee\'s name: ', end='')
    employee_name = str(input())
    
    # Ask user for number of hours worked
    print('Enter amount of hours worked: ', end='')
    hours_worked = int(input())
    
    # Ask user for employee's pay rate
    print('Enter the employee\'s pay rate: ', end='')
    pay_rate = float(input())
    overtime_pay_rate = (pay_rate * 1.5)
    
    # Evaluate if overtime applies, calculate pay for overtime
    if (hours_worked > 40):
        overtime_hours = (hours_worked - 40)
        overtime_pay = (overtime_hours * overtime_pay_rate)
        normal_hours = 40
    elif (hours_worked <= 40):
        normal_hours = hours_worked
        overtime_hours = 0.00
        overtime_pay = 0.00
        
    # Calculate pay for normal hours and overtime hours for gross pay
    total_reg_pay = (normal_hours * pay_rate)
    total_gross_pay = (total_reg_pay + overtime_pay)
    
    # Display employee details, gross pay
    print('---------------------------------------------')
    print('Employee name: ',employee_name)
    print('')
    print('Hours Worked   Pay Rate   Overtime   Overtime Pay      RegHour Pay      Gross Pay')
    print('--------------------------------------------------------------------------------------------')
    print('{0:.2f}'.format(hours_worked), end='          ')
    print('{0:.2f}'.format(pay_rate), end='      ')
    print('{0:.2f}'.format(overtime_hours), end='       ')
    print('${0:.2f}'.format(overtime_pay), end='           ')
    print('${0:.2f}'.format(total_reg_pay), end='           ')
    print('${0:.2f}'.format(total_gross_pay))
    
# Program start
main()
