# Создайте класс BankAccount, который представляет банковский счет, 
# c атрибутами экземпляра: 
# accountNumber (числовой тип), name (имя владельца счета строкового типа), balance.
# Создайте конструктор с параметрами: accountNumber, name, balance.
# Создайте метод Deposit(), который управляет действиями по пополнению счета.
# Создайте метод Withdrawal(), который управляет действиями по снятию средств.
# Создайте метод bankFees() для применения банковской комиссии в размере 5% от баланса счета.
# Создайте метод display() для отображения деталей счета.
# Приведите примеры использования.

class Bankaccount:
    def __init__(self, accountNumber, name, balance): 
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        self.my_balance = balance

    def top_up_balace(self):
        while True:
            try:
                money_to_add = int(input('Введите наличных денег для пополнения баланса: '))
                if money_to_add <= 0:
                    raise ZeroDivisionError
            except ZeroDivisionError:
                print('Введите больше нуля')
            except ValueError:
                print('Вы ввели некорректно')
            else:
                self.balance += money_to_add
                print(f'Ваш баланс: {self.balance} ')
                break

    def top_down_balance(self):
        while True:
            try:
                money_to_take = int(input('Введите сумму которую хотите снять: '))
                if self.balance - money_to_take < 0:
                    raise IndexError
                elif money_to_take <= 0:
                    raise ZeroDivisionError
            except IndexError:
                print('Недостаточно средств на карте ')
            except ZeroDivisionError:
                print('Введите больше нуля')
            except ValueError:
                print('Вы ввели некорректно')
            else:
                self.balance -= money_to_take
                print(f'Ваш баланс: {self.balance}')
                break
                    
    def percentage_fee_of_bank(self):
        print('Комиссия составляет:', self.balance * 0.08)      

    def display(self):
        print('Ваш баланс в карте:', self.balance)
                    

# my_name = input('Введите имя: ')
# my_account_number = int(input('Введите номер аккаунта: '))
# my_balance = int(input('Введите ваш текущий баланс: '))
# user_bank_accaunt = Bankaccount(my_account_number, my_name, my_balance)

user_bank_accaunt = Bankaccount(12345678, 'Talgat', 500)
user_bank_accaunt.top_up_balace()
user_bank_accaunt.percentage_fee_of_bank()
user_bank_accaunt.display()
user_bank_accaunt.top_down_balance()
user_bank_accaunt.percentage_fee_of_bank()
user_bank_accaunt.display()



