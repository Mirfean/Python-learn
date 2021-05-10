import xmltodict
from pathlib import Path


class FileProcessing:
    file_name = "Quest01.xml"
    p = Path(__file__).with_name(file_name)

    def __init__(self):
        print("xD")

    def get_data_from_xml(self):

        # text_from_file = open((os.path.join(sys.path[0], self.file_name)), "r", )

        with self.p.open('r', encoding="utf-8") as text_from_file:
            my_dict = xmltodict.parse(text_from_file.read())  # converting the xml data to Python dictionary
            text_from_file.close()  # closing the file
        # print("I created " + str(my_dict) + " from xml")
        return my_dict
