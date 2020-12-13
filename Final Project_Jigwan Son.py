#Jigwan Son 1669959
import csv

print("[ID] [Manufacturer] [Type] [Price] [Service Date] [Damaged Item]")

with open('/Users/sjk57/PycharmProjects/CIS2348/FullInventory.csv') as file:
    readCSV = csv.reader(file, delimiter=',')
    for row in readCSV:
        print(row)

with open('/Users/sjk57/PycharmProjects/CIS2348/PastServiceDateInventory.csv') as file:
    readCSV = csv.reader(file, delimiter=',')
    for row in readCSV:
        print(row,'Expired Item(No longer service available)')

class AllInventory:
    def __init__(sjk, Inventories):
        sjk.Inventories = Inventories

    def FI(sjk):
        with open('/Users/sjk57/PycharmProjects/CIS2348/FullInventory.csv', 'w') as file:
            items = sjk.Inventories
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
            for item in keys:
                id = item
                mf_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id,mf_name,item_type,price,service_date,damaged))

    def by_type(sjk):
        items = sjk.Inventories
        types = []
        keys = sorted(items.keys())
        for item in items:
            item_type = items[item]['item_type']
            if item_type not in types:
                types.append(item_type)
        for type in types:
            file_name = type.capitalize() + 'FullInventory.csv'
            with open('/Users/sjk57/PycharmProjects/CIS2348/'+file_name, 'w') as file:
                for item in keys:
                    id = item
                    mf_name = items[item]['manufacturer']
                    price = items[item]['price']
                    service_date = items[item]['service_date']
                    item_type = items[item]['item_type']
                    if type == item_type:
                        file.write('{},{},{},{},{}\n'.format(id, mf_name, item_type, price, service_date))


    def damaged(sjk):
        items = sjk.Inventories
        keys = sorted(items.keys(), key=lambda x: items[x]['damaged'], reverse=True)
        with open('/Users/sjk57/PycharmProjects/CIS2348/DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                mf_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, mf_name, item_type, price, service_date))


if __name__ == '__main__':
    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            readCSV = csv.reader(csv_file, delimiter=',')
            for line in readCSV:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    mf_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = mf_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged.strip()
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

    inventory = AllInventory(items)
    inventory.FI()
    inventory.by_type()
    inventory.damaged()

    types = []
    manufacturers = []
    for item in items:
        checked_type = items[item]['item_type']
        checked_manufacturer = items[item]['manufacturer']
        if checked_type not in types:
            types.append(checked_type)
        if checked_manufacturer not in types:
            manufacturers.append(checked_manufacturer)

    user_input = None
    while user_input != 'q':
        user_input = input("\nEnter manufacturer and item type (ex: Samsung phone) or enter 'q' to quit:\n")
        if user_input == 'q':
            break
        else:
            user_manufacturer = None
            user_type = None
            user_input = user_input.split()
            wrong = False
            for word in user_input:
                if word in manufacturers:
                    if user_manufacturer:
                        wrong = True
                    else:
                        user_manufacturer = word
                elif word in types:
                    if user_type:
                        wrong = True
                    else:
                        user_type = word
            if not user_manufacturer or not user_type or wrong:
                print("No such item in inventory")
            else:
                keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)

                same_type_items = []
                similar_items = {}
                for item in keys:
                    if items[item]['item_type'] == user_type:
                        service_date = items[item]['service_date']
                        if items[item]['manufacturer'] == user_manufacturer:
                            if not items[item]['damaged']:
                                same_type_items.append((item, items[item]))
                        else:
                            if not items[item]['damaged']:
                                similar_items[item] = items[item]

                if same_type_items:
                    item = same_type_items[0]
                    item_id = item[0]
                    mf_name = item[1]['manufacturer']
                    item_type = item[1]['item_type']
                    price = item[1]['price']
                    service_date = item[1]['service_date']
                    damaged = item[1]['damaged']
                    print("\nYour item is: {}, {}, {}, {}, {}, {}".format(item_id, mf_name, item_type, price, service_date, damaged))

                    if similar_items:
                        matched_price = price
                        close_item = None
                        close_in_price = None
                        for item in similar_items:
                            if close_in_price == None:
                                close_item = similar_items[item]
                                close_in_price = abs(int(matched_price) - int(similar_items[item]['price']))
                                item_id = item
                                mf_name = similar_items[item]['manufacturer']
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']
                                continue
                            price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                            if price_diff < close_in_price:
                                close_item = item
                                close_in_price = price_diff
                                item_id = item
                                mf_name = similar_items[item]['manufacturer']
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']
                        print("You may, also, consider: {}, {}, {}, {}".format(item_id, mf_name, item_type, price))

                    else:
                        print("No such item in inventory")