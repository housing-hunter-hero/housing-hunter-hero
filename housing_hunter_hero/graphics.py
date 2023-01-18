from housing_hunter import name_url_scraper, bed_bath_scraper, smash_together

welcome_menu = """

  +++++++++++++++++++++++++++++++++++++++++++++++
  +                                             +
  +    Welcome to the Housing Hunter Hero!      +
  +                                             +
  +       1. Research A Property                +
  +       2. Compare 2 Properties               +
  +       3. Research an Area Code              +
  +       4. Compare 2 Area Codes               +
  +       5. Research a State                   +
  +       6. Compare 2 States                   +
  +                                             +    
  +       Choose and option 1 - 6               +               
  +                                             +
  +++++++++++++++++++++++++++++++++++++++++++++++

"""


def greeting():
    print(welcome_menu)
    choice = input("Please make a selection: \n")

    if choice == "1":
        print("Thank you for choosing Research A Property")
        return smash_together(name_url_scraper(), bed_bath_scraper())
    elif choice == "2":
        print("Thank you for choosing Compare 2 Properties")
        return 2
    elif choice == "3":
        print("Thank you for choosing Research an Area Code")
        return 3
    elif choice == "4":
        print("Thank you for choosing Compare 2 Area Codes")
        return 4
    elif choice == "5":
        print("Thank you for choosing Research a State")
        return 4
    elif choice == "6":
        print("Thank you for choosing Compare 2 States")
        return 4
    else:
        print("Invalid selection. Please try again.")
