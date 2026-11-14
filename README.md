# Bitcoin Strategy Desk
Read-only Bitcoin SMA125 daily monitoring dashboard.

- 60% 1x spot / 40% 3x leveraged research strategy
- Daily completed UTC candle entry: fresh upward close/SMA125 crossover with <=1 cross in the preceding 30 completed daily candles
- Exit: completed daily close below SMA125; execution on next daily open
- Refresh live: Kraken current daily candle; provisional only
- Scheduled GitHub Actions snapshots at 00:20 and 12:20 UTC
- No order execution or account access

## Hosting
GitHub Pages: Settings → Pages → Deploy from branch → main / root. This may require one-time configuration if Pages is not already enabled. The repository index.html works as a static site.

## Limitations
Kraken provides a rolling daily OHLC window (~720 candles). History displayed is limited accordingly. The dashboard shows theoretical signals, not actual broker positions, fills or returns. No auto-trading.
