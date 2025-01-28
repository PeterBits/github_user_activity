import cmd
import os
import requests

class MyCLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to get GITHUB user activity CLI of PeterBits. Type "help" for available commands.'
    

    def do_hello(self, _):
        """Greets the user."""
        print("Hello, World!")
        
    def do_clear(self, _):
        """Clears the terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_get_info_of(self, username):
        url = f"https://api.github.com/users/{username}/events"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Request failed with status code {response.status_code}")


if __name__ == '__main__':
    MyCLI().cmdloop()
