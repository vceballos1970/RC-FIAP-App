import subprocess
import argparse

def run_pyuic5(input_file, output_file):
    # Run the pyuic5 command
    subprocess.run(['pyuic5', '-o', output_file, input_file], check=True)

    # Add encoding declaration to the generated file
    with open(output_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    if not lines[0].startswith('# -*- coding: utf-8 -*-'):
        lines.insert(0, '# -*- coding: utf-8 -*-\n')

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def main():
    parser = argparse.ArgumentParser(description='Convert Qt Designer .ui file to Python script with specified encoding.')
    parser.add_argument('input_file', help='The input .ui file')
    parser.add_argument('output_file', help='The output .py file')
    
    args = parser.parse_args()
    
    run_pyuic5(args.input_file, args.output_file)

if __name__ == '__main__':
    main()
