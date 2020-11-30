from functools import total_ordering
from my_parser import Parser


@total_ordering
class Version:
    def __init__(self, version):
        self.split_version = Parser().parse(version)


    def __eq__(self, other):
        return self.split_version == other.split_version
    

    def __lt__(self, other):
        for i, j in zip(self.split_version, other.split_version):
            if i == j:
                continue
            if i < j:
                return True
            else:
                return False 
        return False   
