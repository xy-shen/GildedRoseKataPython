# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_item()
        self.assertEqual(["Sulfuras"], all_items)

    # my tests
    # 1. The Quality of an item is never more than 50
    def test_quality_not_more_than_50(self):
        items = [Item("Aged Brie", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        brie_item = items[0]
        self.assertEqual(50, brie_item.quality)

    # 2. The Quality of an item is never negative
    def test_quality_not_negative(self):
        items = [Item("Sulfuras", 5, -20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(0, sulfuras_item.quality)

    # 3. "Conjured" items degrade in Quality twice as fast as normal items
    def test_conjured_decrease_quality_twice(self):
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        conjured_item = items[0]
        self.assertEqual(4, conjured_item.quality)

    # 4. syntax error
    def test_get_item_by_name(self):
        items = [Item("Elixir of the Mongoose", 5, 7)]
        gilded_rose = GildedRose(items)
        elixir_item = gilded_rose.get_item_by_name("Elixir of the Mongoose")
        self.assertEqual(items, elixir_item)

if __name__ == '__main__':
    unittest.main()