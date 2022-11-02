# Demo on how to call functions using dynamically created function names
# Author: Matteo Del Grosso
# Date: November 2022

import device


def main():
    f1()
    f2()


def f1():
    dev = device.Device()
    # get attribute values from property functions
    for att_val, att_name in enumerate(('attribute_1', 'attribute_2', 'attribute_3'), 1):
        att_val_get = dev.get_attribute(att_name, att_val)
        print(f'{att_name} = {att_val_get}')


def f2():
    dev = device.Device()
    for att_val, att_name in enumerate(('attribute_1', 'attribute_2', 'attribute_3'), 1):
        att_val = dev.get_attribute(att_name, att_val)
        print(f'{att_name} = {att_val}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
