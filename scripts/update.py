#!/usr/bin/env python3
"""Fetch Kraken daily BTCUSD candles; preserve latest provisional candle."""
import json,urllib.request,datetime,pathlib
url="https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1440"
req=urllib.request.Request(url,headers={"User-Agent":"BTC-Strategy-Desk/1.0"})
with urllib.request.urlopen(req,timeout=30) as response: payload=json.load(response)
if payload.get("error"): raise RuntimeError(payload["error"])
key=next(k for k in payload["result"] if k!="last")
candles=[dict(t=int(r[0]),o=float(r[1]),h=float(r[2]),l=float(r[3]),c=float(r[4])) for r in payload["result"][key]]
if len(candles)<160: raise RuntimeError("Insufficient daily history")
# Reject missing, duplicate, out-of-order, non-UTC or malformed candles.
for i, c in enumerate(candles):
    if c["t"] <= 0 or c["t"] % 86400:
        raise RuntimeError(f"Invalid UTC daily timestamp at row {i}")
    if i and c["t"] != candles[i-1]["t"] + 86400:
        raise RuntimeError(f"Gap, duplicate or out-of-order daily candle at row {i}")
    if min(c["o"], c["h"], c["l"], c["c"]) <= 0 or c["l"] > min(c["o"], c["c"]) or c["h"] < max(c["o"], c["c"]):
        raise RuntimeError(f"Invalid OHLC at row {i}")
now = datetime.datetime.now(datetime.timezone.utc).timestamp()
if candles[-1]["t"] > now or now - candles[-1]["t"] > 172800:
    raise RuntimeError("Latest daily candle missing or stale")

path=pathlib.Path("data/daily.json");path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps({"updated":datetime.datetime.now(datetime.timezone.utc).isoformat(),"source":"Kraken BTC/USD daily UTC","candles":candles},separators=(",",":"))+"\n")
print("Saved",len(candles),"candles through",datetime.datetime.fromtimestamp(candles[-1]["t"],datetime.timezone.utc))
