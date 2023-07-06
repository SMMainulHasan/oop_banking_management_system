from bank import Bank


def main():

    # creating a bank
    city_bank = Bank('City Bank')

    mainul = city_bank.create_admin_account(
        "Mainul", "mainul@gamil.com", city_bank)

    print(mainul.total_balance())
    print(mainul.total_loan())
    mainul.inactive_loan_stats()
    print(city_bank.is_loan_available)


if __name__ == '__main__':
    main()
