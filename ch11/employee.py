class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise=""):
        """When called, add $5,000 to annual salary by default, but can accept
        an alternative amount"""
        new_salary_increment = 0
        if salary_raise:
            new_salary_increment += int(salary_raise)
            self.annual_salary += new_salary_increment
            print(f"New salary is: {self.annual_salary:,}")
            return self.annual_salary
        else:
            new_salary_increment = 5_000
            self.annual_salary += new_salary_increment
            print(f"New salary is {self.annual_salary:,}")
            return self.annual_salary
