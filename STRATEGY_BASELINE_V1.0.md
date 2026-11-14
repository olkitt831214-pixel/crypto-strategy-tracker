# BTC SMA125 V1.0 — Locked Strategy Baseline

Status: **Locked specification** (14 November 2026). No modification without explicit user approval.

## Trading rules
- Instrument: BTC/USD, daily UTC candles, long only.
- SMA125: simple average of the latest 125 **completed** daily closes.
- Entry signal: completed daily close moves from at/below SMA125 on the prior completed candle to above SMA125 on the signal candle.
- Lookback: count changes in the close-vs-SMA125 side over the **30 completed daily candles preceding the signal candle**, excluding the signal candle. Accept only if count <= 1. Reject otherwise; do not defer an entry.
- Entry execution: next daily candle open after a qualifying signal.
- Exit signal: completed daily close below SMA125. Exit at next daily candle open.
- No ADX condition, SMA15 filter, profit-taking, fixed stop, or discretionary overrides.
- Allocate starting equity 60% to 1x spot and 40% to 3x leveraged sleeve. Track sleeve equity separately; no periodic rebalancing. Reinvest each sleeve's proceeds into its next eligible entry.
- Liquidation research assumption for 3x sleeve: BTC falls 32.333% from its entry; simulated residual margin 3%. Intraday low checked. This is **not** a broker-verified liquidation model.
- Read-only monitoring only; never place orders.

## Backtest reference (preliminary, not independently audited)
- Historical evaluation: 2018-01-01 through 2026-11-13, initialized flat with GBP 2,300 (GBP 1,380 1x / GBP 920 3x).
- Source: https://github.com/daniegitx1/btc-price-history/blob/main/data/btc_usd_daily.csv
- Previously reported strategy ending equity: GBP 578,193.22; buy-and-hold GBP 11,305.44.
- These figures exclude spread, fees, slippage, financing, taxes, and exchange-specific liquidation mechanics. Do not present as validated real-world performance.

## Live dashboard
- Repository: https://github.com/olkitt831214-pixel/crypto-strategy-tracker
- Monitor source: Kraken public daily BTC/USD OHLC (different from historical backtest dataset); compare timestamp/price definitions before claiming exact backtest/live consistency.
- Provisional current daily candle is informational only. Only completed candles can generate confirmed signals.
- Strategy changes require a new named version and user approval; V1.0 remains unchanged.
