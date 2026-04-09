"""Tests for the frontmatter parser."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.lib import frontmatter


class TestParseScalars(unittest.TestCase):
    def test_unquoted_scalar(self):
        r = frontmatter.parse("---\ntype: note\n---\nbody")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["type"], "note")

    def test_double_quoted_scalar(self):
        r = frontmatter.parse('---\ndescription: "hello world"\n---\n')
        self.assertTrue(r.ok)
        self.assertEqual(r.data["description"], "hello world")

    def test_single_quoted_scalar(self):
        r = frontmatter.parse("---\ndescription: 'hello world'\n---\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["description"], "hello world")

    def test_empty_value(self):
        r = frontmatter.parse("---\ndescription:\n---\n")
        self.assertTrue(r.ok)
        self.assertIsNone(r.data["description"])

    def test_empty_quoted_value(self):
        r = frontmatter.parse('---\ndescription: ""\n---\n')
        self.assertTrue(r.ok)
        self.assertEqual(r.data["description"], "")

    def test_bool_true(self):
        r = frontmatter.parse("---\nuser-invocable: true\n---\n")
        self.assertTrue(r.ok)
        self.assertIs(r.data["user-invocable"], True)

    def test_bool_false(self):
        r = frontmatter.parse("---\nuser-invocable: false\n---\n")
        self.assertTrue(r.ok)
        self.assertIs(r.data["user-invocable"], False)

    def test_integer(self):
        r = frontmatter.parse("---\npost_count: 14\n---\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["post_count"], 14)

    def test_url_stays_string(self):
        r = frontmatter.parse("---\nsource: https://example.com/foo\n---\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["source"], "https://example.com/foo")

    def test_description_with_dashes_and_parens(self):
        desc = "Agile's 'changing requirements' hide two phenomena — genuine change (world moved) and late discovery"
        r = frontmatter.parse(f'---\ndescription: "{desc}"\n---\n')
        self.assertTrue(r.ok)
        self.assertEqual(r.data["description"], desc)


class TestParseInlineLists(unittest.TestCase):
    def test_simple_list(self):
        r = frontmatter.parse("---\ntags: [a, b, c]\n---\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["tags"], ["a", "b", "c"])

    def test_empty_list(self):
        r = frontmatter.parse("---\ntags: []\n---\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["tags"], [])

    def test_single_item(self):
        r = frontmatter.parse("---\ntags: [architecture]\n---\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["tags"], ["architecture"])

    def test_quoted_items(self):
        r = frontmatter.parse('---\ntags: ["a b", \'c d\']\n---\n')
        self.assertTrue(r.ok)
        self.assertEqual(r.data["tags"], ["a b", "c d"])

    def test_quoted_item_may_contain_comma(self):
        r = frontmatter.parse('---\ntags: ["a,b", c]\n---\n')
        self.assertTrue(r.ok)
        self.assertEqual(r.data["tags"], ["a,b", "c"])


class TestParseMultipleFields(unittest.TestCase):
    def test_typical_note(self):
        content = '---\ndescription: "Some description here"\ntype: note\ntags: [kb-design, architecture]\nstatus: seedling\n---\n# Title\n'
        r = frontmatter.parse(content)
        self.assertTrue(r.ok)
        self.assertEqual(r.data["description"], "Some description here")
        self.assertEqual(r.data["type"], "note")
        self.assertEqual(r.data["tags"], ["kb-design", "architecture"])
        self.assertEqual(r.data["status"], "seedling")


class TestDuplicateKeys(unittest.TestCase):
    def test_duplicate_key_keeps_last(self):
        r = frontmatter.parse("---\ntype: note\ntype: adr\n---\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data.get("type"), "adr")


class TestMalformedLines(unittest.TestCase):
    def test_bad_line_reports_error(self):
        r = frontmatter.parse("---\nnot a valid line\ntype: note\n---\n")
        self.assertFalse(r.ok)
        self.assertEqual(r.data, {})

    def test_uppercase_key_is_accepted(self):
        r = frontmatter.parse("---\nType: note\n---\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["Type"], "note")

    def test_mapping_like_scalar_is_accepted(self):
        r = frontmatter.parse("---\nmeta: {a: b}\n---\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["meta"], {"a": "b"})

    def test_yaml_tag_is_accepted(self):
        r = frontmatter.parse("---\nvalue: !!str hello\n---\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["value"], "hello")

    def test_anchor_is_accepted(self):
        r = frontmatter.parse("---\nvalue: &x hello\n---\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["value"], "hello")

    def test_block_list_is_accepted(self):
        r = frontmatter.parse("---\ntags:\n  - a\n  - b\n---\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["tags"], ["a", "b"])

    def test_nested_mapping_is_accepted(self):
        r = frontmatter.parse("---\nmeta:\n  a: b\n---\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["meta"], {"a": "b"})


class TestNoFrontmatter(unittest.TestCase):
    def test_no_delimiters(self):
        r = frontmatter.parse("# Just a heading\nSome text.\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data, {})

    def test_empty_frontmatter(self):
        r = frontmatter.parse("---\n\n---\n# Title\n")
        self.assertTrue(r.ok)
        self.assertEqual(r.data, {})

    def test_closing_delimiter_without_trailing_newline_still_parses(self):
        r = frontmatter.parse("---\ndescription: test\n---")
        self.assertTrue(r.ok)
        self.assertEqual(r.data["description"], "test")

    def test_unclosed_frontmatter_is_error(self):
        r = frontmatter.parse("---\ndescription: test\n# Title\n")
        self.assertFalse(r.ok)
        self.assertEqual(r.errors, ["frontmatter: missing closing delimiter"])


class TestStrip(unittest.TestCase):
    def test_removes_frontmatter(self):
        content = "---\ntype: note\n---\n# Title\nBody."
        self.assertEqual(frontmatter.strip(content), "# Title\nBody.")

    def test_noop_without_frontmatter(self):
        content = "# Title\nBody."
        self.assertEqual(frontmatter.strip(content), content)


if __name__ == "__main__":
    unittest.main()
