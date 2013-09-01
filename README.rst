
Name Based Import Hook
----------------------

This is a quick prototype of an idea to speed up Python imports by providing a
hook which when looking for a module called "bob", for example, will first look
in any directories on the sys.path which have the string "bob" in their full
path.

It is a hack but a vaguely fun one. Needless to say it does not provide optimal
performance improvements.

