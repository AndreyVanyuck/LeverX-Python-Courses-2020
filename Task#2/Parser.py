from string import digits
from collections import namedtuple


class Parser:
    def __init__(self, version):
        self.version = version

    def parse(self):
        version_without_metadata = self.version.split('+')
        vers = version_without_metadata[0].split('.', maxsplit=2)    
        major = int(vers[0])
        minor = int(vers[1])

        Patch = namedtuple('Patch',['patch_int', 'patch_str']) 
        patch = vers[2].split("-", maxsplit=1)[0]
        if (patch.isdigit()):
            patch = Patch(int(patch), None)
        else:
            index = 0
            for ind, val in enumerate(patch):
                if (val not in digits):
                    index = ind
                    break
            patch_int = int(patch[:index])
            patch_str = patch[index:]
            patch = Patch(patch_int, patch_str)
                    
        try:
            pre_release_vers = vers[2].split("-", maxsplit=1)[1]
        except IndexError:
            pre_release_vers = None
        return major, minor, patch, pre_release_vers