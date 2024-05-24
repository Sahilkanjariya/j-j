(function($){

    /*
        1. Data Background Function
        2. Scroll top button
        3. Offcanvus toggle
        4. Theme Slider Functions
        5. Pricing Range Slider
        6. Nice Select
        7. Checkout Toggle
        8. Header Sticky
        9. Mobile Menu
        10. Header Search 
        11. Preloader
        12. Fancybox
        13. Countdown
        14. Cart Drawer
        15. Wow Js
        16. Count Down
        17. Accordion Boxs
    */


    //1. Data Background Set
    $('[data-background]').each(function () {
        $(this).css('background-image', 'url(' + $(this).attr('data-background') + ')');
    });

    //2. Scroll top button
    $(window).on("scroll", function(){
        var scrollBar = $(this).scrollTop();
        if(scrollBar > 150 ) {
            $(".scroll-top-btn").fadeIn();
        } else {
            $(".scroll-top-btn").fadeOut();
        }
    })
    $(".scroll-top-btn").on("click", function(){
        $("body,html").animate({
            scrollTop: 0
        });
    });


    //3. Offcanvus toggle
    $(".offcanvus-toggle").on("click", function () {
        $(".offcanvus-box").addClass("active");
    });

    $(".offcanvus-close").on("click", function(){
        $(".offcanvus-box").removeClass("active");
    });

    $(document).on("mouseup", function (e) {
        var offCanvusMenu = $(".offcanvus-box");
  
        if (!offCanvusMenu.is(e.target) && offCanvusMenu.has(e.target).length === 0) {
          $(".offcanvus-box").removeClass("active");
        }
    });



    //4. Theme Slider 
    $(".theme-slider").slick({
        
    });

        //hero slider
        $(".ur-hero-slider").slick({
            slidesToShow: 1,
            autoplay: true,
            speed: 700,
            fade: true,
            dots: true,
            prevArrow: '<button type="button" class="prev-arrow"><i class="fa-solid fa-angle-up"></i></button>',
            nextArrow: '<button type="button" class="next-arrow"><i class="fa-solid fa-angle-down"></i></button>'
        });

        //category slider
        $(".ur-category-slider").slick({
            slidesToShow: 4,
            arrows: false, 
            autoplay: true,
            speed: 700,
            responsive: [
                {
                    breakpoint: 1200, 
                    settings: {
                        slidesToShow: 3,
                    }
                },
                {
                    breakpoint: 992, 
                    settings: {
                        slidesToShow: 2,
                    }
                }, 
                {
                    breakpoint: 576, 
                    settings: {
                        slidesToShow: 1,
                    }
                }
            ]
        });

        //featured product slider
        $(".feature-product-slider").slick({
            slidesToShow: 4,
            autoplay: true,
            speed: 700,
            prevArrow: "<button class='prev-arrow'><i class='fa-solid fa-chevron-left'></i></button>", 
            nextArrow: "<button class='next-arrow'><i class='fa-solid fa-chevron-right'></i></button>",
            responsive: [
                {
                    breakpoint: 1200, 
                    settings: {
                        slidesToShow: 3,
                    }
                }, 
                {
                    breakpoint: 992, 
                    settings: {
                        slidesToShow: 2,
                    }
                }, 
                {
                    breakpoint: 500,
                    settings: {
                        slidesToShow: 1,
                    }
                }
            ]
        });

        //brand slider
        $(".ur-brand-slider").slick({
            slidesToShow: 5,
            autoplay: true,
            speed: 700,
            arrows: false,
            responsive: [
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 4,
                    }
                }, 
                {
                    breakpoint: 768, 
                    settings: {
                        slidesToShow: 3,
                    }
                }, 
                {
                    breakpoint: 450, 
                    settings: {
                        slidesToShow: 2,
                    }
                }

            ]
        });

        //feedback slider
        $(".ur-feedback-slider").slick({
            slidesToShow: 1,
            autoplay: true,
            speed: 700,
            arrows: false, 
            dots: true,
            asNavFor: '.feedback-clients-thumbail-slider'
        });

        //feedback thumbnail slider
        $(".feedback-clients-thumbail-slider").slick({
            slidesToShow: 1,
            autoplay: true,
            speed: 700,
            arrows: false, 
            asNavFor: '.ur-feedback-slider',
            fade: true,
            cssEase: 'linear'
        });

        //instagram slider
        $(".instagram-slider").slick({
            slidesToShow: 3,
            autoplay: true,
            speed: 700,
            centerMode: true,
            centerPadding: 0,
            prevArrow: "<button class='prev-arrow'><i class='fa-solid fa-chevron-left'></i></button>", 
            nextArrow: "<button class='next-arrow'><i class='fa-solid fa-chevron-right'></i></button>",
            responsive: [
                {
                    breakpoint: 768, 
                    settings: {
                        slidesToShow: 2,
                        centerMode: false,
                    }
                }
            ]
        });

        //ur2 hero slider
        $(".ur2-hero-slider").slick({
            slidesToShow: 1,
            autoplay: true,
            speed: 700,
            arrows: false,
            pauseOnHover: false,
            fade: true,
        });

        //feedback slider 2 
        $(".ur2-feedback-slider").slick({
            slidesToShow: 1,
            autoplay: true,
            speed: 700,
            prevArrow: '<button type"button" class="prev-arrow"><svg width="41" height="26" viewBox="0 0 41 26" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1.15625 12.6094C0.921875 12.8438 0.921875 13.2344 1.15625 13.4688L13.0312 25.3438C13.1094 25.5 13.2656 25.5 13.5 25.5C13.6562 25.5 13.8125 25.4219 13.8906 25.2656C14.125 25.0312 14.125 24.6406 13.8906 24.4062L3.10938 13.625H40.375C40.6875 13.625 41 13.3906 41 13C41 12.6875 40.6875 12.375 40.375 12.375H3.10938L13.8906 1.59375C14.125 1.35938 14.125 0.96875 13.8906 0.734375C13.6562 0.5 13.2656 0.5 13.0312 0.734375L1.15625 12.6094Z" fill="#121111"/></svg></button>',
            nextArrow: '<button type"button" class="next-arrow"><svg width="41" height="26" viewBox="0 0 41 26" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M39.8438 12.6094C40.0781 12.8438 40.0781 13.2344 39.8438 13.4688L27.9688 25.3438C27.8906 25.5 27.7344 25.5 27.5 25.5C27.3438 25.5 27.1875 25.4219 27.1094 25.2656C26.875 25.0312 26.875 24.6406 27.1094 24.4062L37.8906 13.625H0.625C0.3125 13.625 0 13.3906 0 13C0 12.6875 0.3125 12.375 0.625 12.375H37.8906L27.1094 1.59375C26.875 1.35938 26.875 0.96875 27.1094 0.734375C27.3438 0.5 27.7344 0.5 27.9688 0.734375L39.8438 12.6094Z" fill="#74787C"/></svg></button>',
        });

        //instagram slider
        $(".ur-instagram-slider").slick({
            slidesToShow: 4,
            autoplay: true,
            speed: 700,
            arrows: false,
            responsive: [
                {
                    breakpoint: 1200, 
                    settings: {
                        slidesToShow: 3,
                    }
                },
                {
                    breakpoint: 992, 
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 576, 
                    settings: {
                        slidesToShow: 1,
                    }
                },
            ]
        });

        //single product slider 
        $(".single-product-slider").slick({
            slidesToShow: 1,
            arrows: false,
            asNavFor: ".product-nav-slider",
        });

        //product nav slider
        $(".product-nav-slider").slick({
            slidesToShow: 5,
            arrows: false,
            asNavFor: ".single-product-slider",
            vertical: true,
            verticalSwiping: true,
            focusOnSelect: true,
            responsive: [
                {
                    breakpoint: 768, 
                    settings: {
                        vertical: false,
                        slidesToShow: 3,
                        verticalSwiping: false,
                    }
                }
            ]
        });

        $(".single-product-slider2").slick({
            slidesToShow: 1,
            arrows: false,
            asNavFor: ".product-nav-slider2",
        });

        //product nav slider
        $(".product-nav-slider2").slick({
            slidesToShow: 3,
            arrows: false,
            asNavFor: ".single-product-slider2",
            vertical: true,
            verticalSwiping: true,
            focusOnSelect: true,
            responsive: [
                {
                    breakpoint: 1400, 
                    settings: {
                        slidesToShow: 5,
                    }
                },
                {
                    breakpoint: 1200, 
                    settings: {
                        slidesToShow: 4,
                    }
                },
                {
                    breakpoint: 992, 
                    settings: {
                        vertical: false,
                        slidesToShow: 3,
                        verticalSwiping: false,
                    }
                }, 
                {
                    breakpoint: 768, 
                    settings: {
                        vertical: false,
                        slidesToShow: 2,
                        verticalSwiping: false,
                    }
                }, 

            ]
        });
        $(".ur3-gift-slider").slick({
            slidesToShow: 3,
            arrows: false,
            autoplay: true,
            responsive: [
                {
                    breakpoint: 1200, 
                    settings: {
                        slidesToShow: 2,
                    },
                },
                {
                    breakpoint: 768, 
                    settings: {
                        slidesToShow: 1,
                    },
                },
            ]
        });

        $(".ur3-category-slider").slick({
            slidesToShow: 6,
            arrows: false,
            autoplay: true,
            responsive: [
                {
                    breakpoint: 1400,
                    settings: {
                        slidesToShow: 5,
                    }
                }, 
                {
                    breakpoint: 1200, 
                    settings: {
                        slidesToShow: 4,
                    }
                },
                {
                    breakpoint: 992, 
                    settings: {
                        slidesToShow: 3,
                    }
                }, 
                {
                    breakpoint: 768, 
                    settings: {
                        slidesToShow: 2,
                    }
                }, 
                {
                    breakpoint: 430, 
                    settings: {
                        slidesToShow: 1,
                    }
                }
            ]
        }); 

        $(".ur3-featured-slider").slick({
            slidesToShow: 2,
            arrows: false, 
            autoplay: true,
            responsive: [
                {
                    breakpoint: 768, 
                    settings: {
                        slidesToShow: 1,
                    }
                }
            ]
        });

        

    //5. Pricing Range Slider
    $( ".ur-pricing-range" ).slider({
        range: true,
        min: 0,
        max: 500,
        values: [ 75, 300 ],
        slide: function( event, ui ) {
          $( "#amount" ).val( "₹" + ui.values[ 0 ] + " - ₹" + ui.values[ 1 ] );
        }
    });
    $( "#amount" ).val( "₹" + $( ".ur-pricing-range" ).slider( "values", 0 ) + " - ₹" + $( ".ur-pricing-range" ).slider( "values", 1 ) );

    //6. Nice Select
    $('.nice_select').niceSelect();


    //7.checkout toggle
    $(".checkout-toggle-form").each(function() {
        var toggleBtn = $(this).find(".form-toggle-btn");

        toggleBtn.on("click", function(){
            $(this).parents(".checkout-toggle-form").find(".toggle-form").slideToggle(); 
            return false;
        });

    }); 

    //8. Header Sticky
    $(window).on("scroll", function(){
        var scrollBar = $(this).scrollTop();

        if ( scrollBar > 150 ) {
            $(".header-sticky").addClass("sticky-on");
        } else {
            $(".header-sticky").removeClass("sticky-on");
        }
    });

    //9. Mobile Menu
    $(".mobile-menu-toggle").on("click", function () {
        $(".mobile-menu").addClass("active");
    });

    $(".mobile-menu .close").on("click", function () {
        $(".mobile-menu").removeClass("active");
    });

    $(".mobile-menu ul li.has-submenu i").each(function () {
        $(this).on("click", function () {
        $(this).siblings('ul').slideToggle();
        $(this).toggleClass("icon-rotate");
        });
    });

    $(document).on("mouseup", function (e) {
        var offCanvusMenu = $(".mobile-menu");

        if (!offCanvusMenu.is(e.target) && offCanvusMenu.has(e.target).length === 0) {
            $(".mobile-menu").removeClass("active");
        }
    }); 

    //10. Header Search Open
    $(".header-search-open").on("click", function(){
        $(".ur-search-form").addClass("active");
    }); 

    $(".ur-search-form .close").on("click", function(){
        $(".ur-search-form").removeClass("active");
    });

    //11. Preloader
    $(window).on("load", function(){
        $(".preloader").fadeOut();
    });

    //12. Fancybox
    Fancybox.bind("[data-fancybox]", {});

    //13. Countdown
    $(".countdown-timer").each(function () {
        var $data_date = $(this).data('date');
        $(this).countdown({
          date: $data_date
        });
    });

    //14. Cart Drawer
    $(".user-cart .cart-btn, .ur3-cart-btn").on("click", function(){
        $(".cart-drawer").addClass("active");
    });

    $(".drawer-close").on("click", function(){
        $(".cart-drawer").removeClass("active");
    });

    $(document).on("mouseup", function (e) {
        var offCanvusMenu = $(".cart-drawer");

        if (!offCanvusMenu.is(e.target) && offCanvusMenu.has(e.target).length === 0) {
            $(".cart-drawer").removeClass("active");
        }
    }); 


    //15. wow js
    new WOW().init();


    //17. Accordion Boxs
