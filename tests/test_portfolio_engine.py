import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from portfolio_engine import (
    downside_deviation,
    historical_crisis_simulations,
    load_prices,
    mandate_audit,
    marginal_risk_contributions,
    metrics,
    one_way_turnover,
    optimize,
    portfolio_return_series,
    rebalancing_trade_blotter,
    sortino_ratio,
    statistics,
    tangency_portfolio,
)


class PortfolioEngineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_prices(Path(__file__).resolve().parents[1] / "prices.csv")
        cls.returns, cls.vols, cls.cov, _, cls.ret_dict = statistics(cls.rows)

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

    def test_downside_deviation_and_sortino(self):
        series = [0.01, -0.02, 0.03, -0.01, 0.02, 0.0]
        dd = downside_deviation(series, mar=0.0)
        self.assertGreater(dd, 0.0)
        sortino = sortino_ratio(series, risk_free=0.01, mar=0.0)
        self.assertIsInstance(sortino, float)

    def test_rebalancing_trade_blotter(self):
        curr = {"SGOV": 0.40, "RXI": 0.60, "PEJ": 0.0}
        targ = {"SGOV": 0.55, "RXI": 0.0, "PEJ": 0.45}
        blotter = rebalancing_trade_blotter(curr, targ, 100_000_000.0)
        self.assertEqual(len(blotter), 3)
        sgov_trade = next(b for b in blotter if b["Asset"] == "SGOV")
        rxi_trade = next(b for b in blotter if b["Asset"] == "RXI")
        pej_trade = next(b for b in blotter if b["Asset"] == "PEJ")
        self.assertEqual(sgov_trade["Net Trade ($)"], 15_000_000.0)
        self.assertEqual(sgov_trade["Action"], "BUY")
        self.assertEqual(rxi_trade["Net Trade ($)"], -60_000_000.0)
        self.assertEqual(rxi_trade["Action"], "SELL")
        self.assertEqual(pej_trade["Net Trade ($)"], 45_000_000.0)
        self.assertEqual(pej_trade["Action"], "BUY")

    def test_marginal_risk_contributions_sum_to_one(self):
        w = {"SGOV": 0.55, "RXI": 0.0, "PEJ": 0.45}
        rc = marginal_risk_contributions(w, self.cov)
        self.assertAlmostEqual(sum(rc.values()), 1.0, places=2)
        # PEJ should carry practically all risk compared to SGOV
        self.assertGreater(rc["PEJ"], 0.95)

    def test_tangency_portfolio_finds_max_sharpe(self):
        tp = tangency_portfolio(self.returns, self.cov, risk_free=0.0378, cost_drag=0.0015)
        self.assertIn("sharpe", tp)
        self.assertGreater(tp["sharpe"], 0.0)

    def test_historical_crisis_simulations_returns_four_scenarios(self):
        w = {"SGOV": 0.55, "RXI": 0.0, "PEJ": 0.45}
        scenarios = historical_crisis_simulations(w)
        self.assertEqual(len(scenarios), 4)
        for s in scenarios:
            self.assertIn("Crisis Scenario", s)
            self.assertIn("Estimated Strategy Return", s)


if __name__ == "__main__":
    unittest.main()
