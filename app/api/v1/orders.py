"""
orders.py
Purpose - create, update, delete, edit, display orders
WanjawaWB@gmail.com
15-Sep-2018
"""

# global inclusions
from datetime import datetime
from flask import make_response
from flask import abort

def get_recorddate():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

ORDERS = {
    "ref001": {
        "ordernum": "ref001",
        "qty": 5,
        "recorddate": get_recorddate()
    },
    "ref002": {
        "ordernum": "ref002",
        "qty": 3,
        "recorddate": get_recorddate()
    },
    "ref003": {
        "ordernum": "ref003",
        "qty": 2,
        "recorddate": get_recorddate()
    }
}


def read_all():
    """
    Read all orders i.e. /api/orders
    :return:        json string of list of orders
    """
    return [ORDERS[key] for key in sorted(ORDERS.keys())]

def read_one(ordernum):
    """
    List particular order i.e. /api/orders/{ordernum}
    :param ordernum: order number to be listed
    :return:         matching ordernum
    """
    if ordernum in ORDERS:
        order = ORDERS.get(ordernum)
    else:
        abort(404, 'Order with order ref {ordernum} not found'.format(
            ordernum=ordernum))
    return order

def create(order):
    """
    Create new order as per dictionary definition
    :param order: Order number to create
    :return:      success as 201 and 406 if order exists
    """
    ordernum = order.get('ordernum', None)
    qty = order.get('qty', None)
    if ordernum is not None and ordernum not in ORDERS:
        ORDERS[ordernum] = {
            'ordernum': ordernum,
            'qty': qty,
            "recorddate": get_recorddate()
        }
        return ORDERS[ordernum], 201
    else:
        abort(406, 'Order no. {ordernum} exists'.format(
            ordernum=ordernum))

def update(ordernum, order):
    """
    Update existing order
    :param ordernum: order number to be updated
    :param order:    order to update
    :return:         updated order
    """
    if ordernum in ORDERS:
        ORDERS[ordernum]['qty'] = order.get('qty')
        ORDERS[ordernum]['recorddate'] = get_recorddate()
        return ORDERS[ordernum]
    else:
        abort(404, 'Order no. {ordernum} not found'.format(
            ordernum=ordernum))

def delete(ordernum):
    """
    Delete an order
    :param ordernum: order number to be updated
    :return:         successful deletion as 200 and 404 on not found
    """
    if ordernum in ORDERS:
        del ORDERS[ordernum]
        return make_response('Order no. {ordernum} deleted'.format(
            ordernum=ordernum), 200)
    else:
        abort(404, 'Order no. {ordernum} not found'.format(
            ordernum=ordernum))
