import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the las AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        question = "What language did you learn 1st?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_triple_response(self):
        """Test that a single response is stored properly"""
        question = "What language did you learn 1st?"
        my_survey = AnonymousSurvey(question)
        responses = ['german', 'swedish', 'polish', 'english']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
         self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()