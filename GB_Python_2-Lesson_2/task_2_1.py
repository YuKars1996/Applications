import csv
import re


def get_data():
    files = ['info_1.txt', 'info_2.txt', 'info_3.txt']

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    i = 0
    for file in files:

        fh = open(file, "r")

        for line in fh:
            prod = re.split('Изготовитель системы:', line)
            if len(prod) == 2:
                os_prod_list.append(prod[1].strip())

            name = re.split('Название ОС:', line)
            if len(name) == 2:
                os_name_list.append(name[1].strip())

            code = re.split('Код продукта:', line)
            if len(code) == 2:
                os_code_list.append(code[1].strip())

            type = re.split('Тип системы:', line)
            if len(type) == 2:
                os_type_list.append(type[1].strip())

        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])
        i = i + 1
        fh.close()

    return main_data


def write_to_csv(name_file):
    data = get_data()
    with open(name_file, 'w') as fh:
        fh_writer = csv.writer(fh)
        for row in data:
            fh_writer.writerow(row)


def main():
    csvfile = 'result.csv'

    write_to_csv(csvfile)

    with open(csvfile) as fh:
        print(fh.read())


if __name__ == '__main__':
    main()
