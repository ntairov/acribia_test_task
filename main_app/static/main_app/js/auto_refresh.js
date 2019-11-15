function refresh() {
    $.ajax({
        url: 'ajax/status_code/',
        success: function (data) {
            $('#status').replaceWith($('#status', data));
        }
    });
}

$(function () {
    setInterval('refresh()', 2000);
});
