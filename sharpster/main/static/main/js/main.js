$(document).ready(function() {
    var current = 0;
    var images = $('.carousel img');

    setInterval(function() {
        images.eq(current).fadeOut(1000);
        current = (current + 1) % images.length;
        images.eq(current).fadeIn(1000);
    }, 3000);
});