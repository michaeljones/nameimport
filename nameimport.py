"""

    >>> import sys
    >>> hook = NameImportHook()
    >>> sys.meta_path.append(hook)

    >>> import ham
    >>> import spam
    >>> import lumberjack
    >>> import shop.parrot
    >>> import am

"""

import imp
import sys
import os

class Loader(object):

    def __init__(self, file, pathname, description):

        self.file = file
        self.pathname = pathname
        self.description = description

    def load_module(self, module_name):
        """
        """

        # file, pathname, description = imp.find_module(module_name, [self.path])

        return imp.load_module(module_name, self.file, self.pathname, self.description)


class NameImportHook(object):

    def find_module(self, module_name, package_path):
        """
        """

        for entry in sys.path:

            if module_name == "lumber":
                print module_name, entry

            start = module_name.split( "." )[0]

            if start.lower() in entry.lower():

                try:
                    file, pathname, description = imp.find_module(module_name, [entry])
                except ImportError:
                    continue

                return Loader( file, pathname, description )

        return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()

