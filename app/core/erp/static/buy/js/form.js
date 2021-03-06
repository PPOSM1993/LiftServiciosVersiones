var tblProducts;
var comps = {
    items: {
        prove: '',
        date_joined: '',
        subtotal: 0.00,
        total: 0.00,
        products: []
    },
    get_ids: function() {
        var ids = [];
        $.each(this.items.products, function(key, value) {
            ids.push(value.id);
        });
        return ids;
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
                { "data": "stock" },
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

function formatRepo(repo) {
    if (repo.loading) {
        return repo.text;
    }

    var option = $(
        '<div class="wrapper container">' +
        '<div class="row">' +
        '<div class="col-lg-1">' +
        '<img src="' + repo.image + '" class="img-fluid img-thumbnail d-block mx-auto rounded">' +
        '</div>' +
        '<div class="col-lg-11 text-left shadow-sm">' +
        //'<br>' +
        '<p style="margin-bottom: 0;">' +
        '<b>REPUESTO:</b> ' + repo.name + '<br>' +
        '<b>CATEGOR??A:</b> ' + repo.cat.name + '<br>' +
        '<b>PRECIO COMPRA:</b> <span class="badge badge-warning">$' + repo.preciocompra + '</span>' +
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');

    return option;
}

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

    $('select[name="prove"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function(params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_proveedor'
                }
                return queryParameters;
            },
            processResults: function(data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese Descripci??n',
        minimumInputLength: 1,
    });

    $('.btnAddProveedor').on('click', function() {
        $('#myModalProveedor').modal('show');
    });

    $('#myModalProveedor').on('hidden.bs.modal', function(e) {
        $('#frmProveedor').trigger('reset');
    });

    $('#frmProveedor').on('submit', function(e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_proveedor');
        parameters.append('comps', JSON.stringify(comps.items));
        submit_with_ajax(window.location.pathname, 'Notificaci??n', '??Desea registrar nuevo Proveedor?', parameters, function(response) {
            $('#myModalProveedor').modal('hide');
        });
    });

    $('.btnRemoveAll').on('click', function() {
        if (comps.items.products.length === 0) return false;
        alert_action('Notificaci??n', '??Estas seguro de eliminar todos los items de tu detalle?', function() {
            comps.items.products = [];
            comps.list();
        });
    });

    // event cant
    $('#tblProducts tbody')
        .on('click', 'a[rel="remove"]', function() {
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            alert_action('Notificaci??n', '??Estas seguro de eliminar el producto de tu detalle?', function() {
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

    $('.btnClearSearch').on('click', function() {
        $('input[name="search"]').val('').focus();
    });

    // event submit
    $('#frmBuy').on('submit', function(e) {
        e.preventDefault();

        if (comps.items.products.length === 0) {
            message_error('Debe al menos tener un item en su detalle de venta');
            return false;
        }

        comps.items.date_joined = $('input[name="date_joined"]').val();
        comps.items.prove = $('select[name="prove"]').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('comps', JSON.stringify(comps.items));
        submit_with_ajax(window.location.pathname, 'Notificaci??n', '??Estas seguro de realizar la siguiente acci??n?', parameters, function() {
            location.href = '/erp/buy/list/';
        });
    });


    //comps.list();
    $('select[name="search"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function(params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_products',
                    ids: JSON.stringify(comps.get_ids())
                }
                return queryParameters;
            },
            processResults: function(data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese Descripci??n',
        minimumInputLength: 1,
        templateResult: formatRepo,

    }).on('select2:select', function(e) {
        var data = e.params.data;
        data.cant = 1;
        data.subtotal = 0.00;
        comps.add(data);
        $(this).val('').trigger('change.select2');
    });

    comps.list();
});