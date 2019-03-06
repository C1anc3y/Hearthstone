#!/usr/bin/env python
# encoding: utf-8
"""
@File: tests.py
@Author: ClanceyHuang
@Time: 19-3-6 上午9:35
@Desc:  ...
@Version: Python3
"""
import logging
import os
import unittest

import core

logging.getLogger('scrapy').propagate = True
logging.getLogger('requests').propagate = True


class Tests(unittest.TestCase):
    def setUp(self):
        if core.core.MAIN_LANGUAGE != 'zhCN':
            core.set_main_language('zhCN')

    @staticmethod
    def remove_if_exists(path):
        if os.path.exists(path):
            os.remove(path)

    def test_career(self):
        career = core.Career('MAGE')
        self.assertEqual(career.name, '法师')
        self.assertEqual(career.__repr__(), '<Career: 法师 (MAGE)>')

        core.set_main_language('enUS')
        career = core.Career('MAGE')
        self.assertEqual(career.name, 'Mage')

    def test_careers(self):
        self.assertEqual(len(core.CAREERS), 11)
        self.assertEqual(core.CAREERS.get('HUNTER').name, '猎人')

        core.Cards()
        self.assertEqual(core.CAREERS.search('雷 萨').name, '猎人')
        self.assertEqual(core.CAREERS.search('迪，麦 文').name, '法师')

        core.set_main_language('enUS')
        core.Cards()
        self.assertEqual(core.CAREERS.search('Rexxar').name, 'Hunter')

    def test_card(self):
        card = core.Cards().get('OG_134')
        self.assertEqual(card.name, '尤格-萨隆')
        self.assertEqual(card.career.name, '中立')

    def test_cards(self):
        cards = core.Cards()
        found = cards.search('萨隆', '每 施放', return_first=False)
        self.assertEqual(len(found), 1)
        card = cards.get(found[0].id)
        self.assertEqual(found[0], card)
        self.assertEqual(cards.search(in_text='在你召唤一个随从后 随机 敌方 伤害').name, '飞刀杂耍者')
        self.assertIsNone(cards.search('关门放狗', career='mage'))
        self.assertIsInstance(cards.search('海盗', return_first=False), list)

    def test_cards_update(self):
        test_path = 'p_cards_update_test.json'

        self.remove_if_exists(test_path)

        try:
            cards = core.Cards(test_path)
            cards.update(hs_version_code=14366)
        finally:
            self.remove_if_exists(test_path)

        self.assertEqual(cards.search('兽群 呼唤', '三种').cost, 8)

    def test_deck(self):
        decks = core.HSBoxDecks()
        deck = decks[10]
        self.assertIsInstance(deck.career, core.Career)
        self.assertIsInstance(list(deck.cards.keys())[0], core.Card)
        self.assertEqual(len(list(deck.cards.elements())), 30)

    def test_hsbox_decks(self):

        test_path = 'p_hsbox_decks_test.json'
        self.remove_if_exists(test_path)

        try:
            updated_decks = core.HSBoxDecks(json_path=test_path)
            updated_deck = updated_decks[100]
            loaded_decks = core.HSBoxDecks(json_path=test_path)
            loaded_deck = loaded_decks.get(updated_deck.id)
        finally:
            self.remove_if_exists(test_path)

        self.assertEqual(len(updated_decks), len(loaded_decks))
        self.assertEqual(updated_deck.cards, loaded_deck.cards)

        self.assertIsNotNone(loaded_decks.source)
        self.assertIsNotNone(loaded_deck.source)

        self.assertTrue(
            updated_decks.source ==
            updated_deck.source ==
            loaded_decks.source ==
            loaded_deck.source
        )

        self.assertIs(loaded_decks.get(loaded_deck.id), loaded_deck)

        found = loaded_decks.search('萨满', core.MODE_STANDARD, 0.5, 10000, 5)
        self.assertLessEqual(len(found), 5)
        last_win_rate = 1
        for deck in found:
            self.assertEqual(deck.career, core.CAREERS.get('SHAMAN'))
            self.assertEqual(deck.mode, core.MODE_STANDARD)
            self.assertGreaterEqual(deck.win_rate, 0.5)
            self.assertGreaterEqual(deck.games, 10000)
            self.assertLessEqual(deck.win_rate, last_win_rate)
            last_win_rate = deck.win_rate

    def test_can_have(self):
        cards = core.Cards()

        self.assertTrue(core.can_have('萨满', cards.search('叫嚣的中士')))
        self.assertTrue(core.CAREERS.search('萨满').can_have(cards.search('叫嚣的中士')))
        self.assertTrue(core.can_have('猎人', cards.search('关门放狗')))
        self.assertTrue(core.CAREERS.search('猎人').can_have(cards.search('关门放狗')))

        self.assertFalse(core.can_have('萨满', cards.search('关门放狗')))
        self.assertFalse(core.CAREERS.search('萨满').can_have(cards.search('关门放狗')))
        self.assertFalse(core.can_have('猎人', cards.search('玉莲帮密探')))
        self.assertFalse(core.CAREERS.search('猎人').can_have(cards.search('玉莲帮密探')))


if __name__ == '__main__':
    unittest.main()
