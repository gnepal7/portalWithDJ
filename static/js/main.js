$(window).scroll(function() {    
    var scroll = $(window).scrollTop();
    if(scroll >= 75) {
        $(".nav").addClass("fixed");
    } else {
        $(".nav").removeClass("fixed");
    }
});

$( document ).ready(function() {

    $( '.nav_toggler' ).click(function() {
      $( 'body' ).toggleClass( 'over' );
      $( '.nav_ul' ).toggleClass( 'on_mobile' );  
      $(this).toggleClass( 'close' );   
    });

    if ($(window).width()<767) {
      $(".drop").click(function(){
        $(this).toggleClass('with-drop')
        $(this).children(".submnu").toggleClass("show");          
      });
    }
    else {
      $(".drop").hover(function(){
        $(this).toggleClass('with-drop')
        $(this).children(".submnu").toggleClass("show");
      });      
    } 



    $(".today-pic").owlCarousel({
     loop: true,
     autoplay: false,
     margin: 0,
     items: 1,
     dot: true,
     nav: false,
     autoplayTimeout: 5000,
     lazyLoad:true,
     navText: [
     "<i class='fa fa-arrow-left'></i>",
     "<i class='fa fa-arrow-right'></i>",
     ],
    });

    

    // add active class on current menu item
    // var url = window.location; 
    // var element = $('ul.nav_ul a').filter(function() {    
    // return this.href == url || url.href.indexOf(this.href) == 1; }).parent().addClass('active');

});