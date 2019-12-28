// $(selector).animate({params},speed,callback);

// działa: 
// $(".project").hover( function() {
//     $(".project-row").css( "visibility", "visible" )
// }, 
//     function() {
//         $(".project-row").css( "visibility", "collapse" )
//     });

// dziala:
// $(".project").hover( function() {
//         $(".project-row").animate({ opacity: "1"}, 10000)
// })

// // działa, ale działa na wszystkich jednocześnie
// $(".project").hover(function(){
// 	if (!$(".project-row").hasClass('animated')) {
//         $(".project-row").dequeue().stop().animate({ opacity: "1" }, 300);
// 	}
// }, function() {
//     $(".project-row").addClass('animated').animate({ opacity: "0" }, 300, function() {
// 		$(".project-row").removeClass('animated').dequeue();
// 	});
// });


// children() działa tylko raz? 
// $(".project").hover(function(){
// 	if (!$(this).children(".project-row").hasClass('animated')) {
//         $(this).children(".project-row").dequeue().stop().animate({ opacity: "1" }, 300);
// 	}
// }, function() {
//     $(this).children(".project-row").addClass('animated').animate({ opacity: "0" }, 300, function() {
// 		$(this).children(".project-row").removeClass('animated').dequeue();
// 	});
// });

$(".project").hover( function() {
    $(this).children(".project-row").animate({ opacity: "1" }, 300).dequeue()
}, 
    function() {
        $(this).children(".project-row").animate({ opacity: "0" }, 300).dequeue()
    });