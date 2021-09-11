
class Item:
    def __init__(self, name, collectable, collectableDesc, trigger = '', notCollectableDesc = ''):
        self.name = name
        self.collectable = collectable
        self.collectableDesc = collectableDesc
        self.trigger = trigger
        self.notCollectableDesc = notCollectableDesc


    def getDescription(self):
        if self.collectable:
            return self.collectableDesc
        else:
            return self.notCollectableDesc
