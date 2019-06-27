import datetime
import json


def write_order_to_json(item, quantity, price, buyer, date):
    order = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": str(date)
    }

    with open('orders.json', 'r') as fh_r:
        data_orders = json.load(fh_r)

    with open('orders.json', 'w') as fh_w:
        new_data = data_orders['orders']
        new_data.append(order)
        json.dump(data_orders, fh_w, indent=4)


def main():
    write_order_to_json('Cookies', 3, 23.4, 'Guido', datetime.datetime.now())

    with open('orders.json') as fh:
        content = fh.read()
        objs = json.loads(content)

    for dict in objs['orders']:
        for key, val in dict.items():
            print(key, val)


if __name__ == '__main__':
    main()
