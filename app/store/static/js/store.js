$(document).ready(function () {
    $('[data-toggle="collapse"]').click(function () {
        $(this).toggleClass("active");
        if ($(this).hasClass("active")) {
            $(this).text("Hide Filters");
        } else {
            $(this).text("Show Filters");
        }
    });
});