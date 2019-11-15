function refresh() {
    $.ajax({
        url: '{% url "status_checker:status_code" %}',
        success: function (data) {
            $('#status').replaceWith($('#status', data)); // NOTE this
        }
    });
}

$(function () {
    setInterval('refresh()', 1000);
});
