import unittest

from tracker import (
    FinanceTracker,
    iter_transactions_by_month,
    calculate_statistics
)

from models import Income, Expense


class TestFinanceTracker(unittest.TestCase):

    def setUp(self):

        self.tracker = FinanceTracker()

        self.tracker.add_transaction(
            Income(1000, "2026-05-01")
        )

        self.tracker.add_transaction(
            Expense(20, "2026-05-01", "food")
        )

        self.tracker.add_transaction(
            Expense(50, "2026-05-02", "transport")
        )

        self.tracker.add_transaction(
            Expense(30, "2026-06-01", "food")
        )

    def test_get_balance(self):

        self.assertEqual(
            self.tracker.get_balance(),
            900
        )

    def test_get_transactions_by_month(self):

        may_transactions = self.tracker.get_transactions_by_month(
            2026,
            5
        )

        self.assertEqual(
            len(may_transactions),
            3
        )

    def test_get_category_breakdown(self):

        breakdown = self.tracker.get_category_breakdown(
            2026,
            5
        )

        self.assertEqual(
            breakdown["food"],
            20
        )

        self.assertEqual(
            breakdown["transport"],
            50
        )

    def test_calculate_statistics(self):

        statistics = calculate_statistics(
            self.tracker.transactions
        )

        self.assertEqual(
            statistics["max_expense"],
            50
        )

        self.assertEqual(
            statistics["total_expenses"],
            100
        )

        self.assertEqual(
            statistics["transaction_count"],
            4
        )

    def test_generator(self):

        generated = list(
            iter_transactions_by_month(
                self.tracker.transactions,
                2026,
                5
            )
        )

        self.assertEqual(
            len(generated),
            3
        )

    def test_empty_balance(self):

        empty_tracker = FinanceTracker()

        self.assertEqual(
            empty_tracker.get_balance(),
            0
        )

    def test_empty_breakdown(self):

        empty_tracker = FinanceTracker()

        self.assertEqual(
            empty_tracker.get_category_breakdown(2026, 5),
            {}
        )

    def test_statistics_no_expenses(self):

        tracker = FinanceTracker()

        tracker.add_transaction(
            Income(1000, "2026-05-01")
        )

        statistics = calculate_statistics(
            tracker.transactions
        )

        self.assertEqual(
            statistics["max_expense"],
            0
        )

        self.assertEqual(
            statistics["total_expenses"],
            0
        )


if __name__ == "__main__":
    unittest.main()