import TextManager.Box as B_o_x
import TextManager.FileProcessing as Fp


class TextPreparer:

    file_dict = Fp.FileProcessing().get_data_from_xml()

    # box - description with answers
    # description - Main text
    # answers - options to take by player
    def __init__(self):
        # print(self.file_dict["Quest"])
        print("Hi")

    def create_box_list(self):
        result = []
        for x in self.file_dict['Quest']['box']:
            temp = B_o_x.Box(x)
            result.append(temp)

        return result
