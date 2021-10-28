
import src.load_data as loader

col1 = 'Feature_Designation_Code'
col2 = 'Feature_Designation_Name'
col3 = 'Feature_Designation_Name_in_Bengali'
col4 = 'empty'

def get_bengali_class_from_feature_code(feature_code):
    geonames_list = loader.read_csv_into_dictionary('Bengali_Geonames_Classification.csv')
    for item in geonames_list:
        if item[col1].strip() == feature_code.strip():
            return item[col3]


def get_bengali_class_from_english_feature(feature_name):
    geonames_list = loader.read_csv_into_dictionary('Bengali_Geonames_Classification.csv')
    for item in geonames_list:
        if item[col2].strip() == feature_name.strip():
            return item[col3]


def get_english_class_from_feature_code(feature_code):
    geonames_list = loader.read_csv_into_dictionary('Bengali_Geonames_Classification.csv')
    for item in geonames_list:
        if item[col1].strip() == feature_code.strip():
            return item[col2]
