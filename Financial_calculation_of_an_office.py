import enum
# --------------------------------------------------------------------------------


class Employee:
    def __init__(self, name, family, address, mobile, age) -> None:
        self.__name = name
        self.__family = family
        self.__address = address
        self.__mobile = mobile
        self.__age = age

    def _show_Employee_info(self):
        return f"Name: {self.__name}\tFamily: {self.__family}\nAddress: {self.__address}\tMoblie: {self.__mobile}\tAge: {self.__age}"

# --------------------------------------------------------------------------------


class LaborOfficeRights(enum.Enum):
    basicSalaryOfficial = 5000000
    amountOvertimeHour = 32000
    rightChild = 480000
    basicDailySalaryContractual = 250000
# --------------------------------------------------------------------------------


class OfficialEmployee(Employee):
    def __init__(self, name, family, address, mobile, age, numberChildren):
        super().__init__(name, family, address, mobile, age)
        self.__basicSalaryOfficial = LaborOfficeRights.basicSalaryOfficial.value
        if numberChildren > 3:
            numberChildren = 3
        self.__numberChildren = numberChildren
        self.__overtimeHours = 0
        self.__amountOvertimeHour = LaborOfficeRights.amountOvertimeHour.value
        self.__premium = 0

    def save_to_database(self):
        pass

    def __calculate_premium(self):
        self.__premium = self.__basicSalaryOfficial*0.09
        return self.__premium

    # Receiving overtime information from the entry and exit registration system
    @property
    def overtimeHours(self):
        return self.__overtimeHours

    @overtimeHours.setter
    def overtimeHours(self, timeHours):
        if timeHours > 30:
            timeHours = 30
        self.__overtimeHours = timeHours

    def calculate_salary(self):
        self.__calculate_premium()
        totall = self.__basicSalaryOfficial+(self.__amountOvertimeHour*self.__overtimeHours)+(
            self.__numberChildren*LaborOfficeRights.rightChild.value)-self.__premium
        return totall

    def show_info(self) -> str:
        return f"{self._show_Employee_info()}\nSalary : {str(self.calculate_salary())}"


# --------------------------------------------------------------------------------


class ContractualOfficial(Employee):
    def __init__(self, name, family, address, mobile, age):
        super().__init__(name, family, address, mobile, age)
        self.__dailySalary = LaborOfficeRights.basicDailySalaryContractual.value
        self.__numberDays = 0
        self.__violation = 0

    def save_to_database(self):
        pass

    def __calculate_premium(self):
        self.__premium = self.__dailySalary*0.03
        return self.__premium

    # Receiving numberDays information from the entry and exit registration system
    @property
    def numberDays(self):
        return self.__numberDays

    @numberDays.setter
    def numberDays(self, numDay):
        self.__numberDays = numDay

    # Receiving violation information from the entry and exit registration system
    @property
    def violation(self):
        return self.__violation

    @violation.setter
    def violation(self, violationSystem):
        if violationSystem > 500000:
            violationSystem = 500000
        self.__violation = violationSystem

    def calculate_salary(self):
        self.__calculate_premium()
        totall = (self.__dailySalary*self.__numberDays) -self.__premium-self.__violation
        return totall

    def show_info(self) -> str:
        return f"{self._show_Employee_info()}\nSalary : {str(self.calculate_salary())}"


# --------------------------------------------------------------------------------
oe1 = OfficialEmployee("meiad", "noushadi", "shiraz", "09170001122", 29, 8)
oe1.overtimeHours = 58
print(oe1.show_info())
# --------------------------------------------------------------------------------
ce1 = ContractualOfficial("ali", "karimi", "esfahan", "09131112233", 23)
ce1.numberDays = 25
ce1.violation = 900000
print(ce1.show_info())
