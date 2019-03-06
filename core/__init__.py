#!/usr/bin/env python
# encoding: utf-8
"""
@File: __init__.py
@Author: ClanceyHuang
@Time: 19-3-6 上午9:08
@Desc: 快速收集和分析炉石传说的卡牌及卡组数据
@Version: Python3
----
GitHub: https://github.com/ClanceyHuang/Hearthstone
----
:copyright: (c) 2016 by ClanceyHuang.
:license: Apache 2.0, see LICENSE for more details.
"""

import logging

from .core import (
    Career, Careers, Card, Cards, Deck, Decks,
    MODE_STANDARD, MODE_WILD, CAREERS, CARDS,
    set_data_dir, set_main_language, get_career, can_have, days_ago
)
from .hearthstats import HearthStatsDeck, HearthStatsDecks
from .hsbox import HSBoxDeck, HSBoxDecks
from .utils import (
    DeckGenerator,
    diff_decks, decks_expired, get_all_decks,
    cards_value, print_cards, cards_to_csv
)

logging.getLogger('scrapy').propagate = False
logging.getLogger('requests').propagate = False
logging.basicConfig(level=logging.INFO)

__title__ = 'hsdata'
__version__ = '0.0.1'
__author__ = 'ClanceyHuang'
__license__ = 'MIT'
__copyright__ = 'Copyright 2019 ClanceyHuang'
