import configparser
import sys
import os
import zipfile
import time


def get_configuration_file():
    config = configparser.ConfigParser()

    # sandbox_configuration_path = sys.path[0] + '\configurationFile.ini'
    live_configuration_path = sys.executable.replace("AutoUnzipTool.exe","configurationFile.ini")

    # config.read(sandbox_configuration_path)
    config.read(live_configuration_path)

    default_setting = config["DEFAULT"]

    zip_file_location = default_setting["zip_file_location"]
    file_extension = default_setting["file_extension"]

    return zip_file_location, file_extension


def get_zip_directory(zip_location, file_extension):
    # for file in os.listdir(zip_location):
    #     print(f"Searching for files in {os.path.join(zip_location, file)}")
    zip_file_list = []

    for dir_path, dir_names, file_names in os.walk(zip_location):
        for file_name in [f for f in file_names if f.endswith(file_extension)]:
            # print(os.path.join(dir_path, file_name))
            zip_file_list.append(os.path.join(dir_path, file_name))
    return zip_file_list


def start_unzipping_files(zip_files):
    for zip_file in zip_files:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(zip_file))
            print(f"Successfully extracted at {os.path.dirname(zip_file)}")


def main():
    try:
        zip_location, file_extension = get_configuration_file()
        zip_list_of_files = get_zip_directory(zip_location, file_extension)

        # for zip_file in zip_list_of_files:
        #     print(f"{zip_file}, {os.path.dirname(zip_file)}")

        start_unzipping_files(zip_list_of_files)
        time.sleep(5)

    except Exception as e:
        print(f"Error: {e}")


main()
