import sys


def get_command():
    if len(sys.argv) < 2:
        print("Following the format: Config.py <command_name>.txt Device_list.txt")
        sys.exit()
    # Input_command = sys.argv
    # print(Input_command)

    with open(sys.argv[1], 'r') as f:
        commands = f.read().splitlines()
        # commands = f.readlines()
        # print(commands)
        return commands
