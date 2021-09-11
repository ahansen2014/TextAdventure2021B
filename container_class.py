

class Container():
    def __init__(self, name, closedDesc, openDesc, items, trigger, isOpen=False):
        self.name = name
        self.closedDesc = closedDesc
        self.openDesc = openDesc
        self.items = items
        self.trigger = trigger
        self.isOpen = isOpen

    def getDescription(self):
        if self.isOpen == False:
            return self.closedDesc
        else:
            outStr = self.openDesc + '\n'
            if len(self.items) > 0:
                for item in self.items:
                    #outStr += 'There is ' + item.name + ' inside.\n'
                    outStr += item.getDescription() + '\n'
            else:
                outStr += 'The ' + self.name + ' is empty.'

        return outStr

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)