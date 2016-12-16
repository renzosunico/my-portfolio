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
