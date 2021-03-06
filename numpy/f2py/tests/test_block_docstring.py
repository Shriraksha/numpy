from __future__ import division, absolute_import, print_function

import textwrap
from . import util

from numpy.testing import run_module_suite, assert_equal

class TestBlockDocString(util.F2PyTest):
    code = """
      SUBROUTINE FOO()
      INTEGER BAR(2, 3)
      
      COMMON  /BLOCK/ BAR
      RETURN
      END
    """

    def test_block_docstring(self):
        expected = "'i'-array(2,3)\n"
        assert_equal(self.module.block.__doc__, expected)

if __name__ == "__main__":
    run_module_suite()
