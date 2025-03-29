import requests
import subprocess

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

def get_star_type(kelvin):
    if 2400 <= kelvin < 3700:
        return "M", "Light orange red"
    elif 3700 <= kelvin < 5200:
        return "K", "Pale yellow orange"
    elif 5200 <= kelvin < 6000:
        return "G", "Yellowish white"
    elif 6000 <= kelvin < 7500:
        return "F", "White"
    elif 7500 <= kelvin < 10000:
        return "A", "Bluish white"
    elif 10000 <= kelvin < 30000:
        return "B", "Deep blue white"
    elif 30000 <= kelvin < 100000:
        return "O", "Blue"
    else:
        return None, None

def main():
    # Arte ASCII
    print("# Find out some interesting things about Space!")
    print("# Ian Annase")
    print("#                           *     .--.")
    print("#                                / /  `")
    print("#               +               | |")
    print("#                      '         \\ \\__,")
    print("#                  *          +   '--'  *")
    print("#                      +   /\\")
    print("#         +              .'  '.   *")
    print("#                *      /======\\      +")
    print("#                      ;:.  _   ;")
    print("#                      |:. (_)  |")
    print("#                      |:.  _   |")
    print("#            +         |:. (_)  |          *")
    print("#                      ;:.      ;")
    print("#                    .' \\:.    / `.")
    print("#                   / .-'':._.'`-. \\")
    print("#                   |/    /||\\    \\|")
    print("#             jgs _..--\"\"\"````\"\"\"--.._")
    print("#           _.-'``                    ``'-._")
    print("#         -'                                '-")
    print("")

    choice = 1
    kelvin = 0

    while choice != 0:
        print("Welcome to your space engine!")
        print(" ")
        print("Please choose from the following options:")
        print(" ")
        print("1 - Get the location of major satellites around the world.")
        print("2 - Find out a star's type and color.")
        print("3 - Watch Star Wars - Episode IV inside of terminal.")
        print("4 - Run the educational space C++ app.")
        print("0 - Exit")
        print(" ")

        choice = int(input("choice (0-4): "))
        print("")

        if choice == 1:
            download_file("http://www.celestrak.com/NORAD/elements/stations.txt", "stations.txt")
            with open("stations.txt", "r") as file:
                print(file.read())

        elif choice == 2:
            kelvin = int(input("How hot is the star (in kelvin): "))
            star_type, star_color = get_star_type(kelvin)

            if star_type:
                print(f"Star Type: {star_type}")
                precision = 10 - ((kelvin - (2400 if star_type == 'M' else
                                               3700 if star_type == 'K' else
                                               5200 if star_type == 'G' else
                                               6000 if star_type == 'F' else
                                               7500 if star_type == 'A' else
                                               10000 if star_type == 'B' else
                                               30000)) / (130 if star_type == 'M' else
                                                           150 if star_type == 'K' else
                                                           80 if star_type == 'G' else
                                                           150 if star_type == 'F' else
                                                           250 if star_type == 'A' else
                                                           2000 if star_type == 'B' else
                                                           7000))
                print(f"Precise: {precision:.4f}")
                print(f"Star color: {star_color}")
            else:
                print("Invalid temperature range for stars.")

            input("Enter 1 to continue")

        elif choice == 3:
            subprocess.run(["telnet", "towel.blinkenlights.nl"])

        elif choice == 4:
            download_file("https://gist.githubusercontent.com/iannase/ccb19c02a536e38cde57cbbc06fc6ac9/raw/c694f737f9e3cbf48b26e7b4ebe31b23051ae850/space.cpp", "space.cpp")
            subprocess.run(["g++", "space.cpp", "-o", "space1"])
            subprocess.run(["./space1"])

        elif choice == 0:
            break

        else:
            print("Invalid choice!")

        print(" ")
        print(" ")

if __name__ == "__main__":
    main()
