from string import digits


class Parser:
    def parse(self, vers):
        # ['major', 'minor', 'patch_int', 'patch_str', 'pre_release_vers']
        split_version = [
            0,
            0,
            0,
            "",
            "",
        ]

        version_without_metadata = vers.split("+")
        vers = version_without_metadata[0].split(".", maxsplit=2)

        split_version[0] = int(vers[0])
        try:
            split_version[1] = int(vers[1])
        except IndexError:
            split_version[1] = 0
        try:
            split_version[4] = vers[2].split("-", maxsplit=1)[1]
        except IndexError:
            split_version[4] = "z"
        try:
            patch = vers[2].split("-", maxsplit=1)[0]
        except IndexError:
            return split_version

        if patch.isdigit():
            split_version[2] = int(patch)
        else:
            index = 0
            for ind, val in enumerate(patch):
                if val not in digits:
                    index = ind
                    break
            split_version[2] = int(patch[:index])
            split_version[3] = patch[index:]

        return split_version
