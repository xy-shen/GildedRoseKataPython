# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def get_item(self):
        ret = []
        for item in self.items:
            ret.append(item.name)
        return ret
    
    def get_item_by_name(self, name):
        ret = []
        for item in self.items:
            if item.name == name:
                ret.append(item)
        return ret

    def update_quality(self):
        for item in self.items:
            # "Sulfuras" don't need any change
            if "Sulfuras" not in item.name:
                if "Aged Brie" in item.name:
                    item.quality += 1
                elif "Backstage passes" in item.name:
                    if item.sell_in < 0:
                        item.quality = 0
                    elif item.sell_in < 6:
                        item.quality += 3
                    elif item.sell_in < 11:
                        item.quality += 2
                    else:
                        item.quality += 1
                elif "Conjured" in item.name:
                    if item.sell_in < 0:
                        item.quality -= 4
                    else:
                        item.quality -= 2
                else:
                    if item.sell_in < 0:
                        item.quality -= 2
                    else:
                        item.quality -= 1
                item.quality = min(item.quality, 50)
                
            item.quality = max(item.quality, 0)
            item.sell_in = item.sell_in - 1
            
            """
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
            """
