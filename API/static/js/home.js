/*
 * JavaScript file for the application to demonstrate
 * using the API
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/orders',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        create: function(qty, ordernum) {
            let ajax_options = {
                type: 'POST',
                url: 'api/orders',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'qty': qty,
                    'ordernum': ordernum
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_create_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        update: function(qty, ordernum) {
            let ajax_options = {
                type: 'PUT',
                url: 'api/orders/' + ordernum,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'qty': qty,
                    'ordernum': ordernum
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_update_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        'delete': function(ordernum) {
            let ajax_options = {
                type: 'DELETE',
                url: 'api/orders/' + ordernum,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_delete_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        }
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    let $qty = $('#qty'),
        $ordernum = $('#ordernum');

    // return the API
    return {
        reset: function() {
            $ordernum.val('');
            $qty.val('').focus();
        },
        update_editor: function(qty, ordernum) {
            $ordernum.val(ordernum);
            $qty.val(qty).focus();
        },
        build_table: function(orders) {
            let rows = ''

            // clear the table
            $('.orders table > tbody').empty();

            // did we get a orders array?
            if (orders) {
                for (let i=0, l=orders.length; i < l; i++) {
                    rows += `<tr><td class="qty">${orders[i].qty}</td><td class="ordernum">${orders[i].ordernum}</td><td>${orders[i].recorddate}</td></tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $qty = $('#qty'),
        $ordernum = $('#ordernum');

    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read();
    }, 100)

    // Validate input
    function validate(qty, ordernum) {
        return qty !== "" && ordernum !== "";
    }

    // Create our event handlers
    $('#create').click(function(e) {
        let qty = $qty.val(),
            ordernum = $ordernum.val();

        e.preventDefault();

        if (validate(qty, ordernum)) {
            model.create(qty, ordernum)
        } else {
            alert('Problem with first or order ref input');
        }
    });

    $('#update').click(function(e) {
        let qty = $qty.val(),
            ordernum = $ordernum.val();

        e.preventDefault();

        if (validate(qty, ordernum)) {
            model.update(qty, ordernum)
        } else {
            alert('Problem with first or order ref input');
        }
        e.preventDefault();
    });

    $('#delete').click(function(e) {
        let ordernum = $ordernum.val();

        e.preventDefault();

        if (validate('placeholder', ordernum)) {
            model.delete(ordernum)
        } else {
            alert('Problem with first or order ref input');
        }
        e.preventDefault();
    });

    $('#reset').click(function() {
        view.reset();
    })

    $('table > tbody').on('dblclick', 'tr', function(e) {
        let $target = $(e.target),
            qty,
            ordernum;

        qty = $target
            .parent()
            .find('td.qty')
            .text();

        ordernum = $target
            .parent()
            .find('td.ordernum')
            .text();

        view.update_editor(qty, ordernum);
    });

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));


