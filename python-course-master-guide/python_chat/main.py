import requests


"""
https://tt-python-chat.herokuapp.com/


    GET /users
        Get a list of registered users.
        Response will be either plain text or json if a "json" argument is given
        
        Arguments:
            ?json:  Boolean, Optional
    

    GET /messages
        Get all sent messages.
        Response will be either plain text or json if a "json" argument is given
        
        Arguments:
            ?json:  Boolean, Optional


    POST /register
        Register a new user name.

        Data:
            ?user:  String, Required

    POST /send
        Send a message from a registered user.

        Data:
            ?user:  String, Required
            ?message:  String, Required
"""


def get(url, arguments=None):
    response = requests.get(url, params=arguments)
    if not response.status_code == 200:
        print("GET Error", response.status_code)
        print(response.text)
        exit()

    if arguments and "json" in arguments:
        return response.json()
    else:
        return response.text


def post(url, data=None):
    response = requests.post(url, data=data)
    if not response.status_code == 200:
        print("POST Error", response.status_code)
        print(response.text)
        exit()

    if data and "json" in data:
        return response.json()
    else:
        return response.text


def print_messages():
    messages = get(url + "messages")
    print("Messages:")
    print(messages)


def send_message():
    new_message = input("\n" + user + ": ")

    data = {
        "user": user,
        "message": new_message
    }
    post(url + "send", data)


url = "https://tt-python-chat.herokuapp.com/"
registered_users = get(url + "users")
print("Currently registered users:")
print(registered_users)

user = "Nico"
if user not in registered_users:
    print("User", repr(user), "not registered. Registering.")
    data = {"user": user}
    post(url + "register", data)


print_messages()
send_message()
print_messages()
