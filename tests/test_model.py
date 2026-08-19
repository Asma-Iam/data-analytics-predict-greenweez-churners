from nbresult import ChallengeResultTestCase


class TestModel(ChallengeResultTestCase):

    def test_baseline_calculated(self):
        """Calculated baseline accuracy"""
        self.assertIsNotNone(
            self.result.baseline_accuracy,
            "Hint: Should calculate baseline accuracy")
        self.assertGreater(
            self.result.baseline_accuracy,
            0.65,
            f"Hint: Baseline seems too low: {self.result.baseline_accuracy:.1%}. Did you predict the majority class (all churn, predict 0)?")
        self.assertLess(
            self.result.baseline_accuracy,
            0.80,
            f"Hint: Baseline seems too high: {self.result.baseline_accuracy:.1%}")

    def test_model_trained(self):
        """Trained Logistic Regression model"""
        self.assertIsNotNone(
            self.result.model_accuracy,
            "Hint: Should train model and get accuracy")

    def test_model_precision(self):
        """Model achieves meaningful precision on repurchasers"""
        self.assertGreater(
            self.result.precision,
            0.55,
            f"Hint: Model precision for repurchasers seems low: {self.result.precision:.1%}. Did you train the model correctly? Logistic Regression on this dataset should achieve precision above 55%."
        )

    def test_accuracy_not_suspiciously_perfect(self):
        """Check accuracy isn't suspiciously high (might indicate evaluating on training data)"""
        accuracy = self.result.model_accuracy
        self.assertLess(
            accuracy,
            0.99,
            f"Accuracy is suspiciously high ({accuracy:.1%}). Did you accidentally evaluate your model on the training data instead of test data? "
            "For churn prediction, accuracy this high suggests data leakage.")

    def test_accuracy_not_suspiciously_low(self):
        """Check accuracy isn't suspiciously low (might indicate wrong preprocessing)"""
        accuracy = self.result.model_accuracy
        self.assertGreater(
            accuracy,
            0.50,
            f"Accuracy is suspiciously low ({accuracy:.1%}). Did you forget to scale your features or properly encode categorical variables? "
            "Logistic Regression on this dataset should achieve better than random guessing.")
