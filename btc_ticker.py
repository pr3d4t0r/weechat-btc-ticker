#!/usr/bin/env python
# coding=utf-8

# Copyright (c) 2014, Eugene Ciurana (pr3d4t0r)
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
# 
# * Neither the name of the {organization} nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Main repository, version history:  https://github.com/pr3d4t0r/weechat-btc-ticker


import        urllib2
import        json

import        weechat


# *** Symbolic constants ***

BTC_URI = 'https://btc-e.com/api/2/btc_usd/ticker'
LTC_URI = 'https://btc-e.com/api/2/ltc_usd/ticker'


# *** Functions ***

def fetchJSONTickerFrom(locator):
    return urllib2.urlopen(locator).read()


def extractRelevantInfoFrom(rawTicker):
    payload = json.loads(rawTicker)
    result  = dict()

    result['avg']  = float(payload['ticker']['avg'])
    result['buy']  = float(payload['ticker']['buy'])
    result['high'] = float(payload['ticker']['high'])
    result['last'] = float(payload['ticker']['last'])
    result['low']  = float(payload['ticker']['low'])
    result['sell'] = float(payload['ticker']['sell'])

    return result


def display(buffer, ticker, currencyLabel):
    output = ('%s:USD sell = %4.2f, buy = %4.2f, last = %4.2f; high = %4.2f, low = %4.2f, avg = %4.2f  ||  via BTC-e' % \
                    (currencyLabel, \
                    ticker['sell'], ticker['buy'], ticker['last'], \
                    ticker['high'], ticker['low'], ticker['avg']))

    weechat.command(buffer, '/say %s' % output)


def displayCurrentTicker(buffer, currencyLabel, locator):
    rawTicker = fetchJSONTickerFrom(locator)
    
    if rawTicker is not None:
        ticker = extractRelevantInfoFrom(rawTicker)
        display(buffer, ticker, currencyLabel)
    else:
        weechat.prnt(buffer, '*** UNABLE TO READ DATA FROM:  %s ***' % locator)


def displayBTCTicker(data, buffer, arguments):
    displayCurrentTicker(buffer, 'BTC', BTC_URI)

    return weechat.WEECHAT_RC_OK


def displayLTCTicker(data, buffer, arguments):
    displayCurrentTicker(buffer, 'LTC', LTC_URI)

    return weechat.WEECHAT_RC_OK


# *** main ***

weechat.register('btc_ticker', 'pr3d4t0r', '1.0-beta', 'BSD', 'Display a crypto currency ticker (BTC, LTC) in the active buffer', '', 'UTF-8')

weechat.hook_command('btc', 'Display Bitcoin ticker values in USD', '', '', '', 'displayBTCTicker', '')
weechat.hook_command('ltc', 'Display LiteCoin ticker values in USD', '', '', '', 'displayLTCTicker', '')

