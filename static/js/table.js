$(document).ready(() => {
    table()
});

    function table() {
    $('#profile_table').DataTable({
        ordering: false,
        searching: false,
        lengthChange: false,
        pageLength: 4,
        pagingType: 'simple'
        });
    }