$(document).ready(function() {
    $("#backtotop").click(function() {
        $("html, body").animate({
            scrollTop: 0
        }, 500)
    });
    $("#site-footer .footer-block .block-title").click(function() {
        if ($(this).parent().hasClass("active")) {
            $(this).parent().removeClass("active")
        } else {
            $(".footer-block.active").removeClass("active");
            $(this).parent().addClass("active")
        }
    });
    $(".technology-card .card-desk > .card-title").click(function() {
        $(".technology-card .card-desk > .card-title.active").removeClass("active");
        $(this).addClass("active");
        $("#technology-desc").show()
    });
    $(".continue-reading").click(function(e) {
        e.preventDefault();
        $(this).parents(".para-wrap").find(".has-more-content").removeClass("has-more-content");
        $(this).hide()
    });
    $(".play-video").magnificPopup({
        type: "iframe"
    });
    $("#technology-slider").slick({
        speed: 300,
        slidesToShow: 3,
        infinite: !1,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 1199,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, ],
    });
    $(".heroslider").slick({
        speed: 300,
        slidesToShow: 1,
        arrows: !1,
        slidesToScroll: 1,
        dots: !0,
        autoplay: !0
    });
    $(".chairman-slider").slick({
        speed: 300,
        slidesToShow: 1,
        arrows: !0,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
    });
    $(".home-banner-slider").slick({
        speed: 300,
        slidesToShow: 1,
        arrows: !1,
        slidesToScroll: 1,
        dots: !0,
        autoplay: !0
    });
    $("#updates-slider").slick({
        speed: 300,
        slidesToShow: 3,
        slidesToScroll: 1,
        centerMode: !0,
        centerPadding: "20px",
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 1199,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
                centerMode: !1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,
                centerMode: !1
            }
        }, ],
    });
    $(".reports-slider").slick({
        speed: 300,
        slidesToShow: 4,
        infinite: !1,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 1199,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 991,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, ],
    });
    $(".quick-links-slider").slick({
        speed: 300,
        mobileFirst: !0,
        slidesToShow: 2,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 768,
            settings: "unslick"
        }],
    });
    $(".recent-blogs-slider").slick({
        speed: 300,
        mobileFirst: !0,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 992,
            settings: "unslick"
        }, {
            breakpoint: 768,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 260,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, ],
    });
    $(".speciality-filter-slider").slick({
        speed: 300,
        infinite: !1,
        variableWidth: !0,
        prevArrow: '<button type="button" class="slick-arrow slick-prev"><svg width="8" height="12" viewBox="0 0 8 12" fill="none" xmlns="https://www.w3.org/2000/svg"><path d="M7 0.999023L1 5.99902L7 10.999" stroke="#58595B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>',
        nextArrow: '<button type="button" class="slick-arrow slick-next"><svg width="7" height="12" viewBox="0 0 7 12" fill="none" xmlns="https://www.w3.org/2000/svg"><path d="M1 1.9977L5.32 6.3177L1 10.6377" stroke="#58595B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>',
    });
    $("#hospital-slider").slick({
        speed: 300,
        slidesToShow: 3,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 1199,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, ],
    });
    $(".directors-slider").slick({
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 1199,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, ],
    });
    $("#heart-slider").slick({
        speed: 300,
        slidesToShow: 3,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 1199,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, ],
    });
    $(".institute-features").slick({
        speed: 300,
        slidesToShow: 2,
        slidesToScroll: 1,
        arrows: !1,
        responsive: [{
            breakpoint: 1199,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, ],
    });
    $("#sub-specialisations-slider, #sub-specialisations-slider1").slick({
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 1,
        autoplay: !0,
        autospeed: 3000,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 1199,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, ],
    });
    $(".trauma-feature-slider").slick({
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 1199,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, ],
    });
    $("#accreditations-slider").slick({
        speed: 300,
        slidesToShow: 2,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 1199,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 480,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, ],
    });
    $("#award-slider").slick({
        speed: 300,
        slidesToShow: 1,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
    });
    if (window.matchMedia("(max-width: 1280px)").matches) {
        $(".md-bannerfloat").slick({
            slidesToShow: 5,
            slidesToScroll: 1,
            autoplay: !1,
            arrows: !0,
            dots: !1,
            prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
            nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
            responsive: [{
                breakpoint: 991,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                }
            }, {
                breakpoint: 767,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    arrows: !1
                }
            }, ],
        });
        $(".services-mobile-slider").slick({
            slidesToShow: 2,
            slidesToScroll: 1,
            autoplay: !1,
            arrows: !0,
            dots: !1,
            prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
            nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
            responsive: [{
                breakpoint: 991,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            }, {
                breakpoint: 767,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }, ],
        })
    }
    $(".services-desktop-slider").slick({
        dots: !1,
        infinite: !0,
        speed: 300,
        slidesToShow: 1,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
    });
    $(".location-filter-slider").slick({
        speed: 300,
        infinite: !1,
        variableWidth: !0,
        prevArrow: '<button type="button" class="slick-arrow slick-prev"><svg width="8" height="12" viewBox="0 0 8 12" fill="none" xmlns="https://www.w3.org/2000/svg"><path d="M7 0.999023L1 5.99902L7 10.999" stroke="#58595B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>',
        nextArrow: '<button type="button" class="slick-arrow slick-next"><svg width="7" height="12" viewBox="0 0 7 12" fill="none" xmlns="https://www.w3.org/2000/svg"><path d="M1 1.9977L5.32 6.3177L1 10.6377" stroke="#58595B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>',
    });
    setTimeout(function() {
        let currItem = $(".location-filter-slider.slick-initialized").find(".slick-slide:not(.slick-cloned) > a.theme-button:not(.button-outline)").parent().attr("data-slick-index");
        $(".location-filter-slider").slick("slickGoTo", currItem)
    }, 600);
    $("#story-video-slider").slick({
        dots: !1,
        infinite: !0,
        speed: 300,
        slidesToShow: 2,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 600,
            settings: {
                mobileFirst: !0,
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }],
    });
    $("#news-slider").slick({
        slidesToShow: 2,
        slidesToScroll: 1,
        autoplay: !1,
        arrows: !0,
        dots: !1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 767,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }],
    });
    if (window.matchMedia("(max-width: 767px)").matches) {
        $("#hospital-slider").slick("refresh");
        $("#updates-slider").slick("refresh");
        $(".news-tab-slider").slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            autoplay: !1,
            arrows: !0,
            dots: !1,
            prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
            nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        });
        $(".sliderrefress").click(function() {
            $("#tabs-content").hide();
            $(".news-tab-slider").slick("refresh");
            setTimeout(function() {
                $(".news-tab-slider").slick("refresh");
                $("#tabs-content").show()
            }, 400)
        })
    }
    $("#wellness-slider").slick({
        speed: 300,
        slidesToShow: 3,
        arrows: !0,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 1024,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 991,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, ],
    });
    $("#home-award-slider").slick({
        speed: 300,
        slidesToShow: 3,
        arrows: !0,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 1024,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 991,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: !1
            }
        }, ],
    });
    $(".distinctive-specialities-slider").slick({
        speed: 300,
        slidesToShow: 3,
        arrows: !0,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 1199,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, ],
    });
    $("#types-organ-donation").slick({
        speed: 300,
        slidesToShow: 3,
        infinite: !1,
        slidesToScroll: 1,
        prevArrow: "<button type='button' class='slick-arrow slick-prev'><img src='/static/base/images/icons/vector-left.png' alt='Previous' width='6' height='10' /></button>",
        nextArrow: "<button type='button' class='slick-arrow slick-next'><img src='/static/base/images/icons/vector-right.png' alt='Next' width='6' height='10' /></button>",
        responsive: [{
            breakpoint: 1199,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1
            }
        }, {
            breakpoint: 767,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1
            }
        }, ],
    });
    $(".eqslides-height").each(function() {
        var thiss = $(this);
        var heightt = thiss.find(".slick-track").innerHeight();
        thiss.find(".eqheight").innerHeight(heightt)
    });
    $(window).on("resize", function(e) {
        $(".eqslides-height").each(function() {
            var thiss = $(this);
            var heightt = thiss.find(".slick-track").innerHeight();
            thiss.find(".eqheight").innerHeight(heightt)
        })
    });
    $(".selectfield-style .default-item").click(function() {
        if ($(this).parents(".selectfield-style").hasClass("active")) {
            $(this).parents(".selectfield-style").removeClass("active")
        } else {
            $(".selectfield-style.active").removeClass("active");
            $(this).parents(".selectfield-style").addClass("active")
        }
    });
    $(".selectfield-style .option-list li").click(function() {
        $(this).parents(".selectfield-style").removeClass("active")
    });
    $(".custom-tab:not(.redirect)").click(function(e) {
        e.preventDefault();
        var id = $(this).attr("href");
        $(this).parents("section").find(".custom-tabs ul li a.active, .custom-tab-content .custom-tab-panel .custom-tab.active").removeClass("active");
        $(this).parents("section").find(".custom-tab-content .custom-tab-panel.active").removeClass("active");
        $(this).addClass("active");
        $(".reports-slider.slick-initialized").slick("refresh");
        $(".custom-tab-content .custom-tab-panel" + id).addClass("active")
    });
    $(".toggle-menu").click(function(e) {
        e.preventDefault();
        $(this).toggleClass("active");
        $(".site-header nav").toggleClass("is-opened");
        $("body").toggleClass("hidden-overlfow")
    });
    $(".sticky-btn").click(function() {
        $(".sticky-icon").toggleClass("active")
    });
    $("nav .menu .open-submenu").click(function(e) {
        e.preventDefault();
        if ($(this).parent().hasClass("active")) {
            $(this).parent().removeClass("active")
        } else {
            $(this).parent().siblings().removeClass("active");
            $(this).parent().addClass("active")
        }
    });
    $(".why-medanta .why-list .click-circle").click(function() {
        var imgg = $(this).attr("datasrc");
        console.log(imgg);
        $(".center-image").attr("src", imgg);
        $(".center-image").addClass("isloading");
        setTimeout(function() {
            $(".center-image").removeClass("isloading")
        }, 800)
    });
    $(".faq-wrap .faq-title").click(function() {
        if ($(this).parent().hasClass("expanded")) {
            $(this).parent().removeClass("expanded")
        } else {
            $(".faq-wrap.expanded").removeClass("expanded");
            $(this).parent().addClass("expanded")
        }
    });
    $(document).on("click", ".sidebar-accordion > ul > li > a", function(e) {
        e.preventDefault();
        if ($(this).parent().hasClass("active")) {
            $(this).parent().removeClass("active")
        } else {
            $(".sidebar-accordion ul li.active").removeClass("active");
            $(this).parent().addClass("active")
        }
    });
    $(".accor-heading").on("click", function() {
        if ($(this).hasClass("active")) {
            $(this).removeClass("active");
            $(this).siblings(".accor-collepse-wraper").slideUp()
        } else {
            $(".accor-heading").removeClass("active");
            $(this).addClass("active");
            $(".accor-collepse-wraper").slideUp();
            $(this).siblings(".accor-collepse-wraper").slideDown()
        }
    });
    $(document).on("mouseup", ".shareaholic-service-copy_link", function() {
        $("#sharedrprofile").removeClass("open")
    });
    $("#tabs-nav li:first-child").addClass("active");
    $(".tab-content").hide();
    $(".tab-content:first").show();
    $("#tabs-nav li").click(function() {
        $("#tabs-nav li").removeClass("active");
        $(this).addClass("active");
        $(".tab-content").hide();
        var activeTab = $(this).find("a").attr("href");
        $(activeTab).fadeIn();
        $(".news-tab-slider.slick-initialized").slick("refresh");
        return !1
    });
    $(".content-holder .more-content .read-more").click(function() {
        $(this).parents(".content-holder").find(".more-content").removeClass("show");
        $(this).parents(".content-holder").find(".less-content").addClass("show")
    });
    $(".content-holder .less-content .read-less").click(function() {
        $(this).parents(".content-holder").find(".less-content").removeClass("show");
        $(this).parents(".content-holder").find(".more-content").addClass("show")
    });
    $(document).on("scroll", onScroll);
    if ($(window).width() > 1199) {
        $('.sticky-links a[href^="#"]').on("click", function(e) {
            e.preventDefault();
            $("html, body").animate({
                scrollTop: $($(this).attr("href")).offset().top - 124
            }, 500)
        })
    } else {
        $('.sticky-links a[href^="#"]').on("click", function(e) {
            e.preventDefault();
            $("html, body").animate({
                scrollTop: $($(this).attr("href")).offset().top - 104
            }, 500)
        })
    }
});
function onScroll(event) {
    var scrollPos = $(document).scrollTop();
    if ($(window).width() > 1199) {
        $('.sticky-links a[href^="#"]').each(function() {
            var currLink = $(this);
            var refElement = $(currLink.attr("href"));
            if (refElement.position().top - 134 <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
                $(".sticky-links ul li a").removeClass("active");
                currLink.addClass("active")
            } else {
                currLink.removeClass("active")
            }
        })
    } else {
        $('.sticky-links a[href^="#"]').each(function() {
            var currLink = $(this);
            var refElement = $(currLink.attr("href"));
            if (refElement.position().top - 124 <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
                $(".sticky-links ul li a").removeClass("active");
                currLink.addClass("active")
            } else {
                currLink.removeClass("active")
            }
        })
    }
}
var a = 0;
$(window).scroll(function() {
    var container = $('#stats-counter[style*="visibility: visible"]');
    if (container.length) {
        var oTop = $("#stats-counter").offset().top - window.innerHeight;
        if (a == 0 && $(window).scrollTop() > oTop) {
            $(".count").each(function() {
                var $this = $(this)
                  , countTo = $this.attr("data-count");
                $({
                    countNum: $this.text()
                }).animate({
                    countNum: countTo
                }, {
                    duration: 2000,
                    easing: "swing",
                    step: function() {
                        $this.text(Math.floor(this.countNum))
                    },
                    complete: function() {
                        if (this.countNum < 10) {
                            $this.text("0" + this.countNum + "+")
                        } else {
                            $this.text(this.countNum + "+")
                        }
                    },
                })
            });
            a = 1
        }
    }
});
document.addEventListener("click", function(e) {
    var scrollbar = document.body.clientWidth - window.innerWidth + "px";
    let $target = e.target;
    if ($target.closest('[data-toggle="modal"]')) {
        e.preventDefault();
        $target = $target.closest('[data-toggle="modal"]');
        document.querySelector($target.dataset.target).classList.add("open");
        document.body.style.overflow = "hidden"
    } else if ($target.dataset.close === "modal") {
        e.preventDefault();
        $target.closest(".modal").classList.remove("open");
        document.body.style.overflow = "visible"
    }
});
function playAudio(idAudio, url) {
    let modal = document.getElementById("audio-modal");
    modal.style.display = "block";
    var a = document.getElementById(idAudio);
    a.setAttribute("src", url);
    a.play()
}
function stopAudio(idAudio) {
    let modal = document.getElementById("audio-modal");
    modal.style.display = "none";
    var a = document.getElementById(idAudio);
    a.pause();
    a.currentTime = 0
}
window.onorientationchange = function() {
    window.location.reload()
}
;
if ($(window).width() < 767) {
    const section = document.querySelector(".sticky-links ul");
    window.addEventListener("scroll", function() {
        const activeItem = $(".sticky-links ul li a.active").position();
        if (activeItem) {
            if (activeItem.left != 20) {
                section.style.transform = "translate3d(" + "-" + activeItem.left + "px, 0, 0)"
            }
        }
    })
}
$(document).ready(function() {
    $(".useraccount-menu ul li.account-dropdown a").on("click", function(e) {
        $(".account-item").toggleClass("showdropdown");
        e.stopPropagation()
    });
    $(document).on("click", function(e) {
        if ($(e.target).is(".useraccount-menu ul li.account-dropdown a") === !1) {
            $(".account-item").removeClass("showdropdown")
        }
    })
});
let calcScrollValue = () => {
    let scrollProgress = document.getElementById("backtotop");
    let progressValue = document.getElementById("backtotop-value");
    let pos = document.documentElement.scrollTop;
    let calcHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    let scrollValue = Math.round((pos * 100) / calcHeight);
    if (pos > 100) {
        scrollProgress.style.display = "grid"
    } else {
        scrollProgress.style.display = "none"
    }
    scrollProgress.style.background = `conic-gradient(#F04E30 ${scrollValue}%, #d7d7d7 ${scrollValue}%)`
}
;
window.onscroll = calcScrollValue;
window.onload = calcScrollValue
