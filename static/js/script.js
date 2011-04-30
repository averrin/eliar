/* Author:
    Averrin
 */
function notification(msg){
    $('.notification .msg').html(msg)
            $('.notification').fadeIn()
}


$(".loginbutton, .sendform").click(function() {
    $('form').submit()
})

//        $(".regbutton").click(function({
//            $.post('/eliar/accounts/register/',$('.ik').html())
//        }))

$(".showlogin").click(function() {
    if ($('title').html() == 'Averr.in Login') {
        $('#inviteform').hide()
        $('#greeting').hide()
        $('#loginform').fadeIn('slow')
    }
    else {
        location = '/accounts/login' /*do something with this link*/
    }
})


$(".showinvite").click(function() {
        location = '/accounts/request_invite/' /*do something with this link*/
})

$('.hide').click(function() {
    $(this).parent().fadeOut()
})


$(function(){
        if ($('title').html() == 'Averr.in Login') {
        $('#inviteform').hide()
        $('#greeting').hide()
        $('#loginform').fadeIn('slow')
    }
})