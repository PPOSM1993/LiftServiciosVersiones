var tblBuy;
$(function() {
    tblBuy = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "position" },
            { "data": "prove.names" },
            { "data": "date_joined" },
            { "data": "subtotal" },
            { "data": "total" },
            { "data": "id" },
        ],
        columnDefs: [{
                targets: [-2, -3],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return '$' + parseFloat(data).toFixed(2);
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    var buttons = '<a href="/erp/buy/delete/' + row.id + '/" class="btn btn-danger btn-sm btn-flat"><i class="fas fa-trash-alt"></i></a> ';
                    buttons += '<a href="/erp/buy/update/' + row.id + '/" class="btn btn-warning btn-sm btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a rel="details" class="btn btn-success btn-sm btn-flat"><i class="fas fa-search"></i></a> ';
                    //buttons += '<a href="/erp/sale/invoice/pdf/' + row.id + '/" target="_blank" class="btn btn-info btn-sm btn-flat"><i class="fas fa-file-pdf"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function(settings, json) {

        }
    });
    $('#data tbody')
        .on('click', 'a[rel="details"]', function() {
            var tr = tblBuy.cell($(this).closest('td, li')).index();
            var data = tblBuy.row(tr.row).data();

            $('#tblDet').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                deferRender: true,
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details_prod',
                        id: data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    { "data": "prod.name" },
                    { "data": "prod.cat.name" },
                    { "data": "price" },
                    { "data": "cant" },
                    { "data": "subtotal" },

                ],
                columnDefs: [{
                        targets: [-1, -3],
                        class: 'text-center',
                        render: function(data, type, row) {
                            return '$' + parseFloat(data).toFixed(2);
                        }
                    },
                    {
                        targets: [-2],
                        class: 'text-center',
                        render: function(data, type, row) {
                            return data;
                        }
                    },
                ],
                initComplete: function(settings, json) {

                }
            });
            $('#myModalDet').modal('show');

        });
});