import yfiannce as yf
import mplfinance as mpl
import mljar-mercury as mlj

ticker = "TSLA"

history = yf.ticker(ticker).history(period="3mo")

print(f"3 Month low" {history.low.min().astype(int)})

history.tail()

mpf.plot(history, type='candle', mav = (7), figratio = (18,10))