/*******************************
* ACCORDION WITH TOGGLE ICONS
*******************************/
const items = document.querySelectorAll('.accordion button');

function toggleAccordion() {
  const itemToggle = this.getAttribute('aria-expanded');

  for (i = 0; i < items.length; i++) {
    items[i].setAttribute('aria-expanded', 'false');
  }

  if (itemToggle == 'false') {
    this.setAttribute('aria-expanded', 'true');
  }
}

items.forEach((item) => item.addEventListener('click', toggleAccordion));

   

    $(document).ready(function(){
	$('.rtl-slider').slick({
	  slidesToShow: 1,
	  slidesToScroll: 1,
	  arrows: false,
	  asNavFor: '.rtl-slider-nav'
	});
	$('.rtl-slider-nav').slick({
		slidesToShow: 2,
		slidesToScroll: 1,
		vertical: true,
	    asNavFor: '.rtl-slider',
	    centerMode: false,
	    focusOnSelect: true,
	    arrows: false,
        responsive: [
        {
            breakpoint: 1200, 
            settings: {
                slidesToShow: 3,
                vertical: false,
                verticalSwiping: false,
            }
        },
        {
            breakpoint: 500,
            settings: {
                slidesToShow: 2,
                vertical: false,
            }
        }
    ]
	});
});


})(jQuery)

