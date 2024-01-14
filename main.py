from sys import exit 

main_user_dict = {}

def input_error(func):
    def inner(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except KeyError:
                print("Enter user name")
            except ValueError:
                print ("Give me name and phone please")
            except IndexError:
                print ("Invalid input. Please try again.")
    return inner


def hello():
    print('How I can help you?')


def add(input):
    if input[2].isnumeric():
        name = input[1].title()
        main_user_dict[name] = input[2]
    elif input[3].isnumeric():
        name = input[1].title() + ' ' + input[2].title()
        main_user_dict[name] = input[3]
    else:
        raise ValueError
    print('Contact added.')


def change(input):
    if input[2].isnumeric():
        name = input[1].title()
        main_user_dict[name] = input[2]
    elif input[3].isnumeric():
        name = input[1].title() + ' ' + input[2].title()
        main_user_dict[name] = input[3]
    else:
        raise ValueError
    print('Contact changed.')


def phone(input):
    if len(input) > 2:
        name = input[1].title() + ' ' + input[2].title()
    else:
        name = input[1].title()
    print(f'Phone is: {main_user_dict[name]}')


def show_all():
    print(f'All your contacts: {main_user_dict}')


def good_bye():
    print('Good bye!')
    exit()

@input_error
def main(): 
    while True:
        user_input = input('Enter command: ').lower().strip().split()
        command = user_input[0]
        
        if command == '.':
            break

        elif command == 'hello':
            hello()

        elif command == 'add':
            add(user_input)
            
        elif command == 'change':
            change(user_input)
            
        elif command == 'phone': 
            phone(user_input)

        elif len(user_input) > 1:
            if command + ' ' + user_input[1] == 'show all':
                show_all()
            if command + ' ' + user_input[1] == 'good bye':
                good_bye()

        elif command in ['close', 'exit']:
            good_bye()
            
        else:
            raise IndexError




if __name__ == '__main__':
    main()
   