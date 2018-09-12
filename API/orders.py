"""
This is the orders module and supports all the ReST actions for the
ORDERS collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import (
    make_response,
    abort
)


def get_recorddate():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
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
    This function responds to a request for /api/orders
    with the complete lists of orders

    :return:        json string of list of orders
    """
    # Create the list of orders from our data
    return [ORDERS[key] for key in sorted(ORDERS.keys())]


def read_one(ordernum):
    """
    This function responds to a request for /api/orders/{ordernum}
    with one matching order from orders

    :param ordernum:   order ref of order to find
    :return:        order matching order ref
    """
    # Does the order exist in orders?
    if ordernum in ORDERS:
        order = ORDERS.get(ordernum)

    # otherwise, nope, not found
    else:
        abort(404, 'Order with order ref {ordernum} not found'.format(
            ordernum=ordernum))

    return order


def create(order):
    """
    This function creates a new order in the orders structure
    based on the passed in order data

    :param order:  order to create in orders structure
    :return:        201 on success, 406 on order exists
    """
    ordernum = order.get('ordernum', None)
    qty = order.get('qty', None)

    # Does the order exist already?
    if ordernum not in ORDERS and ordernum is not None:
        ORDERS[ordernum] = {
            'ordernum': ordernum,
            'qty': qty,
            "recorddate": get_recorddate()
        }
        return ORDERS[ordernum], 201

    # Otherwise, they exist, that's an error
    else:
        abort(406, 'Order with order ref {ordernum} already exists'.format(
            ordernum=ordernum))


def update(ordernum, order):
    """
    This function updates an existing order in the orders structure

    :param ordernum:   order ref of order to update in the orders structure
    :param order:  order to update
    :return:        updated order structure
    """
    # Does the order exist in orders?
    if ordernum in ORDERS:
        ORDERS[ordernum]['qty'] = order.get('qty')
        ORDERS[ordernum]['recorddate'] = get_recorddate()

        return ORDERS[ordernum]

    # otherwise, nope, that's an error
    else:
        abort(404, 'Order with order ref {ordernum} not found'.format(
            ordernum=ordernum))


def delete(ordernum):
    """
    This function deletes a order from the orders structure

    :param ordernum:   order ref of order to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the order to delete exist?
    if ordernum in ORDERS:
        del ORDERS[ordernum]
        return make_response('{ordernum} successfully deleted'.format(
            ordernum=ordernum), 200)

    # Otherwise, nope, order to delete not found
    else:
        abort(404, 'Order with order ref {ordernum} not found'.format(
            ordernum=ordernum))
