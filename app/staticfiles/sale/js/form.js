var tblProducts;
var vents = {
    items: {
        cli: '',
        date_joined: '',
        subtotal: 0.00,
        formapago: '',
        iva: 0.00,
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
        var iva = $('input[name="iva"]').val();
        $.each(this.items.products, function(pos, dict) {
            dict.pos = pos;
            dict.subtotal = dict.cant * parseFloat(dict.pvp);
            subtotal += dict.subtotal;
        });
        this.items.subtotal = subtotal;
        this.items.iva = this.items.subtotal * iva;
        this.items.total = this.items.subtotal + this.items.iva;

        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        $('input[name="ivacalc"]').val(this.items.iva.toFixed(2));
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
                { "data": "pvp" },
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
                    max: data.stock,
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
        '<p style="margin-bottom: 0;">' +
        '<b>NOMBRE:</b> ' + repo.name + '<br>' +
        '<b>STOCK:</b> ' + repo.stock + '<br>' +
        '<b>PRECIO CLIENTE:</b> <span class="badge badge-warning">$' + repo.pvp + '</span>' +
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
    });

    $("input[name='iva']").TouchSpin({
            min: 0.19,
            max: 0.19,
            step: 0,
            decimals: 2,
            boostat: 5,
            maxboostedstep: 10,
            postfix: '%'
        }).on('change', function() {
            vents.calculate_invoice();
        })
        .val(0.19);

    //search clients
    $('select[name="cli"]').select2({
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
                    action: 'search_clients'
                }
                return queryParameters;
            },
            processResults: function(data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una descripci??n',
        minimumInputLength: 1,
    });
    $('.btnAddClient').on('click', function() {
        $('#myModalClient').modal('show');
    });
    $('#myModalClient').on('hidden.bs.modal', function(e) {
        $('#frmClient').trigger('reset');
    });
    $('#frmClient').on('submit', function(e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_client');
        parameters.append('vents', JSON.stringify(vents.items));
        submit_with_ajax(window.location.pathname, 'Notificaci??n', '??Desea registrar nuevo Cliente?', parameters, function(response) {

            $('#myModalClient').modal('hide');
        });
    });
    $('.btnRemoveAll').on('click', function() {
        if (vents.items.products.length === 0) return false;
        alert_action('Notificaci??n', '??Estas seguro de eliminar todos los items de tu detalle?', function() {
            vents.items.products = [];
            vents.list();
        });
    });


    // event cant
    $('#tblProducts tbody')
        .on('click', 'a[rel="remove"]', function() {
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            alert_action('Notificaci??n', '??Estas seguro de eliminar el producto de tu detalle?', function() {
                vents.items.products.splice(tr.row, 1);
                vents.list();
            });
        })
        .on('change', 'input[name="cant"]', function() {
            console.clear();
            var cant = parseInt($(this).val());
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            vents.items.products[tr.row].cant = cant;
            vents.calculate_invoice();
            $('td:eq(5)', tblProducts.row(tr.row).node()).html('$' + vents.items.products[tr.row].subtotal.toFixed(2));
        });

    $('.btnClearSearch').on('click', function() {
        $('input[name="search"]').val('').focus();
    });

    // event submit
    $('#frmSale').on('submit', function(e) {
        e.preventDefault();

        if (vents.items.products.length === 0) {
            message_error('Debe al menos tener un item en su detalle de venta');
            return false;
        }

        vents.items.date_joined = $('input[name="date_joined"]').val();
        vents.items.cli = $('select[name="cli"]').val();
        vents.items.formapago = $('select[name="formapago"]').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('vents', JSON.stringify(vents.items));
        submit_with_ajax(window.location.pathname, 'Notificaci??n', '??Estas seguro de realizar la siguiente acci??n?', parameters, function() {
            location.href = '/erp/sale/list/';
        });
    });

    //vents.list();

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
                    ids: JSON.stringify(vents.get_ids())
                }
                return queryParameters;
            },
            processResults: function(data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una descripci??n',
        minimumInputLength: 1,
        templateResult: formatRepo,
    }).on('select2:select', function(e) {
        var data = e.params.data;
        console.log(data);
        data.cant = 1;
        data.subtotal = 0.00;
        console.log(vents.items);
        vents.add(data);
        $(this).val('').trigger('change.select2');

    });
});