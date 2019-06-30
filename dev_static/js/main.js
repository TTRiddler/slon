(function ($) {
    function FooterBottom() {
        $('body').css('margin-bottom', $('.footer').outerHeight())
    };

    FooterBottom();
    window.addEventListener('resize', FooterBottom, false);
})(jQuery);

(function ($) {
    function HeaderHeight() {
        $('.jumbotron').css('height', $(window).outerHeight() - $('.top-bar').outerHeight() - $('.top-bar-2').outerHeight() - $('.navbar').outerHeight())
    };

    HeaderHeight();
    window.addEventListener('resize', HeaderHeight, false);
})(jQuery);

(function ($) {
    function CardsHeight() {
        if(window.matchMedia('(min-width: 576px)').matches){
            $(function() {
                $('.shuffle-item .card-body').matchHeight({
                    byRow:false
                });
            });

            $(function() {
                $('.newsfeed-item .card-body').matchHeight({
                    byRow:false
                });
            });

            $(function() {
                $('.tab-pane .card-body').matchHeight({
                    byRow:false
                });
            });

            $(function() {
                $('.staff-item .card-body').matchHeight({
                    byRow:false
                });
            });
        };
    };

    CardsHeight();
    window.addEventListener('resize', CardsHeight, false);
})(jQuery);

(function ($) {
    function StickySlider() {
        if(window.matchMedia('(min-width: 992px)').matches){
            $(window).on('scroll', function (event) {
                var scrollValue = $(window).scrollTop();
                if (scrollValue >= 350) {
                    $('.slider-container').addClass('sticky-slider');
                } else {
                    $('.slider-container').removeClass('sticky-slider');
                }
            });
        };
    };

    StickySlider();
    window.addEventListener('resize', StickySlider, false);
})(jQuery);

$(function () {
    $(".zoom-image").SmartPhoto();
});

$(document).ready(function () {
    $(".dropdown").hover(
        function () {
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true, true).delay(50).slideDown("fast");
            $(this).toggleClass('open');
        },
        function () {
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true, true).delay(50).slideUp("fast");
            $(this).toggleClass('open');
        }
    );
});

$(function () {
    'use strict'
    $('[data-toggle="offcanvas"]').on('click', function () {
        $('.offcanvas-collapse').toggleClass('open')
    })
})

$(document).ready(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 700) {
            $('.scroll-to-top').fadeIn(200);
        } else {
            $('.scroll-to-top').fadeOut(200);
        }
    });
    $('.scroll-to-top').click(function () {
        $('html, body').animate({
            scrollTop: 0
        }, 300);
        return false;
    });
});

$(window).on('scroll', function (event) {
    var scrollValue = $(window).scrollTop();
    if (scrollValue >= $('.top-bar').outerHeight() + $('.top-bar-2').outerHeight()) {
        $('.navbar').addClass('sticky');
    } else {
        $('.navbar').removeClass('sticky');
    }
});

$(document).ready(function () {
    var Shuffle = window.Shuffle;
    var jQuery = window.jQuery;

    var myShuffle = new Shuffle(document.querySelector('.shuffle'), {
        itemSelector: '.shuffle-item',
        buffer: 1,
    });

    jQuery('input[name="shuffle-filter"]').on('change', function (evt) {
        var input = evt.currentTarget;
        if (input.checked) {
            myShuffle.filter(input.value);
        }
    });
});

function numberWithCommas(number) {
    var parts = number.toString().split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    return parts.join(".");
}
$(document).ready(function() {
    $(".number").each(function() {
        var num = $(this).text();
        var commaNum = numberWithCommas(num);
        $(this).text(commaNum);
    });
});

(function() {
    'use strict';
    window.addEventListener('load', function() {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

$(document).ready(function () {
    var SignPhoneMask = IMask(
        document.getElementById('SignPhone'), {
            mask: '+{7} (000) 000-00-00'
        });

    var CallbackPhoneMask = IMask(
        document.getElementById('CallbackPhone'), {
            mask: '+{7} (000) 000-00-00'
        });

    var SignPhone2Mask = IMask(
        document.getElementById('SignPhone2'), {
            mask: '+{7} (000) 000-00-00'
        });

    var SignAgeMask = IMask(
        document.getElementById('SignAge'),
        {
            mask: Number,
            min: 0,
            max: 10,
            thousandsSeparator: ' '
        });

    var SignAge2Mask = IMask(
        document.getElementById('SignAge2'),
        {
            mask: Number,
            min: 0,
            max: 10,
            thousandsSeparator: ' '
        });
});

$('.slider-for').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.slider-nav'
});
$('.slider-nav').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    asNavFor: '.slider-for',
    dots: false,
    centerMode: false,
    focusOnSelect: true,
    arrows: false,
});