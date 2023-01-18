from address_to_json import info_to_json
import json

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
        return 1
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



def render_property(ADDRESS):

    with open(f'{ADDRESS}') as our_info:
        our_info = json.load(our_info)

    # print(ADDRESS)

    def print_one():
        # print("  +                                             +")
        return

    street = our_info['payload']['addressSectionInfo']['streetAddress']['assembledAddress']
    city = our_info['payload']['addressSectionInfo']['city']
    state = our_info['payload']['addressSectionInfo']['state']
    bed = our_info['payload']['addressSectionInfo']['beds']
    bath = our_info['payload']['addressSectionInfo']['baths']
    price = our_info['payload']['addressSectionInfo']['priceInfo']['amount']
    sq_ft = our_info['payload']['addressSectionInfo']

    print(f"Address of Property: {street}, {city} {state}")
    print(f"Number of bedrooms: {bed}")
    print(f"Number of bathrooms: {bath}")
    print(f"Number of square feet: {sq_ft}")
    print(f"Current Market Price: ${price}")
    # print_one()


render_property("data_assets/41 Fig St, Central Islip  New York.json")
