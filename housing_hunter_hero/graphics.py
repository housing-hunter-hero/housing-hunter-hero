from housing_hunter import user_zip

art5 = """
┬ ┬┌─┐┬ ┬┌─┐┬┌┐┌┌─┐    ┬ ┬┬ ┬┌┐┌┌┬┐┌─┐┬─┐    ┬ ┬┌─┐┬─┐┌─┐
├─┤│ ││ │└─┐│││││ ┬    ├─┤│ ││││ │ ├┤ ├┬┘    ├─┤├┤ ├┬┘│ │
┴ ┴└─┘└─┘└─┘┴┘└┘└─┘    ┴ ┴└─┘┘└┘ ┴ └─┘┴└─    ┴ ┴└─┘┴└─└─┘ 

"""



welcome_menu = """

  +++++++++++++++++++++++++++++++++++++++++++++++
  +                                             +
  +    Welcome to the Housing Hunter Hero!      +
  +                                             +
  +       1. Search by zipcode                  +
  +       2. Quit                               +
  +                                             +
  +++++++++++++++++++++++++++++++++++++++++++++++

"""


def greeting():
    """
    Initial function which generates a menu for the user to choose which option
    they would like to do, and then based on choice they can either search properties
    by zip code or exit the function
    :return: varies based on user input, but either a prompt for zip code or an exit
    message
    """
    print('\n'.join(l.center(80) for l in art5.splitlines()))
    print('\n'.join(l.center(80) for l in welcome_menu.splitlines()))
    choice = input("Please make a selection: \n")

    if choice == "1":
        print("Please enter zipcode: ")
        return user_zip()
    elif choice == "2":
        print("See you next time")
        return 2
    else:
        print("Invalid selection. Please try again.")
        greeting()

# greeting()