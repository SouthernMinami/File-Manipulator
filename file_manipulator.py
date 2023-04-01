import sys

contents = ''
command = sys.argv[1]

def reverse(input_path, output_path):
    with open(input_path) as f:
        contents = f.read()

    with open(output_path, 'w') as f:
        f.write(''.join(reversed(contents)))


def copy(input_path, output_path):
    with open(input_path) as f:
        contents = f.read()

    with open(output_path, 'w') as f:
        f.write(contents)


def duplicate_contents(input_path, n):
    with open(input_path) as f:
        contents = f.read()

    with open(input_path, 'a') as f:
        for i in range(int(n)):
            f.write("\n" + contents)

def replace_string(input_path, needle, new_string):
    with open(input_path) as f:
        contents = f.read()

    with open(input_path, 'w') as f:
        f.write(contents.replace(needle, new_string))



if command == 'reverse' : reverse(sys.argv[2], sys.argv[3])
elif command == 'copy' : copy(sys.argv[2], sys.argv[3])
elif command == 'duplicate-contents' : duplicate_contents(sys.argv[2], sys.argv[3])
elif command == 'replace-string' : replace_string(sys.argv[2], sys.argv[3], sys.argv[4])