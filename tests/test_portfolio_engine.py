import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from portfolio_engine import one_way_turnover, load_prices, mandate_audit, metrics, optimize, statistics


class PortfolioEngineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_prices(Path(__file__).resolve().parents[1] / "prices.csv")
        cls.returns, cls.vols, cls.cov, _, _ = statistics(cls.rows)

    def test_statistics_have_expected_assets(self):
        self.assertEqual(set(self.returns), {"SGOV", "RXI", "PEJ"})
        self.assertGreater(self.vols["PEJ"], self.vols["SGOV"])

    def test_cost_drag_is_in_net_return(self):
        weights = {"SGOV": 0.5, "RXI": 0.0, "PEJ": 0.5}
        result = metrics(weights, self.returns, self.cov, 0.0015)
        self.assertAlmostEqual(result["gross_return"] - result["net_return"], 0.0015)

    def test_turnover_is_one_way(self):
        self.assertAlmostEqual(one_way_turnover({"SGOV": .4, "RXI": .6, "PEJ": 0}, {"SGOV": .5, "RXI": 0, "PEJ": .5}), .6)

    def test_optimizer_respects_net_hurdle(self):
        weights = optimize(self.returns, self.cov, .0503, .03, .0015)
        self.assertIsNotNone(weights)
        self.assertGreaterEqual(metrics(weights, self.returns, self.cov, .0015)["net_return"], .0503)


if __name__ == "__main__":
    unittest.main()
