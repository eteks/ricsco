/**
 * list filter collapse for admin
 * Fancier version https://gist.github.com/985283
 * 
 * @author  Karthikesh
 * @since   02/05/2014
 * 
 */

;(function($){ $(document).ready(function(){
    $('#changelist-filter').children('h3').each(function(){
        var $title = $(this);
        $title.css('cursor', 'pointer')
        .click(function(){
            $title.next().slideToggle();
        });
    });   
  });
})(django.jQuery);