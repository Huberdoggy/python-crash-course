import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in ALL test methods
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Spanish", "Mandarin"]

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that 3 individual responses are stored properly
        using 'setUp(), we can eliminate the need to instantiate an instance here (and also the above method
        for single response tests, because the variables are already defined in 'self'
        '"""
        for response in self.responses:
            self.my_survey.store_response(response)
        # Now, run a second loop to assert that each string does, in fact, exist in the list
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()
