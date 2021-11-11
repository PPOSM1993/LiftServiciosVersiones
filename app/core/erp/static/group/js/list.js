$(function() {
    $('#data').DataTable({
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
            { "data": "name" },
            { "data": "id" },
        ],
        columnDefs: [{
            targets: [-1],
            class: 'text-center',
            orderable: false,
            render: function(data, type, row) {
                var buttons = '<a href="/erp/group/update/' + row.id + '/" class="btn btn-warning btn-sm btn-flat"><i class="fas fa-edit"></i></a> ';
                buttons += '<a href="/erp/group/delete/' + row.id + '/" type="button" class="btn btn-danger btn-sm btn-flat"><i class="fas fa-trash-alt"></i></a>';
                return buttons;
            }
        }, ],
        initComplete: function(settings, json) {

        }
    });
});