
from nameimport import NameImportHook

import sys
hook = NameImportHook()
sys.meta_path.append(hook)

import mini
import ham
import spam
import ministry
import shop.parrot

