"""Regression tests for the CLI: an unknown cow exits cleanly (issue #6).

Stdlib unittest only, so the tests run with plain `python3 -m unittest`.
"""

import contextlib
import io
import sys
import unittest

from koezeg.cli import main
from koezeg.cowfile import list_cows


def run_cli(argv):
    """Run koezeg's main with argv; return (exit_code, stdout, stderr)."""
    out, err = io.StringIO(), io.StringIO()
    code = 0
    old_argv, sys.argv = sys.argv, ["koezeg"] + argv
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            main()
    except SystemExit as exc:
        code = exc.code
    finally:
        sys.argv = old_argv
    return code, out.getvalue(), err.getvalue()


class UnknownCow(unittest.TestCase):
    def test_unknown_cow_exits_1_with_a_friendly_message(self):
        code, out, err = run_cli(["-f", "paard", "Hallo"])

        self.assertEqual(code, 1)
        self.assertEqual(out, "")
        self.assertIn("Onbekende koe: paard", err)
        for cow in list_cows():
            self.assertIn(cow, err)

    def test_unknown_cow_message_has_no_traceback(self):
        code, out, err = run_cli(["-f", "paard", "Hallo"])

        self.assertNotIn("Traceback", err)
        self.assertNotIn("FileNotFoundError", err)

    def test_known_cow_still_renders(self):
        code, out, err = run_cli(["-f", list_cows()[0], "Hallo"])

        self.assertEqual(code, 0)
        self.assertIn("Hallo", out)


if __name__ == "__main__":
    unittest.main()
