#====================================================================
#
#           author :Shinnosuke Yamazaki@TokyoUnivOfScience
#           date   :2021/06/15
#           adress :*private*
#
#====================================================================

import json
import re
import pprint

class reversePcdList():
    FILE_NUMBER=0
    pcd_dict={}
    rev_dict={}

    def __init__(self):
        self.make_reverse_list()

    def input_json_files(self):
        pcds = []
        json_files = []
        for i in range(5):
            json_files.append(open("./modelnet40_ply_hdf5_2048/ply_data_test_" + str(self.FILE_NUMBER) + "_id2file.json", 'r'))
            pcds.append(json.load(json_files[i]))
        return pcds

    def make_reverse_list(self):
        pcd_prev = self.input_json_files()[self.FILE_NUMBER]
        pcd_prev = list(pcd_prev)
        pprev_id = list(range(len(pcd_prev)))
        pcd_prev = [re.sub('/.*ply','', s ) for s in pcd_prev]
        self.pcd_dict = dict(zip(pprev_id, pcd_prev))

        # rev_keys = sorted(set(list(d.values())))
        # pprint.pprint(rev_keys)
        for i in self.pcd_dict.keys():
            if(self.pcd_dict[i] not in self.rev_dict):
                self.rev_dict[self.pcd_dict[i]] = []
            self.rev_dict[self.pcd_dict[i]].append(i)
        # return self.rev_dict

    def print_model_list(self):
        pprint.pprint(sorted(set(list(self.pcd_dict.values()))))

    def print_pcd_dict(self):
        print("---PCD("+"./modelnet40_ply_hdf5_2048/ply_data_test_" + str(self.FILE_NUMBER) + "_id2file.json"+")---")
        pprint.pprint(self.pcd_dict,depth=40,width = 3000)

    def print_rev_dict(self):
        print("---PCD("+"./modelnet40_ply_hdf5_2048/ply_data_test_" + str(self.FILE_NUMBER) + "_id2file.json"+")---")
        pprint.pprint(self.rev_dict,depth=40,width = 3000)




# if __name__ == "__main__":
#     a = reversePcdList()
#     a.print_rev_dict()
