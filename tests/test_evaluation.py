from nbresult import ChallengeResultTestCase


class TestEvaluation(ChallengeResultTestCase):

    def test_metrics_calculated(self):
        """Calculated precision, recall, accuracy"""
        self.assertIsNotNone(
            self.result.precision,
            "Hint: Should calculate precision")
        self.assertIsNotNone(
            self.result.recall,
            "Hint: Should calculate recall")
        self.assertIsNotNone(
            self.result.accuracy,
            "Hint: Should calculate accuracy")

    def test_probabilities_generated(self):
        """Generated prediction probabilities"""
        self.assertGreater(
            self.result.proba_rows,
            0,
            "Hint: Should create probability DataFrame")
        self.assertGreaterEqual(
            self.result.proba_cols,
            2,
            "Hint: Probability DataFrame should have at least 2 columns (binary classification). Extra analysis columns are fine!")

    def test_at_risk_identified(self):
        """Identified at-risk customers (20-50% probability)"""
        self.assertGreater(
            self.result.at_risk_count,
            0,
            "Hint: Should find some at-risk customers")
