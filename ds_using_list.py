shop_list = ['apple', 'mango','banana']

print('I have',len(shop_list),'items')

print('These items are:', end=' ' )
for items in shop_list:
    print(items, end=' ')

print('items', shop_list)

print('adding rice')

shop_list.append('rice')

print('updated: ',shop_list)

print('Sorting list')
shop_list.sort()

print('sorted list',shop_list)

print('buying first item', shop_list[0])

olditem = shop_list[0]

del shop_list[0]

print('item bought', olditem)

print('remaining items', shop_list)

