from functools import total_ordering
from my_parser import Parser


@total_ordering
class Version:
    def __init__(self, version):
        self.major, self. minor, self.patch, self.pre_release_vers = Parser(version).parse()

    def __eq__(self, other):
        return (self.major == other.major
               and self.minor == other.minor 
               and self.patch.patch_int == other.patch.patch_int
               and self.patch.patch_str == other.patch.patch_str 
               and self.pre_release_vers == other.pre_release_vers)
            

    def __lt__(self, other):
        if (self.major < other.major):
            return True
        elif self.major > other.major:
            return False
        elif self.minor < other.minor:
            return True
        elif self.minor > other.minor:
            return False
        elif self.patch.patch_int < other.patch.patch_int:
            return True
        elif self.patch.patch_int > other.patch.patch_int:
            return False
        elif self.patch.patch_str is None and other.patch.patch_str is not None:
            return True
        elif self.patch.patch_str is None  and other.patch.patch_str is None:
            if other.pre_release_vers is None:
                return True
            if self.pre_release_vers is None:
                return False
            if self.pre_release_vers < other.pre_release_vers:
                return True
            else:
                return False
        elif self.patch.patch_str is not None  and other.patch.patch_str is not None:
            if self.patch.patch_str < other.patch.patch_str:
                return True
            else:
                return False
