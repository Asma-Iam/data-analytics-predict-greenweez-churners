from nbresult import ChallengeResultTestCase


class TestDataExploration(ChallengeResultTestCase):
    """Test data loading and cleaning"""

    def test_correct_row_count(self):
        """Loaded correct number of unique customers after deduplication"""
        self.assertEqual(
            self.result.df_shape[0],
            172523,
            f"Hint: Expected 172,523 rows (one per unique customer after deduplication), got {self.result.df_shape[0]:,}")

    def test_dropped_irrelevant_columns(self):
        """Removed orders_id and date_date columns"""
        self.assertNotIn(
            'orders_id',
            self.result.cleaned_columns,
            "Hint: orders_id should be removed")
        self.assertNotIn(
            'date_date',
            self.result.cleaned_columns,
            "Hint: date_date should be removed")
        # Ensure core feature columns still exist
        required_columns = ['re_purchase', 'avg_basket']
        for col in required_columns:
            self.assertIn(
                col,
                self.result.cleaned_columns,
                f"Hint: Required column '{col}' should not be removed")

    def test_set_index_to_customers_id(self):
        """Set customers_id as DataFrame index"""
        self.assertEqual(
            self.result.index_name,
            'customers_id',
            f"Hint: Index should be 'customers_id', got '{self.result.index_name}'")
