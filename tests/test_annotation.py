import unittest
from src.annotation import validate,agreement,adjudicate
class AnnotationTests(unittest.TestCase):
 def test_invalid(self):self.assertIn('missing id',validate({'text':'hi'}))
 def test_agreement(self):self.assertEqual(agreement([{'rater_a':{'factuality':'supported'},'rater_b':{'factuality':'supported'}}])['agreement'],1.0)
 def test_adjudication(self):self.assertEqual(adjudicate({'rater_a':{'factuality':'supported'},'rater_b':{'factuality':'unsupported'}}),'needs_adjudication')
if __name__=='__main__':unittest.main()
