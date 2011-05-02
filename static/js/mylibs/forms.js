jQuery.noConflict();

jQuery(function($){

    var form = $('#formContainer form');

    form.zinePretifyForm();

    form.submit(handleFormSubmit);
    form.find('input[type=submit]').click(handleFormSubmit);

    var submitFlag = false;

    function handleFormSubmit(){
        if(submitFlag){
            return false;
        }
        overlay.show();
        submitFlag = true;

        $.post('./',form.serialize(),function(msg){
            submitFlag = false;
            overlay.hide();
            $('span.errorIcon').remove();

            if(msg.success){
                $('#formContainer').fadeOut(function(){
                    form.get(0).reset();
                    $('#thankYou').fadeIn();
                });
            }
            else {
                $.each(msg,function(k,v){

                    var errorIcon = $('<span>',{className:'errorIcon'});
                    var errorTip = $('<span>',{className:'errorTip',text:v}).hide().appendTo(errorIcon);

                    errorIcon.hover(function(){
                        errorTip.stop().fadeIn(function(){
                            errorTip.css('opacity',1);
                        });
                    },function(){
                        errorTip.stop().fadeOut('slow',function(){
                            errorTip.hide().css('opacity',1);
                        });
                    });

                    form.find('[name='+k+']').closest('.formRow').append(errorIcon);

                    if($(window).width() - errorIcon.offset().left > 240){
                        errorTip.css('left',30);
                    }
                    else {
                        errorTip.css('right',30);
                    }
                });
            }
        },'json');

        return false;
    }

    var overlay = {
        show    : function(){
            $('body').append('<div id="overlay"></div><div id="preloader">Working..</div>');
        },
        hide    : function(){
            $('#overlay,#preloader').remove();
        }
    }

    function displayOverlay(){
    }

});

(function($){

    $.fn.zinePretifyForm = function(){
        return this.each(function(){

            var form = $(this);

            form.find('input[type=button],input[type=submit]').each(function(){

                var originalButton = $(this),
                    button = $('<span>',{
                        className   : 'button',
                        html        : originalButton.val()+'<span></span>'
                    });

                button.insertAfter(originalButton.hide());

                button.click(function(){
                    originalButton.click();
                });

            });

            form.find('input[type=checkbox]').each(function(){

                var originalCheckBox = $(this),
                    checkBox = $('<span>',{
                        className   : 'checkBox '+(this.checked?'checked':'')
                    });

                checkBox.insertAfter(originalCheckBox.hide());

                checkBox.click(function(){
                    checkBox.toggleClass('checked');
                    originalCheckBox.attr('checked',checkBox.hasClass('checked'));
                });

            });

            form.find('input[type=radio]').each(function(){

                var originalRadio = $(this),
                    radio = $('<span>',{
                        className   : 'radio '+(this.checked?'checked':'')
                    });

                radio.insertAfter(originalRadio.hide());

                radio.click(function(){
                    $('input[type=radio][name='+originalRadio.attr('name')+']').each(function(){
                        $(this).next().removeClass('checked');
                    });

                    radio.addClass('checked');
                    originalRadio.attr('checked',true);
                });

            });

            form.find('select').each(function(i){

                var select = $(this);

                var selectBoxContainer = $('<span>',{
                    width       : select.outerWidth(),
                    className   : 'selectContainer',
                    html        : '<div class="selectBox"></div><span></span>',
                    css         : {zIndex : 1000-i}
                });

                var dropDown = $('<ul>',{className:'dropDown'});
                var selectBox = selectBoxContainer.find('.selectBox');

                select.find('option').each(function(i){
                    var option = $(this);

                    if(i==select.attr('selectedIndex')){
                        selectBox.html(option.text());
                    }

                    var li = $('<li>',{
                        html:   option.html()
                    });

                    li.click(function(){

                        selectBox.html(option.text());
                        dropDown.trigger('hide');

                        select.val(option.val());
                        return false;
                    });

                    dropDown.append(li);
                });

                selectBoxContainer.append(dropDown.hide());
                select.hide().after(selectBoxContainer);

                dropDown.bind('show',function(){

                    if(dropDown.is(':animated')){
                        return false;
                    }

                    selectBox.addClass('expanded');
                    dropDown.slideDown('fast');

                }).bind('hide',function(){

                    if(dropDown.is(':animated')){
                        return false;
                    }

                    selectBox.removeClass('expanded');
                    dropDown.slideUp('fast');

                }).bind('toggle',function(){
                    if(selectBox.hasClass('expanded')){
                        dropDown.trigger('hide');
                    }
                    else dropDown.trigger('show');
                });

                selectBoxContainer.click(function(){
                    dropDown.trigger('toggle');
                    return false;
                });

                $(document).click(function(){
                    dropDown.trigger('hide');
                });
            });

        });
    }

})(jQuery);