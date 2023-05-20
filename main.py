import argparse
import json
import xml.etree.ElementTree as ET

def parse_arguments():
    parser = argparse.ArgumentParser(description='Skrypt do parsowania argumentów, wczytywania i zapisu danych w różnych formatach.')
    parser.add_argument('--arg1', type=int, help='Przykładowy argument 1')
    parser.add_argument('--arg2', type=str, help='Przykładowy argument 2')
    parser.add_argument('--json_file', type=str, help='Plik .json do wczytania/zapisu')
    parser.add_argument('--xml_file', type=str, help='Plik .xml do wczytania/zapisu')
    return parser.parse_args()

def parse_arguments_task():
    args = parse_arguments()
    arg1_value = args.arg1
    arg2_value = args.arg2
    print(f'arg1: {arg1_value}')
    print(f'arg2: {arg2_value}')

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f'Plik {file_path} nie istnieje.')
    except json.JSONDecodeError as e:
        print(f'Błąd składni pliku .json: {e}')

def verify_json_syntax(file_path):
    try:
        with open(file_path, 'r') as file:
            json.load(file)
            print(f'Plik {file_path} ma poprawną składnię .json.')
    except FileNotFoundError:
        print(f'Plik {file_path} nie istnieje.')
    except json.JSONDecodeError as e:
        print(f'Błąd składni pliku .json: {e}')

def save_to_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f'Dane zapisano do pliku {file_path} w formacie .json.')

def load_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        print(f'Plik {file_path} nie istnieje.')
    except ET.ParseError as e:
        print(f'Błąd składni pliku .xml: {e}')

def verify_xml_syntax(file_path):
    try:
        ET.parse(file_path)
        print(f'Plik {file_path} ma poprawną składnię .xml.')
    except FileNotFoundError:
        print(f'Plik {file_path} nie istnieje.')
    except ET.ParseError as e:
        print(f'Błąd składni pliku .xml: {e}')

def save_to_xml_file(root, file_path):
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print(f'Dane zapisano do pliku {file_path} w formacie .xml.')

def main():
    args = parse_arguments()
    if args.arg1 or args.arg2:
        parse_arguments_task()
    if args.json_file:
        data = load_json_file(args.json_file)
        if data:
            save_to_json_file(data, args.json_file)
    if args.xml_file:
        root = load_xml_file(args.xml_file)
        if root:
            save_to_xml_file(root, args.xml_file)

if __name__ == 'main':
    main()