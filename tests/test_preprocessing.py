from nbresult import ChallengeResultTestCase


class TestPreprocessing(ChallengeResultTestCase):

    def test_train_test_split_done(self):
        """Created train and test sets"""
        total = self.result.X_train_rows + self.result.X_test_rows
        test_ratio = self.result.X_test_rows / total

        self.assertAlmostEqual(
            test_ratio,
            0.2,
            places=2,
            msg=f"Hint: Test set should be 20%, got {test_ratio:.1%}")

    def test_scaling_applied(self):
        """Applied StandardScaler to features"""
        # Check if X_train is a numpy array (result of fit_transform)
        self.assertEqual(
            self.result.X_train_type,
            'numpy.ndarray',
            "Hint: X_train should be a numpy array after scaling")

    def test_X_train_has_2_dimensions(self):
        """Check X_train has 2 dimensions (not swapped with y_train)"""
        X_train_shape = self.result.X_train_shape if hasattr(
            self.result, 'X_train_shape') else None
        if X_train_shape:
            self.assertEqual(
                len(X_train_shape), 2,
                "Did you accidentally swap X and y in your train_test_split? "
                "X_train should be 2-dimensional (samples, features)"
            )
