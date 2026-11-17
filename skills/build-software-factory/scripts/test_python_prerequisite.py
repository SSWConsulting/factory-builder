"""Documentation routing for the Python prerequisite and its instructions-only lite option."""
import re
import unittest

from scaffold import ROOT


class PythonPrerequisiteGuidanceTests(unittest.TestCase):
    def setUp(self):
        self.guide = (ROOT / 'references/python-prerequisite.md').read_text(encoding='utf-8')

    def test_setup_entrypoints_link_to_the_prerequisite_guide(self):
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        discover = skill.split('## 1. Discover', 1)[1].split('## 2.', 1)[0]
        self.assertIn('(references/python-prerequisite.md)', discover)
        scaffolding = (ROOT / 'references/scaffolding.md').read_text(encoding='utf-8')
        self.assertIn('(python-prerequisite.md)', scaffolding)
        for target in re.findall(r'`<skill-dir>/(scripts/[^`\s]+)', self.guide):
            self.assertTrue((ROOT / target).is_file(), target)

    def test_install_needs_explicit_approval_and_check_precedes_research(self):
        self.assertIn('3.9', self.guide)
        self.assertIn('before the interview', self.guide)
        self.assertIn('Stop before research and scaffolding', self.guide)
        self.assertIn('only after the user explicitly approves that exact command', self.guide)
        self.assertIn('does not authorize installing software', self.guide)

    def test_lite_option_is_instructions_only_and_never_evidence(self):
        lite = self.guide.split('## Lite option', 1)[1]
        for phrase in ('explicitly choose', 'It is not a factory',
                       'Do not create `.software-factory/`', 'improvised substitute',
                       'NOT RUN', 'Nothing is PASSED by a gate',
                       'never readiness, merge or deploy authority', 'not factory evidence',
                       'not imported as evidence'):
            self.assertIn(phrase, lite)


if __name__ == '__main__':
    unittest.main()
