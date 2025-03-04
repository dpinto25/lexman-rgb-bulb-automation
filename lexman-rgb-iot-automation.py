on_command = "sudo gatttool -b F8:44:77:05:01:36 --char-write-req -a 0x1d -n 0000100103010000"
off_command = "sudo gatttool -b F8:44:77:05:01:36 --char-write-req -a 0x1d -n 0000100103000000"
color_command_format = "sudo gatttool -b F8:44:77:05:01:36 --char-write-req -a 0x1d -n {color}"
intensity_command_format = "sudo gatttool -b F8:44:77:05:01:36 --char-write-req -a 0x1d -n 0000110103{intensity}0000"

colors = {
    '1': '000012010400990000',  # White
    '2': '0000120104011d0000',  # Yellow
    '3': '0001307045efe0000',  # Red
    '4': '00013070400fe0000',  # Green
    '5': '000130704e7a550000',  # Purple
    '6': '0001307048b8650000',  # Light Blue
    # The LEXMAN RGB GU10 BULBS USE A PRESET COLOR TABLE. IT IS NOT POSSIBLE TO INPUT JUST ANY RGB VALUE.
}

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError:
        print("Error executing command.")

def show_menu():
    print("Choose an option:")
    print("1. Turn On Light")
    print("2. Turn Off Light")
    print("3. Change Color")
    print("4. Change Intensity")

def show_color_menu():
    print("Choose a color:")
    print("1. White")
    print("2. Yellow")
    print("3. Red")
    print("4. Green")
    print("5. Blue")

def change_color():
    show_color_menu()
    color_choice = input("Enter your choice (1/2/3/4/5): ")
    color = colors.get(color_choice)
    if color:
        color_command = color_command_format.format(color=color)
        execute_command(color_command)
    else:
        print("Invalid color choice, please try again.")

def change_intensity():
    intensity = input("Enter intensity (10 to 99): ")
    if intensity.isdigit() and 10 <= int(intensity) <= 99:
        intensity_command = intensity_command_format.format(intensity=intensity)
        execute_command(intensity_command)
    else:
        print("Invalid intensity, please enter a value between 10 and 99.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            print("Turning on the light...")
            execute_command(on_command)
        elif choice == '2':
            print("Turning off the light...")
            execute_command(off_command)
        elif choice == '3':
            change_color()
        elif choice == '4':
            change_intensity()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()