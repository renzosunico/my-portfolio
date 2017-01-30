function unblur(selector, from=10, to=0) {
    $({blurRadius: from}).animate({blurRadius: to}, {
        duration: 500,
        easing: 'swing',
        step: function() {
            $(selector).css({
                "-webkit-filter": "blur(" + this.blurRadius + "px)",
                "filter": "blur(" + this.blurRadius + "px)"
            });
        }
    });
}

// Pop up Section

$('a.button').click(function(){
    $(this).parents('.popup-con').fadeOut();
});

$('a.location').click(function(){
    var loc = $(this).data('map');
    $('#' + loc).fadeIn();
});

$(document).scroll(function() {
    nav = parseInt($('.content-container').css('margin-top'), 10);
    nav_height = $('nav').height();

    start_change = nav - nav_height;
    scroll_start = $(this).scrollTop();
    color = scroll_start > start_change ? 'black' : 'rgba(255, 255, 255, .2)';

    $("nav").css('background-color', color);
});
