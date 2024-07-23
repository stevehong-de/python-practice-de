from datetime import datetime as dt, date
from dateutil.relativedelta import relativedelta


class MyAge:
    def __init__(self, date_of_birth, my_name):
        # __init__ function to fill properties and use self
        # your birthdate input yyyy-mm-dd
        self.__date_of_birth = dt.strptime(date_of_birth, '%Y-%m-%d')
        self.__my_name = my_name
        self.__my_age_years = relativedelta(
            date.today(), self.__date_of_birth).years

    # create print function
    def show_me_my_age(self):
        return f"{self.__my_name}, you are so young, only {self.__my_age_years} years old!"