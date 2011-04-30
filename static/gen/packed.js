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
window.log = function(){
  log.history = log.history || [];  
  log.history.push(arguments);
  arguments.callee = arguments.callee.caller;  
  if(this.console) console.log( Array.prototype.slice.call(arguments) );
};
(function(b){function c(){}for(var d="assert,count,debug,dir,dirxml,error,exception,group,groupCollapsed,groupEnd,info,log,markTimeline,profile,profileEnd,time,timeEnd,trace,warn".split(","),a;a=d.pop();)b[a]=b[a]||c})(window.console=window.console||{});



$(document).ready(function(){
	/* The code here is executed on page load */
	
	/* Replacing all the paragraphs */
	$('.main p').replaceWith(function(){
	
		/* The style, class and title attributes of the p are copied to the slideout: */
		
		return '\
		<div class="slideOutTip '+$(this).attr('class')+'" style="'+$(this).attr('style')+'">\
			\
			<div class="tipVisible">\
				<div class="tipIcon"><div class="plusIcon"></div></div>\
				<p class="tipTitle">'+$(this).attr('title')+'</p>\
			</div>\
			\
			<div class="slideOutContent">\
				<p>'+$(this).html()+'</p>\
			</div>\
		</div>';
	});

	$('.slideOutTip').each(function(){

		/*
			Implicitly defining the width of the slideouts according to the width of its title,
			because IE fails to calculate it on its own.
		*/
		
		$(this).width(40+$(this).find('.tipTitle').width());
	});
	
	/* Listening for the click event: */
	
	$('.tipVisible').bind('click',function(){
		var tip = $(this).parent();
		
		/* If a open/close animation is in progress, exit the function */
		if(tip.is(':animated'))
			return false;

		if(tip.find('.slideOutContent').css('display') == 'none')
		{
			tip.trigger('slideOut');
		}
		else tip.trigger('slideIn');

	});
	
	$('.slideOutTip').bind('slideOut',function(){

		var tip = $(this);
		var slideOut = tip.find('.slideOutContent');
		
		/* Closing all currently open slideouts: */
		$('.slideOutTip.isOpened').trigger('slideIn');
		
		/* Executed only the first time the slideout is clicked: */
		if(!tip.data('dataIsSet'))
		{
			tip	.data('origWidth',tip.width())
				.data('origHeight',tip.height())
				.data('dataIsSet',true);
			
			if(tip.hasClass('openTop'))
			{
				/*
					If this slideout opens to the top, instead of the bottom,
					calculate the distance to the bottom and fix the slideout to it.
				*/
				
				tip.css({
					bottom	: tip.parent().height()-(tip.position().top+tip.outerHeight()),
					top		: 'auto'
				});
				
				/* Fixing the title to the bottom of the slideout, so it is not slid to the top on open: */
				tip.find('.tipVisible').css({position:'absolute',bottom:3});
				
				/* Moving the content above the title, so it can slide open to the top: */
				tip.find('.slideOutContent').remove().prependTo(tip);
			}
			
			if(tip.hasClass('openLeft'))
			{
				/*
					If this slideout opens to the left, instead of right, fix it to the
					right so the left edge can expand without moving the entire div:
				*/
				tip.css({
					right	: Math.abs(tip.parent().outerWidth()-(tip.position().left+tip.outerWidth())),
					left	: 'auto'
				});
				
				tip.find('.tipVisible').css({position:'absolute',right:3});
			}
		}
		
		/* Resize the slideout to fit the content, which is then faded into view: */
		
		tip.addClass('isOpened').animate({
			width	: Math.max(slideOut.outerWidth(),tip.data('origWidth')),
			height	: slideOut.outerHeight()+tip.data('origHeight')
		},function(){
			slideOut.fadeIn();
		});

	}).bind('slideIn',function(){
		var tip = $(this);

		/* Hide the content and restore the original size of the slideout: */
		
		tip.find('.slideOutContent').fadeOut('fast',function(){
			tip.animate({
				width	: tip.data('origWidth'),
				height	: tip.data('origHeight')
			},function(){
				tip.removeClass('isOpened');
			});
		});

	});
});

/*!
 * jquery.ui.potato.menu
 * 
 * Copyright (c) 2009-2010 makoto_kw, http://www.makotokw.com
 * Licensed under the MIT license.
 * 
 * @author makoto_kw
 * @version 1.0
 */
(function($) {
	$.fn.extend({
		ptMenu:function(arg) {
			var defaltOption = {
				vertical:false,
				menuItemSelector: 'li',
				menuGroupSelector: 'ul',
				firstClass:'potato-menu',
				menuItemClass:'potato-menu-item',
				menuGroupClass:'potato-menu-group',
				verticalClass:'potato-menu-vertical',
				holizontalClass:'potato-menu-holizontal',
				hasVerticalClass:'potato-menu-has-vertical',
				hasHolizontalClass:'potato-menu-has-holizontal',
				showDuration: 350,
				hideDuration: 100
			}
			
			var option = (typeof(arg)!='string') ? $.extend(defaltOption,arg) : $.extend(defaltOption,{});
			var $menu = $(this).addClass(option.firstClass).addClass((option.vertical) ? option.verticalClass : option.holizontalClass);
			var $menuItems = $menu.find(option.menuItemSelector).addClass(option.menuItemClass);
			var $menuGroups = $menu.find(option.menuGroupSelector).addClass(option.menuGroupClass);
			$menuGroups.parent().each(function(index){
				var bottom = $(this).parent(option.menuGroupSelector+'.'+option.firstClass).length == 1 && !option.vertical;
				var $menuGroup = $(this).addClass((bottom) ? option.hasVerticalClass : option.hasHolizontalClass)
					.children(option.menuGroupSelector+':first').addClass(option.verticalClass)
				$(this)
					.hover(
						function(e) {
							var offset = (bottom) ? {left:'0',top:''} : {left:$(this).width()+'px',top:'0'};
							$menuGroup.css({left:offset.left,top:offset.top}).fadeIn(option.showDuration);
						},
						function(e) {
							$menuGroup.fadeOut(option.hideDuration);
						}
					)
				;
			});
			$menu.find('a[href^="#"]').click(function() {
				$menuGroups.fadeOut(option.hideDuration);
				return ($(this).attr('href')=='#') ? false : true;
			})
			;
			return this;
		}
	})
})(jQuery);