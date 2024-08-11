import os


def output_to_file(connection, commands):
    new_dir_name = connection.base_prompt
    os.mkdir(new_dir_name)
    for command in commands:
        filename = command.replace(' ', '_')[:-1] + '.txt'
        print(filename)
        filename = "\\".join((new_dir_name, filename))
        with open(filename, 'w') as f:
            f.write(connection.send_command(command) + '\n')