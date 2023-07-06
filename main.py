from bank import Bank


def main():

    # Creating a Bank
    city_bank = Bank('City Bank')

    # Admin Account
    Dr_Kamal = city_bank.create_admin_account(
        "Mainul", "kamal@gamil.com", city_bank)

    # General Account
    Hasan = city_bank.create_General_account(
        "Hasan", "hasan@gamil.com", city_bank)
    Jamin = city_bank.create_General_account(
        "Jamin", "jamin@gmail.com", city_bank)
    Angel_pria = city_bank.create_General_account(
        "Angel_pria", "pria@gmail.com", city_bank)

    Hasan.deposit(500)
    Hasan.deposit(5000)
    Jamin.deposit(5000)
    Hasan.withdrawal(1500)
    # Dr_Kamal.inactive_loan_stats()
    Hasan.get_loan()
    Jamin.transfer(999, Angel_pria)
    Jamin.withdrawal(1000)
    Jamin.transaction_history()
    print("Hasan's current balance:", Hasan.balance)
    # Hasan.transaction_history()

    print("========City Bank=========")
    print("Total Loan Given:", Dr_Kamal.total_loan())
    print("Liquid cash:", Dr_Kamal.total_balance())
    print("Loan status is active:", city_bank.is_loan_available)


if __name__ == '__main__':
    main()
