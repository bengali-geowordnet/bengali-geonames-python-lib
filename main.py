# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import src.classification as bg
import src.load_data as loader


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    bg.get_bengali_class_from_feature_code("ADM1")
    bg.get_bengali_class_from_english_feature("zone")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # loader.read_csv_into_dictionary('Bengali_Geonames_Classification.csv')
    # geonames_list = loader.read_csv_into_dictionary('Bengali_Geonames_Classification.csv')
    # print(geonames_list[-1])
    print(f" English class for feature code ADM1 is: %s" % bg.get_english_class_from_feature_code("ADM1"))
    print(f" Bengali class for feature code ADM1 is: %s" % bg.get_bengali_class_from_feature_code("ADM1"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
