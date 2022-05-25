$(document).ready(function (){
    $('.slider').slick({
        arrows:true,
        adaptiveHeight: true,
        slidesToShow: 3,
        speed:1250,
        autoplay:true,
        autoplaySpeed: 2000,
        draggable:false,
        swipe:false,
        centerMode: true,
        variableWidth: true,
        responsive: [{
            breakpoints: 768,
            settings: {
                slidesToShow: 2
            }
        },{
            breakpoints: 480,
            settings: {
                slidesToShow: 1
            }
        }]
    });
});