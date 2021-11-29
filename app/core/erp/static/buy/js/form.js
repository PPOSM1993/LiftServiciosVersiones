/*var tblProducts;

var comps = {
    items: {
        prove: '',
        date_joined: '',
        subtotal: 0.00,
        total: 0.00,
        products: []
    },
    calculate_invoice: function() {
        var subtotal = 0.00;
        $.each(this.items.products, function(pos, dict) {
            dict.subtotal = dict.cant * parseFloat(dict.preciocompra);
            subtotal += dict.subtotal;
        });
        this.items.subtotal = subtotal;
        this.items.total = this.items.subtotal;

        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        $('input[name="total"]').val(this.items.total.toFixed(2));
    },
    add: function(item) {
        this.items.products.push(item);
        this.list();
    },
    list: function() {
        this.calculate_invoice();

        tblProducts = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.products,
            columns: [
                { "data": "id" },
                { "data": "name" },
                { "data": "cat.name" },
                { "data": "preciocompra" },
                { "data": "cant" },
                { "data": "subtotal" },
            ],
            columnDefs: [{
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function(data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat" style="color: white;"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function(data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function(data, type, row) {
                        return '<input type="text" name="cant" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cant + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function(data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {
                $(row).find('input[name="cant"]').TouchSpin({
                    min: 1,
                    step: 1,
                    max: 1000000000
                });
            },
            initComplete: function(settings, json) {}
        });
    },
};

$(function() {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#date_joined').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        //minDate: moment().format("YYYY-MM-DD")
    });


    // search products

    $('input[name="search"]').autocomplete({
        source: function(request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function(data) {
                response(data);
            }).fail(function(jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function(data) {

            });
        },
        delay: 500,
        minLength: 1,
        select: function(event, ui) {
            event.preventDefault();
            console.clear();
            ui.item.cant = 1;
            ui.item.subtotal = 0.00;
            console.log(comps.items);
            comps.add(ui.item);
            $(this).val('');
        }
    });

    //event cant

    $('#tblProducts tbody').on('change', 'input[name="cant"]', function() {
        console.clear();
        var cant = parseInt($(this).val());
        var tr = tblProducts.cell($(this).closest('td, li')).index();
        comps.items.products[tr.row].cant = cant;
        comps.calculate_invoice();
        $('td:eq(5)', tblProducts.row(tr.row).node()).html('$' + comps.items.products[tr.row].subtotal.toFixed(2));

    });
});*/

var tblProducts;
var comps = {
    items: {
        prove: '',
        date_joined: '',
        subtotal: 0.00,
        total: 0.00,
        products: []
    },
    calculate_invoice: function() {
        var subtotal = 0.00;
        $.each(this.items.products, function(pos, dict) {
            dict.pos = pos;
            dict.subtotal = dict.cant * parseFloat(dict.preciocompra);
            subtotal += dict.subtotal;
        });
        this.items.subtotal = subtotal;
        this.items.total = this.items.subtotal;

        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        $('input[name="total"]').val(this.items.total.toFixed(2));
    },
    add: function(item) {
        this.items.products.push(item);
        this.list();
    },
    list: function() {
        this.calculate_invoice();
        tblProducts = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.products,
            columns: [
                { "data": "id" },
                { "data": "name" },
                { "data": "cat.name" },
                { "data": "preciocompra" },
                { "data": "cant" },
                { "data": "subtotal" },
            ],
            columnDefs: [{
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function(data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat" style="color: white;"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function(data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function(data, type, row) {
                        return '<input type="text" name="cant" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cant + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function(data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="cant"]').TouchSpin({
                    min: 1,
                    max: 1000000000,
                    step: 1
                });

            },
            initComplete: function(settings, json) {

            }
        });
    },
};

$(function() {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#date_joined').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        //minDate: moment().format("YYYY-MM-DD")
    });

    // search products

    $('input[name="search"]').autocomplete({
        source: function(request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function(data) {
                response(data);
            }).fail(function(jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function(data) {

            });
        },
        delay: 500,
        minLength: 1,
        select: function(event, ui) {
            event.preventDefault();
            console.clear();
            ui.item.cant = 1;
            ui.item.subtotal = 0.00;
            console.log(comps.items);
            comps.add(ui.item);
            $(this).val('');
        }
    });


    $('.btnRemoveAll').on('click', function() {
        if (comps.items.products.length === 0) return false;
        alert_action('Notificación', '¿Estas seguro de eliminar todos los items de tu detalle?', function() {
            comps.items.products = [];
            comps.list();
        });
    });

    // event cant
    $('#tblProducts tbody')
        .on('click', 'a[rel="remove"]', function() {
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            alert_action('Notificación', '¿Estas seguro de eliminar el producto de tu detalle?', function() {
                comps.items.products.splice(tr.row, 1);
                comps.list();
            });
        })
        .on('change', 'input[name="cant"]', function() {
            console.clear();
            var cant = parseInt($(this).val());
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            comps.items.products[tr.row].cant = cant;
            comps.calculate_invoice();
            $('td:eq(5)', tblProducts.row(tr.row).node()).html('$' + comps.items.products[tr.row].subtotal.toFixed(2));
        });
});