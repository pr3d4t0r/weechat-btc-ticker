WeeChat Crypto Currency Ticker
==============================
WeeChat plugin for Bitcoin, Litecoin, other cyrptocurrency ticker reporting.


Installation and Use
--------------------
* Copy the `btc_ticker.py` file to `$HOME/.weechat/python/autoload`
* Re-start WeeChat
* Type /btc in any buffered window


Supported Commands
------------------
```/tick [ btc|ltc|nmc [usd|eur|rur] ]```

Where:
* btc = Bitcion
* ltc = Litecoin
* nmc = Namecoin  _experimental - may not always work_

and:

* usd = US dollar
* eur = euro
* rur = Russian ruble

TODO
----
Deciding how to report the ticker's time stamp.  UTC seems to be the ideal format,
no decision has been made yet.

