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

    Hasan.deposit(5000)
    Jamin.deposit(5000)

    Hasan.withdrawal(1500)

    Dr_Kamal.inactive_loan_stats()
    Dr_Kamal.active_loan_status()
    Hasan.get_loan()

    Jamin.transfer(999, Angel_pria)

    print("Hasan's Transaction History\n==============================")
    Hasan.transaction_history()
    print("Hasan's current balance:", Hasan.balance, "\n")

    print("Jamin's Transaction History\n==============================")
    Jamin.transaction_history()
    print("Jamin's current balance:", Jamin.balance, "\n")

    print("========City Bank=========")
    print("Total Loan Given:", Dr_Kamal.total_loan())
    print("Liquid cash:", Dr_Kamal.total_balance())
    print("Loan status is active:", city_bank.is_loan_available)


if __name__ == '__main__':
    main()
