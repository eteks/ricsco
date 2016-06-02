$(document).ready(function() {
     $("#phone_number").keypress(function (e) {
     //if the letter is not digit then display error and don't type anything
     if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
         return false;
    }
   });

    // Let's get a new form validator
    // Arguments: (boolean isSilent, text field error class, label error class, select error class, error display element class)
    var sfFV = new FieldValidator(false, "inputError", "labelError", "selectError");

    // Add all the required fields
    // Arguments (ID, Type[select, checkbox, usPhone, email, zip, date, radio], Guide Text, Required?)
    sfFV.add("fname", "", "Name", true);
    sfFV.add("company_name", "", "Company", true);
    sfFV.add("email", "email", "Email", true);
    sfFV.add("phone_number", "", "Phone", true);
    //cfFv.add("message", "", "Message" , true);

    // Setup the validation on submits
    $("#home_signup_form").live('submit', function(e) {
        if (sfFV.validate()) {
            // if ($('.signup_btn').attr('data-emailexist') == 'true') {
            //     $('.email_input_act').addClass("inputError");

            //     $('.join_form label.error_label').show();
            //     // event.preventDefault();
            //     return false;
            // } else {
            //     // document.banner_signup_form.submit();
            //     return true;
            // }
            document.banner_signup_form.submit();
            // alert ("validate");
             return true
        } else {
            return false;
            // event.preventDefault();
        }
    });
    
    // Setup the validation on submits
       $("#joinNow_form").live('submit', function(e) {
          if (sfFV.validate()) {
           
           if ($('.invite_btn').attr('data-emailexist') == 'true') {
          
           
           $('.email_input_act').addClass("inputError");
           
           $('.invite_form label.error_label').show();
           // event.preventDefault();
           return false;
           } else {
           // document.banner_signup_form.submit();
           return true;
           }
           // document.banner_signup_form.submit();
           } else {
           return false;
           // event.preventDefault();
           }
    });
       
       
       $("#joinNow_form_banner").live('submit', function(e) {
          if (sfFV.validate()) {
           
           if ($('.invite_btn').attr('data-emailexist') == 'true') {
          
           
           $('.email_input_act').addClass("inputError");
           
           $('.join_form label.error_label').show();
           // event.preventDefault();
           return false;
           } else {
           // document.banner_signup_form.submit();
           return true;
           }
           // document.banner_signup_form.submit();
           } else {
           return false;
           // event.preventDefault();
           }
    });
       
       
       
       var baFV = new FieldValidator(false, "inputError", "labelError", "selectError");

       // Add all the required fields
       // Arguments (ID, Type[select, checkbox, usPhone, email, zip, date, radio], Guide Text, Required?)
       baFV.add("fname1", "", "Name", true);
       baFV.add("company_name1", "", "Company", true);
       baFV.add("email1", "email", "Email", true);
       baFV.add("phone_number1", "", "Phone", true);
       
       
       $("#joinNow_form_banner_mob").live('submit', function(e) {
          if (baFV.validate()) {
           
           if ($('.invite_btn').attr('data-emailexist') == 'true') {
          
           
           $('.email_input_act').addClass("inputError");
           
           $('.invite_form label.error_label').show();
           // event.preventDefault();
           return false;
           } else {
           // document.banner_signup_form.submit();
           return true;
           }
           // document.banner_signup_form.submit();
           } else {
           return false;
           // event.preventDefault();
           }
    });
    
    
    // Validation for partner registration
    $("[name='partner_registration']").live('click', function(e) {
        $('.errorlist').html('')
        if (sfFV.validate()) {
            $(this).parents('#seller_registration').submit();
        } else {
            $('#fname, #company_name, #email, #phone_number').addClass("inputError");
            event.preventDefault();
        }
    }); 


    var pop_reg_fv = new FieldValidator(false, "inputError", "labelError", "selectError");

    //Add all the required fields
    //Arguments (ID, Type[select, checkbox, usPhone, email, zip, date, radio], Guide Text, Required?)
    pop_reg_fv.add("fname_p", "", "Name", true);
    pop_reg_fv.add("company_name_p", "", "Company", true);
    pop_reg_fv.add("email_p", "email", "Email", true);
    pop_reg_fv.add("phone_number_p", "", "Phone", true);
    
    //Setup the validation on submits
    $("#popup_joinus_form").live('submit', function(event) {

        if (pop_reg_fv.validate()) {
            if ($('.banner_signup_form_send_p.signup_btn').attr('data-emailexist') == 'true') {
                $('.email_input_act').addClass("inputError");

                $('.join_form label.error_label').show();
                return false;
                // event.preventDefault();
            }else{
                return true;
                // $('#popup_joinus_form').submit();
            }
        } else {
            return false;
            // event.preventDefault();
        }
    }); 
   
   
   // Let's get a new form validator
   // Arguments: (boolean isSilent, text field error class, label error class, select error class, error display element class)
   var ffFV = new FieldValidator(false, "inputError", "labelError", "selectError");

   // Add all the required fields
   // Arguments (ID, Type[select, checkbox, usPhone, email, zip, date, radio], Guide Text, Required?)
   ffFV.add("filtername", "", "", true);
   //cfFv.add("message", "", "Message" , true);
   // Setup the validation on submits
 
    $(".leadrequest_detail table tr td.cols3").each(function(i){

        len=$(this).text().length;

        if(len>10){

          $(this).text($(this).text().substr(0,20)+'...');

        }
    });


    $('.user_api_login').live('click', function() {

        $('.popup_fade:first').show();

        login_form = $('#signin_popup1')
        login_form.show()
        login_form.find('input:submit').attr('name', 'fxapi_login_submit')
    });

    $('.user_playground_login').live('click', function() {

        $('.popup_fade:first').show();

        login_form = $('#signin_popup1')
        login_form.show()
        login_form.find('input:submit').attr('name', 'fxapi_playground_submit')

    });

    $(".lead_wrap_text a").each(function(i){
       len=$(this).text().length;
       if(len>10){
        $(this).text($(this).text().substr(0,35)+'...');
       }
    })

    $('.signin_alert2').click(function(){
        $('#login_window').show();
        $('#joinus_popup_content').hide();
    });

    $('#joinus_popup_window').click(function(){
        $('#login_window').hide();
        $('#joinus_popup_content').show();
    });    

    $('.lead_buy_btn').click(function (){
        $('.cart_popup_wrapper').show();      
    });

    $('.validated_msg').hide();
 
    $('input.price_validation').bind('keypress', function (e) {
        return (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) ? false : true;
    });

    $('.phoneno_validation').keyup(function() {
        var inputVal = $(this).val();
        var numericReg = /^[0-9-+()\s]+$/;
        if(!numericReg.test(inputVal)) {
            $(this).closest('div').find('.validated_msg').show();
            return false();
        }else{
            $(this).closest('div').find('.validated_msg').hide();
        }
    });
     
    $(".join_form .form_inputfileds").keydown(function(event) {
            $('#recaptcha_widget').slideDown('slow');
    });    

    $("#id_amount").keydown(function(event) {

        // Allow: backspace, delete, tab, escape, and enter
        if ( event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 || event.keyCode == 27 || event.keyCode == 13 || 
             // Allow: Ctrl+A
            (event.keyCode == 65 && event.ctrlKey === true) || 
             // Allow: home, end, left, right
            (event.keyCode >= 35 && event.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;

        } else {
            // Ensure that it is a number and stop the keypress
            if (event.shiftKey || (event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105 )) {
                event.preventDefault(); 
            }
        }

    });

    setTimeout(function() {
        if (location.hash) {
            window.scrollTo(0, 0);
        }
    }, 1);   

    $("#payment_details").submit(function(){
        if($("#id_amount").val() == '' || $("#id_amount").val() == 0) {
            alert("Please enter valid deposit amount");
            return false;
        }
        if($("#id_amount_pop").val() == '' || $("#id_amount_pop").val() == 0) {
            alert("Please enter valid deposit amount");
            return false;
        }
        $('.paypal_btn').addClass('gry_out').attr('disabled', 'disabled')
    });
    // Setup the validation on submits
    accounttype();
    editLead();
    joinus_validation();
    filter_show();
    addasfavorite();
    position_popup();
    signin_position_popup();
    leadvalidation();
    filterhideandshow();
    pagination_filter_align();
    btn_align()
    paginate_alter_text();
    left_dyanmic_height();
    help_box_expansion();
    var callus_height = $(".call_us_holder").height();  
    $(".callus_block_bg").css({'height': callus_height + "px"});
    $(".callus_block").css({'height': callus_height + "px"});
            
    setTimeout(function() {
        if (location.hash) {
            window.scrollTo(0, 0);
        }
    }, 1);

        
    $(".password_change_content").live('click', function() {
        var $change_password = $('div#change_password');
        if ($change_password.css("display") == "none")
            $change_password.slideDown();
        else
            $change_password.slideUp();
    }); 
  

    $("#changeemail").live('click', function() {
        if (!$("#userEmail").attr('readonly')) {
            email = $("#userEmail").val().trim()
            old_email = $("#userEmailhidden").val().trim()
            if (email == '' || email == old_email) {
                $("#userEmail").val(old_email)
                $("#changeStatus").css('color','red').fadeIn(500)
                    .html(gettext('Email has not been changed'))
            } else {
                $.ajax({
                    type: 'GET',
                    url: '/dashboard/emailchange/',
                    data: { 'email': email },
                    success: function(data) {
                        if (data == "True") {
                            $("#userEmailhidden").val(email)
                            $("#changeStatus").css('color','green')
                                .html(gettext('Email has been changed'))
                                .fadeIn(500).delay(5000).fadeOut(1500)
                        } else {
                            $("#userEmail").val(old_email)
                            $("#changeStatus").css('color','red').fadeIn(500)
                                .html(data)
                        }
                    },
                    error: function(){
                        $("#userEmail").val(old_email)
                        $("#changeStatus").css('color','red').fadeIn(500)
                            .html(gettext('Email has not been changed'))
                    }
                });
            }
            $("#changeemail").text(gettext("Change email"))
            $("#userEmail").attr('readonly', 'readonly')
        } else {
            $("#changeemail").text(gettext("Update"))
            $("#userEmail").attr('readonly', false)
        }
    });

    $('#change_email_form').live('submit', function(){
        $(".email_change_content").click()
        event.preventDefault();
    })

    $('#latest_lead_thumbnail > .leads_thumbnail_content:last, #latest_requestlead_thumbnail > .leads_thumbnail_content:last').addClass('last');

    $('#filter_rank, #filter_budget, #filter_deal_time, #filter_price_range, #filter_rating').attr("readonly", true);

    $(window).load(function (){
        $(".infield").inFieldLabels();
        $(".infield_p").inFieldLabels();
        $('#latest_lead_thumbnail > .leads_thumbnail_content:last, #latest_requestlead_thumbnail > .leads_thumbnail_content:last').addClass('last');
         var theHeight = $(".seller_logo img").height();
         var theWidth = $(".seller_logo img").width();
         var callus_height = $(".call_us_holder").height();
         $(".callus_block_bg").css({'height': callus_height + "px"});
         $(".callus_block").css({'height': callus_height + "px"});
        
         //place them into the image styles:
         $(".seller_logo img").css({'margin-top': -theHeight / 2 + "px", 'margin-left': -theWidth / 2 + "px"});
        
        left_dyanmic_height();
        addasfavorite();
        accounttype();
        signin_position_popup();
        pagination_filter_align();
        btn_align()
        paginate_alter_text();
        email_campaign();
        filterhideandshow();
        
        help_box_expansion();
        jQuery(".lead_details_popup, .signup_popup, .auction_popup, .forgotpassword_popup, #ask_question_popup, #thank_you_popup").center();
        $(".terms_services_popup").terms_position_center();
        
        var url = window.location.href;
                
        if (url.indexOf('/search') >= 0)
        {
            
            if($("#filterkeywordtxt").val().length>15)
            {
                valKey = jQuery.trim($("#filterkeywordtxt").val()).substring(0, 15).trim(this) + "...";
            }
            else
            {
                valKey = $("#filterkeywordtxt").val();
            }
            $( "#filterkeywordtxt" ).val(valKey)
        }

        // Code by ramu/devi for home page regn issue
        var url = window.location.href;
        if(url.indexOf('/search')>=0)
        {
            if($("#filterkeywordtxt").val().length>15)
            {
                valKey = jQuery.trim($("#filterkeywordtxt").val()).substring(0, 15).trim(this) + "...";
            }
            else
            {
                valKey = $("#filterkeywordtxt").val();  
            }
            $( "#filterkeywordtxt" ).val(valKey)   
        }
    });       


    $('.back_act').click(function(){
        parent.history.back();
        return false;
    });

    $( "#datepicker" ).datepicker();

    $('input.text_val_act, textarea.text_val_act, textarea.text_val_actt').focus(function() { 

     if( this.value == this.defaultValue ) {
      //this.value = "";
     }
     }).blur(function() {

      if( !this.value.length ) {
                //this.value = this.defaultValue;
      }
    });


    $("textarea.text_val_act").focus(function() {
       var textareaval = this.value();
       if( $(this).val() == textareaval ) {
           $(this).val("");
       }

    }).focusout(function() {
       if( $(this).val() == "" ) {
           $(this).val(textareaval);
       }      

    });               

    // modified by karthikesh on 13/11/2013, for handling 'change' event when errors exist at js part
    $(".custom_select_value_act").live('change', function() {
        $(this).closest('div').find('p').html($(this).find("option:selected").text());
        $('#action_url').attr('action', $(this).val());
    });

    $(".sales_email_custom_select_value_act").change(function() {
        $(this).closest('div').find('.sales_email').html($(this).find("option:selected").text());
    });

    $(".language_custom_select_value_act").change(function() {
        $(this).closest('div').find('.language').html($(this).find("option:selected").text());
    });

    $(".profile_custom_select_value_act").change(function() {
        $(this).closest('div').find('p#prof_country').html($(this).find("option:selected").text());
    });
    
    $(".gen_method_change").change(function() {
        $(this).closest('div').find('p#gen_method').html($(this).find("option:selected").text());
    });
    
    $(".lead_status_change").change(function() {
        $(this).closest('div').find('p#lead_status').html($(this).find("option:selected").text());
    });
    
    $(".accept_campaign_change").change(function() {
        $(this).closest('div').find('p#accept_campaign').html($(this).find("option:selected").text());
    });
    
    $(".profile_custom_select_value_act1").change(function() {
        $(this).closest('div').find('p#prof_country1').html($(this).find("option:selected").text());
    });

    // without visibility verification, it is unnecesary :)

  $("#delete_all").live('click', function(){
    if ($('#delete_all').is(':checked')){
        var val = [];
        $(':checkbox:checked[name=delete]').each(function(i){
          val[i] = $(this).val(); 
        });     
        $('#prov_delete').val(val);
        $("#delete").val(val);
        $("#req_delete").val(val);
        $("#prov_status").val(val);
        $("#req_status").val(val);
        $("#boug_delete").val(val); 
        $("#fil_delete").val(val);
        $("#fil_status").val(val);
        }
    });
    $(".checkbox_edit_act").change(function () {
        $(".mySelectAll").attr("checked", $(this).is(""));
        var lead_id = $(this).val();
        $("#delete").val(lead_id);
        var val = [];
        $(':checkbox:checked[name=delete]').each(function(i){
          val[i] = $(this).val(); 
        });
        $('#prov_delete').val(val);
        $("#req_delete").val(val);
        $("#prov_status").val(val);
        $("#req_status").val(val);
        $("#fil_delete").val(val);
        $("#fil_status").val(val);
        $('.change_status').removeClass('gry_out');
        $('.change_status_req').removeClass('gry_out');
        $('.providelead_delete').removeClass('gry_out');
        $('.requestslead_delete').removeClass('gry_out');
        $('.boughtlead_delete').removeClass('gry_out');
        $('.edit_requestedlead_link').removeClass('gry_out');
        $('.edit_lead_link').removeClass('gry_out');
        $('.filter_delete').removeClass('gry_out');
        $('.filter_status').removeClass('gry_out');
        $('.subscription_delete').removeClass('gry_out');
        $('.subscription_status').removeClass('gry_out');
        $("#boug_delete").val(val);
        if ($("input.checkbox_edit_act:checked").length >= 2 ) {
            $(".edit_list").hide();
        } else {
            $('.edit_requestedlead_link').removeClass('gry_out');
            $('.edit_lead_link').removeClass('gry_out');
            // without visibility verification, it is unnecesary :)
            $(".edit_list").show();
            $('[data-leadeditlink]').each(function(){
                var link = $(this).attr('data-leadeditlink');
                if($(this).is(':checked')){
                    $('.edit_lead_link').attr('href', link);
                    $('.change_status').addClass('change_status_popup_act');
                    $('.change_status_req').addClass('change_status_req_popup_act');
                    $('.providelead_delete').addClass('provide_lead_delete_act');
                    $('.requestslead_delete').addClass('requests_lead_delete_act');
                    $('.filter_delete').addClass('delete_warning_filters_act');
                    $('.filter_status').addClass('status_filters_act');
                    $('.change_status').removeClass('gry_out');
                    $('.change_status_req').removeClass('gry_out');
                    $('.providelead_delete').removeClass('gry_out');
                    $('.requestslead_delete').removeClass('gry_out');
                    $('.boughtlead_delete').removeClass('gry_out');
                    $('.edit_requestedlead_link').removeClass('gry_out');
                    $('.edit_lead_link').removeClass('gry_out');
                    $('.filter_delete').removeClass('gry_out');
                    $('.filter_status').removeClass('gry_out');
                    $('.subscription_delete').removeClass('gry_out');
                    $('.subscription_status').removeClass('gry_out');
                    
                    return false;
                } else{
                    $('.edit_lead_link').attr('href', 'javascript:alert("Please select a lead to edit")');
                    $('.change_status').removeClass('change_status_popup_act');
                    $('.change_status_req').removeClass('change_status_req_popup_act');
                    $('.providelead_delete').removeClass('provide_lead_delete_act');
                    $('.requestslead_delete').removeClass('requests_lead_delete_act');
                    $('.filter_delete').removeClass('delete_warning_filters_act');
                    $('.filter_status').removeClass('status_filters_act');
                    $('.change_status').addClass('gry_out');
                    $('.change_status_req').addClass('gry_out');
                    $('.providelead_delete').addClass('gry_out');
                    $('.requestslead_delete').addClass('gry_out');
                    $('.boughtlead_delete').addClass('gry_out');
                    $('.edit_requestedlead_link').addClass('gry_out');
                    $('.edit_lead_link').addClass('gry_out');
                    $('.filter_delete').addClass('gry_out');
                    $('.filter_status').addClass('gry_out');
                    $('.subscription_delete').addClass('gry_out');
                    $('.subscription_status').addClass('gry_out');

                }
            });
                    
            $('[data-reqleadeditlink]').each(function(){
                var link = $(this).attr('data-reqleadeditlink');
                if($(this).is(':checked')){
                    $('.edit_requestedlead_link').attr('href', link);
                    $('.change_status').addClass('change_status_popup_act');
                    $('.change_status_req').addClass('change_status_req_popup_act');
                    $('.providelead_delete').addClass('provide_lead_delete_act');
                    $('.requestslead_delete').addClass('requests_lead_delete_act');
                    $('.filter_delete').addClass('delete_warning_filters_act');
                    $('.filter_status').addClass('status_filters_act');
                    $('.change_status').removeClass('gry_out');
                    $('.change_status_req').removeClass('gry_out');
                    $('.providelead_delete').removeClass('gry_out');
                    $('.requestslead_delete').removeClass('gry_out');
                    $('.boughtlead_delete').removeClass('gry_out');
                    $('.edit_requestedlead_link').removeClass('gry_out');
                    $('.edit_lead_link').removeClass('gry_out');
                    $('.filter_delete').removeClass('gry_out');
                    $('.filter_status').removeClass('gry_out');
                    $('.subscription_delete').removeClass('gry_out');
                    $('.subscription_status').removeClass('gry_out');
                    return false;
                }else{
                    $('.edit_requestedlead_link').attr('href', 'javascript:alert("Please select a lead to edit")');
                    $('.change_status').removeClass('change_status_popup_act');
                    $('.change_status_req').removeClass('change_status_req_popup_act');
                    $('.providelead_delete').removeClass('provide_lead_delete_act');
                    $('.requestslead_delete').removeClass('requests_lead_delete_act');
                    $('.filter_delete').removeClass('delete_warning_filters_act');
                    $('.filter_status').remove('status_filters_act');
                    $('.change_status').addClass('gry_out');
                    $('.change_status_req').addClass('gry_out');
                    $('.providelead_delete').addClass('gry_out');
                    $('.requestslead_delete').addClass('gry_out');
                    $('.boughtlead_delete').addClass('gry_out');
                    $('.edit_requestedlead_link').addClass('gry_out');
                    $('.edit_lead_link').addClass('gry_out');
                    $('.filter_delete').addClass('gry_out');
                    $('.filter_status').addClass('gry_out');
                    $('.subscription_delete').addClass('gry_out');
                    $('.subscription_status').addClass('gry_out');
                    
                }
            });
        }
  });


    $(".leadselected").change(function () {
        $(".SelectAll_boughtlead").attr("checked", $(this).is(""));
        $('.leadselected').each(function(){ 
            if($(this).is(':checked')){
                $('.boughtlead_delete').addClass('bought_lead_delete_act');
                $('.change_status').addClass('change_status_popup_act');
                return false;
            } else{
                $('.boughtlead_delete').removeClass('bought_lead_delete_act');
                $('.change_status').addClass('change_status_popup_act');
                
            }
        });
    });


    $(".folders_hide_act").click(function () {
        $(".folders .toggle").slideToggle("slow");
        $('.folders_hide_act code').toggleClass("leftarrow")
    });
    
    $(".mySelectAll").click(function() {
       $("INPUT[type='checkbox'][@name='list']").attr("checked", $(this).is(":checked"));
       if ($("input.checkbox_edit_act:checked").length >= 2 ) {
            $('#edit_lead_link').attr('href', 'javascript:alert("Please select a lead to edit")');
            $('.change_status').addClass('change_status_popup_act');
            $('.change_status_req').addClass('change_status_req_popup_act');
            $('.providelead_delete').addClass('provide_lead_delete_act');
            $('.requestslead_delete').addClass('requests_lead_delete_act');
            $('.filter_delete').addClass('delete_warning_filters_act');
            $('.filter_status').addClass('status_filters_act');
            $(".edit_list").hide();
            $('.change_status').removeClass('gry_out');
            $('.change_status_req').removeClass('gry_out');
            $('.providelead_delete').removeClass('gry_out');
            $('.requestslead_delete').removeClass('gry_out');
            $('.filter_delete').removeClass('gry_out');
            $('.filter_status').removeClass('gry_out');
            $('.subscription_delete').removeClass('gry_out');
            $('.subscription_status').removeClass('gry_out');
            
       } else {
           // without visibility verification, it is unnecesary :)
           $(".edit_list").show();
           $('.change_status').removeClass('change_status_popup_act');
           $('.change_status_req').removeClass('change_status_req_popup_act');
           $('.providelead_delete').removeClass('provide_lead_delete_act');
           $('.requestslead_delete').removeClass('requests_lead_delete_act');
           $('.filter_delete').removeClass('delete_warning_filters_act');
           $('.filter_status').removeClass('status_filters_act');
           $('.change_status').addClass('gry_out');
           $('.change_status_req').addClass('gry_out');
           $('.providelead_delete').addClass('gry_out');
           $('.requestslead_delete').addClass('gry_out');
           $('.edit_requestedlead_link').addClass('gry_out');
           $('.edit_lead_link').addClass('gry_out');
           $('.filter_delete').addClass('gry_out');
           $('.filter_status').addClass('gry_out');
           $('.subscription_delete').addClass('gry_out');
           $('.subscription_status').addClass('gry_out');
       } 
    }); 
    
    $(".SelectAll_boughtlead").click(function() {      
       $("INPUT[type='checkbox'][@name='list1']").attr("checked", $(this).is(":checked"));
       updateTextArea();
       $('.leadselected').each(function(){  
            if($(this).is(':checked')){
                $('.boughtlead_delete').addClass('bought_lead_delete_act');
                $('.change_status').addClass('change_status_popup_act');
                $('.boughtlead_delete, li.export_action, li.change_status').removeClass('gry_out');
                $('li.export_action').addClass('export_popup_act');
                return false;
            } else{
                $('.boughtlead_delete').removeClass('bought_lead_delete_act');
                $('.change_status').addClass('change_status_popup_act');
                $('.boughtlead_delete, li.export_action, li.change_status').addClass('gry_out');
                $('li.export_action').removeClass('export_popup_act');
            }
        }); 
    }); 
    
    
    $('[data-leadeditlink]').change(function(){
        
    });
    
    $('[data-reqleadeditlink]').change(function(){
        var link = $(this).attr('data-reqleadeditlink');
        if($(this).is(':checked')){
            $('#edit_requestedlead_link').attr('href', link);
            $('.edit_requestedlead_link').removeClass('gry_out');
            $('.edit_lead_link').removeClass('gry_out');
        }else{
            $('#edit_requestedlead_link').attr('href', 'javascript:alert("Please select a lead to edit")');
        }
    });


    $('#go').click(function() {
       imageFiles = document.getElementById('files').files
       // get the number of files
       numFiles = imageFiles.length;
       readFile();           
    });


    function update_search_locations(){
        var str = '';
        for(var i in _selected_locations){
            str += i + ',';
        }
        $('#selected_locations').val(str);
        perform_search();
    }

    $('.add_location_act').click(function(){
        var _val = $(".location").val();
        _selected_locations[_val] = true;
        update_search_locations();
        $(".location_display_holder").show();
        $(".location_display_holder").prepend("<span><b class='delete_location' data-location='"+ _val +"'>X</b>"+_val+"</span>");
        $(".location").val('');
    });
           

    $('.delete_location').live('click',function() {
        var _val = $(this).attr('data-location');
        delete _selected_locations[_val];
        update_search_locations();
        $(this).parent().remove();

    });

    /**************detail select first word and append span ************/
    $('.prod_header h4').each(function() {
        var jqt = $(this);
        var txt = jqt.text();
        jqt.html('<span>'+txt.substring(0,(txt.indexOf(" ")))+'</span>'+ txt.substring((txt.indexOf(" "))));

    });

    $(".location").keypress(function () {
        $('.location_holder ul').show();
    });

    $('.location_holder ul').find('li').live('click',function() {
        var field_value = $(this).text();
        $(this).parent().parent().children('input').val(field_value);
        $(this).parent().hide();
    });

    $('body').click(function(){
        var wrappclass = $('body').attr("class");
        if (wrappclass == 'wrappflag'){
            $('.location_holder').find('ul').hide(); 
            $('body').removeClass('wrappflag');
        }
    });

    /*************rating**********/
    $(".rating_display span").click(function(){    
        $(".rating_display span").toggle(function(){ 
                $(this).removeClass("default_rating");
                $(this).addClass("review_selected");
                $(this).prevAll().removeClass("default_rating");                   
                $(this).prevAll().addClass("review_selected");
                $(this).nextAll().removeClass("review_selected");                
                $(this).nextAll().addClass("default_rating");
         },function(){                        
            $(this).nextAll().removeClass("review_selected");                
            $(this).nextAll().addClass("default_rating");
        });
    });

    $('.steps_navigation_tab .steps_wrapper').click ( function () {
                $('.back2top').trigger('click'); 
                $('.steps_navigation_tab .steps_wrapper').removeClass('steps_active');
                $(this).addClass('steps_active');
                $('.tabs_act').hide();
                $("."+$(this).attr("id")).show();
    });

     $('.add_lead_step2 .show_more_details_act').click (function() {
                            left_dyanmic_height();
                            $(".add_lead_step2 .show_more_details_content").slideToggle('slow');
                            $(this).text($(this).text() == gettext('Show more details') ? gettext('Show less details') : gettext('Show more details')); // <- HERE
                return false;
     });

      $('.add_lead_step3 .show_more_details_act1').click (function() {
                           left_dyanmic_height();
                            $(".add_lead_step3 .show_more_details_content1").slideToggle('slow');
                            $(this).text($(this).text() == gettext('Show more details') ? gettext('Show less details') : gettext('Show more details')); // <- HERE
                return false;
     });

         

     $('.reset_act').live('click', function() {
                $(this).closest('form').find('input[type=text], textarea, select').val('');
     });



    $('.go_to_step2').click(function () {
        left_dyanmic_height();
        $('.back2top').trigger('click');
        $('.add_lead_step1, .add_lead_step3').hide();
        $('.add_lead_step2').show();
        $('#add_lead_step2').addClass('steps_active');
        $('#add_lead_step1, #add_lead_step3').removeClass('steps_active');
    })

    $('.go_to_step1').click(function () {
                left_dyanmic_height();
                $('.add_lead_step3, .add_lead_step2').hide();
                $('.add_lead_step1').show();
                $('#add_lead_step1').addClass('steps_active');
                $('#add_lead_step2, #add_lead_step3').removeClass('steps_active');
    })

    $('.go_to_step3').click(function () {
                left_dyanmic_height();
                $('.add_lead_step1, .add_lead_step2').hide();
                $('.add_lead_step3').show();
                $('#add_lead_step3').addClass('steps_active');
                $('#add_lead_step1, #add_lead_step2').removeClass('steps_active');
    })

    /************tabswap******************/
    $('#tabs_swap li').click ( function () {
        left_dyanmic_height();                      
        $('#tabs_swap li').removeClass('tabs_active');
        $(this).addClass('tabs_active');
        $('.tabs_act').hide();
        $("."+$(this).attr("id")).show();
        var general_tab = $('#tabs_swap').find("li").attr("class");
        if (general_tab == 'tabs_active')
            {
                left_dyanmic_height();
                $('.filter_selec_area').hide();   
            }
        else {
            left_dyanmic_height();
            $('.filter_selec_area').show();
        }         

    });

       

    $('.frequent_questions').find('div').hide();

    $('.frequent_questions ul').find('li').click(function() {
            left_dyanmic_height();
            $(this).children('div').slideDown();
            $(this).children('h3').addClass("showanwer");
            $(this).siblings().children('div').slideUp();
            $(this).siblings().children('h3').removeClass("showanwer");

     });

   /***********leadboughts append menu li****************/

   $('.bought_lead_delete_act').live('click',function() {
    $('.bought_lead_delete').show();
    $('.popup_fade:first').show();
  });
  
  $('.popup_cancel_btn').live('click',function() {
    $('.pop_up').hide();
    $('.popup_fade').hide();
  });
  
  $('.provide_lead_delete_act').live('click',function() {
    $('.provide_lead_delete').show();
    $('.popup_fade:first').show();
  });
  
   $('.requests_lead_add_act').click (function (){
    $('.request_new_lead').show();
    $('.edit_reqlead_link').hide();
    left_dyanmic_height();
  });
  
  $('.transaction_popup_act').click (function (){
    $(this).find('.transaction_popup').show();
    $(this).find('.pop_up').show(); 
  });
  
  function editLead(){
    $('.edit_reqlead_link').hide();
    if($('#i_reqtitle').val() !='')
    {
        $('.edit_reqlead_link').show();
    }
    left_dyanmic_height();
  }

    $('.requests_lead_delete_act').live('click',function() {
        $('.requests_lead_delete').show();
        $('.popup_fade:first').show();
     });
    
    $('.delete_warning_subscription_act').live('click',function() {
        $('.delete_warning_subscription').show();
        $('.popup_fade:first').show();
     });

    $('.delete_warning_filters_act').live('click',function() {
        $('.filter_lead_delete').show();
        $('.popup_fade:first').show();
     });
     
    $('.status_filters_act').live('click',function() {
        $('.filter_status_popup').show();
        $('.popup_fade:first').show();
     });
    
    $('.move_popup_menu_act').live('click',function() {
        $('.move_popup_menu').show();
        $('.popup_fade:first').show();
     });

    $('.export_popup_act').live('click',function() {
        $('.export_popup').show();
        if($(this).hasClass('export_all_action') == false){
            $('#action_url>[name=all_lead_pdf]').remove()
        }
        $('.popup_fade:first').show();
     });
    $('.export_all_action').live('click',function() {
        if ($('#action_url>[name=all_lead_pdf]').length == 0){
            $('#action_url').append(
                $('<input>').attr({
                    'type': 'hidden',
                    'name': 'all_lead_pdf',
                    'value': 'all'
                }))
        }else{
            $('#action_url>[name=all_lead_pdf]').val('all')
        }
     });
    
    $('.change_status_popup_act').live('click',function() {
        $('.change_status_popup').show();
        $('.popup_fade:first').show();
     });
     
     $('.change_status_req_popup_act').live('click',function() {
        $('.change_status_req_popup').show();
        $('.popup_fade:first').show();
     });

    $('.note_popup_act').click (function (){
        $('.note_popup').show();
        $('.popup_fade:first').show();
     });

    $(".account_options input:radio[name='acc_option']").click(function() {
       $('.select_account_type_act').hide();
       $('#' + $("input:radio[name='acc_option']:checked").val()).show();
      });


  $('#deposit_act').click ( function (){
        $('.deposit_popup, .popup_fade:first').show();
  });
  // Code modified by Karthikesh on 6/11/2013, for Forgot password issue
  $('#forgotpassword_act, .forgotpassword').live('click', function (){
            $('.forgotpassword_popup, .popup_fade:first').show();
            $('[id*="signin_popup"]').hide();
  });

  $('.cancel_btn, .close_btn').live('click', function (){
    $('.deposit_popup, .popup_fade, .forgotpassword_popup, .terms_services_popup, #signin_popup, #joinus_popup_content, #signin_popup1, #email_activate, #login_window, #login_window1, .lead_details_popup, #directbuy_signin_popup, #auction_popup, #ask_question_popup, #thank_you_popup').hide();
  });

    

    $('.signin_alert').live('click', function (){
        $('.popup_fade:first').show();
        $('#signin_popup1').show();
        signin_position_popup();
        $(".banner_signup_form_send_p").attr('name', 'addtobasket_popup_reg');
    });

    $('.direct_buy_signin_alert').live('click', function (){
        $('.popup_fade:first').show();
        $('#directbuy_signin_popup').show();
        signin_position_popup();
        $(".banner_signup_form_send_p").attr('name', 'auto_buy_popup_reg');
    });

    $('.buynow_link_act').live('click', function (){
        $('.popup_fade:first').show();
        $('#signin_popup, #signin_popup1, #directbuy_signin_popup').hide();
        $('#joinus_popup_content').show();
        position_popup();
        $(".banner_signup_form_send_p").attr('name', 'addtobasket_popup_reg');
    });

    $('#joinus_popup_window1').live('click', function (){
        $('.popup_fade:first').show();
        $('#signin_popup, #signin_popup1, #directbuy_signin_popup').hide();
        $('#joinus_popup_content').show();
        position_popup();
    });

    $('.signin_alert1 ').live('click', function(){
        var has_auto_buy = window.location.href.indexOf('ler=2')
        if($(this).hasClass('basket_lead')){
            $('#signin_popup1').show();
        }else if($(this).hasClass('buynow_lead') || has_auto_buy > 0){
            $('#directbuy_signin_popup').show();
        }else{
            $('#signin_popup1').show();
        }
        $('#joinus_popup_content').hide();
        signin_position_popup();
    });

    $('.signin_alert2').live('click', function(){
        $('#login_window').show();
        $('#joinus_popup_content').hide();
    });

/**************** personal_company address **********************/

     $('#copyaddress').click(function() {
        // If checked
        if ($("#copyaddress").is(":checked")) {
            //for each input field
            $('#company_address input, #company_address textarea, #company_address select', ':visible', document.body).each(function(i) { 
                //copy the values from the billing_fields inputs
                //to the equiv inputs on the shipping_fields
                $(this).val( $('#personal_address input, #personal_address textarea, #personal_address select').eq(i).val() );
                });

            $('#company_address .select p', ':visible', document.body).each(function(i) { 
                //copy the values from the billing_fields inputs
                //to the equiv inputs on the shipping_fields
                $(this).text( $('#personal_address .select p').eq(i).text() );
                });    

            //won't work on drop downs, so get those values

        } else {
            //for each input field
            $('#company_address input, #company_address textarea, #company_address select', ':visible', document.body).each(function(i) { 
                //set shipping_fields inputs to blank
                $(this).val("");
                $("#company_address .select p").text("select");  
                });

        }

    });

 
    $(window).resize(function(){
         var theHeight = $(".seller_logo img").height();
         var theWidth = $(".seller_logo img").width();
         var callus_height = $(".call_us_holder").height();
         
        $(".lead_details_popup, .signup_popup, .auction_popup, .forgotpassword_popup, #ask_question_popup, #thank_you_popup").center();
        $(".terms_services_popup").terms_position_center();
         //place them into the image styles:
         $(".seller_logo img").css({'margin-top': -theHeight / 2 + "px", 'margin-left': -theWidth / 2 + "px"});
         
         $(".callus_block_bg").css({'height': callus_height + "px"});
         $(".callus_block").css({'height': callus_height + "px"});
         
        left_dyanmic_height();
        position_popup();
        signin_position_popup();
        accounttype();
        pagination_filter_align();
        btn_align()
        paginate_alter_text();
        help_box_expansion();
          var body_win_height = parseInt(document.body.clientHeight) ;
          var win_height = parseInt(document.documentElement.clientHeight) ;
          if( body_win_height > win_height) {
                $('.popup_fade').height(body_win_height);
          } else {
                $('.popup_fade').height(win_height);
          }
    });

    var body_win_height = parseInt(document.body.clientHeight) ;
    var win_height = parseInt(document.documentElement.clientHeight) ;
    if( body_win_height > win_height) {
        $('.popup_fade').height(body_win_height);
    } else {
        $('.popup_fade').height(win_height);
    }

     $('.save_filter_act').click (function (){
        $('.popup_fade:first').show();
        $('.save_filter_popup').show();
        //validateFilterValues()           ;          
        $( "#filterdesc" ).val('')                    
        $('#budget_start').val($('budgetstart').val())
        $('#budget_end').val($('budgetend').val())               
        $('#deal_start').val($('dealstart').val())
        $('#deal_end').val($('dealend').val())            
        $('#price_start').val($('pricestart').val())
        $('#price_end').val($('priceend').val())
        $('#rating_start').val($('ratingstart').val())
        $('#rating_end').val($('ratingend').val())                   
        $('#ranking_start').val($('rankingstart').val())
        $('#ranking_end').val($('rankingend').val())

        $('#created_start').val($('#from').val())
        $('#created_end').val($('#to').val())    

        $('#filter_location').val($('#filterlocation').val())
        $('#filter_keyword').val($('#filterkeyword').val())
        $('#filter_search').val($('#q').val())
        $('#filtersearch').val($('#q').val())   

        position_popup();
     });

     $('.reset_filter_act').click (function (){
        var b_start = 0;
        var b_end = 1000000;
        var r_start = 0;
        var r_end = 5;
        var p_start = 0;
        var p_end = 1000;
        var d_start = 0;
        var d_end = 20;
        var rat_start = 0;
        var rat_end = 5;

        resetSlider('.rank',r_start,r_end);
        resetSlider('.budget',b_start,b_end);
        resetSlider('.time',d_start,d_end);
        resetSlider('.price',p_start,p_end);
        resetSlider('.rating_act',rat_start,rat_end);

        resetHiddenvalues('#filter_rank',r_start,r_end);
        resetHiddenvalues('#filter_budget',b_start,b_end + " SEK");
        resetHiddenvalues('#filter_deal_time',d_start,d_end + gettext(" weeks"));
        resetHiddenvalues('#filter_price_range',p_start,p_end + " SEK");
        resetHiddenvalues('#filter_rating',rat_start,rat_end);

        $( "name=budget_end" ).val(b_end);
        $( "name=price_start" ).val(p_start);
        $( "name=price_end" ).val(p_end);
        $( "name=deal_start" ).val(d_start);
        $( "name=deal_end" ).val(d_end);
        $( "name=rating_start" ).val(rat_start);
        $( "name=rating_end" ).val(rat_end);
        $( "name=ranking_start" ).val(r_start);
        $( "name=ranking_end" ).val(r_end);
        $('#from').val('')
        $('#to').val('')  
        $('#filterlocation').val('')
        $('#filterkeyword').val('')
        perform_search();
     });

    $('.termsofservice_act>a').live('click', function() {
        $('.popup_fade:first').show();
        $('.terms_services_popup').show();
    }); 
             
     $('#tabs_swap li').click ( function () {
        terms_position_popup();
        $('#tabs_swap li').removeClass('tabActiveHeader');
        $(this).addClass('tabActiveHeader');
        $('.tabs_act').hide();
        $("."+$(this).attr("id")).show();
        var general_tab = $('#tabs_swap').find("li").attr("class");
        var body_win_height = parseInt(document.body.clientHeight) ;
          var win_height = parseInt(document.documentElement.clientHeight) ;
          if( body_win_height > win_height) {
            $('.popup_fade').height(body_win_height);
          } else {
            $('.popup_fade').height(win_height);
          }
    });

     $('.buy_enable_act').change(function () {
        if ($(".buy_enable_act").is(":checked")) {
            $('.terms_condition_act').removeAttr('disabled');
            $('.select_transaction').hide();
        } else {
           $('.terms_condition_act').attr('disabled', 'true');
           $('.select_transaction').show();
       } 
     });

     $('.submit_enable_act').change(function () {
        if ($(".submit_enable_act").is(":checked")) {
            $('.add_lead_enable_act').removeAttr('disabled');
            $('.error_publish_msg').hide();
       } else {
           $('.add_lead_enable_act').attr('disabled', 'true');
           $('.error_publish_msg').show();
       } 
     });

    $('.addlead_submit_enable_act').live('change', function() {
        if ($(".addlead_submit_enable_act").is(":checked")) {
            $('.add_reqlead_enable_act').removeAttr('disabled');
        } else {
            $('.add_reqlead_enable_act').attr('disabled', 'disabled');
        }
    }); 
              

    $('#leadkeywords').keyup(function () {
        var TotalTags = $('#leadkeywords').val().split(',');
        if (TotalTags.length <= 10) {
            for (var Index = 0; Index < TotalTags.length; Index++) {
                if (TotalTags[Index].length <= 64) {
                }
                else {
                    // alert('Maximum charecters should be 64.');
                    TotalTags[Index] = TotalTags[Index].substr(0, TotalTags[Index].length - 1);
                    var TagValue = "";
                    for (var i = 0; i < TotalTags.length; i++) {
                        TagValue += TotalTags[i] + ","
                    }
                    TagValue = TagValue.substr(0, TagValue.length - 1);
                    $('#leadkeywords').val(TagValue);
                    return false;
                }
            }
        }
        else {
            $('#leadkeywords').val($('#leadkeywords').val().substr(0, $('#leadkeywords').val().length - 1))
            return false;
        }
    });
    if ($('#related_leads_table>tbody>tr').length == 0){
        $('#related_leads_block, #goto_related_lead, .related_lead_text').hide()
    }
}); /*readydocumentclosed*/

function validateFilterValues() {
    var b_start = 0;
    var b_end = 1000000;
    var r_start = 0;
    var r_end = 5;
    var p_start = 0;
    var p_end = 1000;
    var d_start = 0;
    var d_end = 20;
    var rat_start = 0;
    var rat_end = 5;
}

function resetSlider(sliderObject,minVal,maxVal) {
    var $slider = $(sliderObject);
    $slider.slider("values", 0, minVal);
    $slider.slider("values", 1, maxVal);
}

function resetHiddenvalues(sliderObject,minVal,maxVal) {
    var $slider = $(sliderObject)
    $slider.val( minVal + " to  " + maxVal);
}

function show_searching(show) {
    if(show){
        $('.loding_icon').show();
        $('.founded_no').hide();
    }else{
        $('.loding_icon').hide();
        $('.founded_no').show();
    }

}

function accounttype(){
   $('.select_account_type_act').hide();
   $('#' + $("input:radio[name='acc_option']:checked").val()).show();
}
            function perform_search(){
                        $.cookie('keywords', $('input[name=keywords]').val(),{ path: "/" });
                        $.cookie('location', $('input[name=locations]').val(),{ path: "/" });
                        left_dyanmic_height();  
                        $(".infield").inFieldLabels();
                        $(".infield_p").inFieldLabels();
                        show_searching(true);
                        $('[name=rating_start]').val('')
                        $('[name=rating_end]').val('')
                        var q = $('#form_search_filter').serialize();
                        q=decodeURIComponent(q);
                        q = q.replace(/filtersearch/g,'q');
                        var qsort = $("#sortdata").val();
                        q = q +'&sortdata='+$.trim(qsort);
                        var qlang = $("#currentlanguage").val();
                        if ($('[name=newsearch]').val() == "new")
                        
                        {
                            $.get('/search/?'+ q, function(data){
                                    show_searching(false);
                                    $('#search_result').html(data);
                                    leadfound= $('.founded_no').text().trim();
                                    if (leadfound == '')
                                        $('[name=search_founded_no]').val ('0 ' + gettext("Leads found"));
                                     else
                                         $('[name=search_founded_no]').val($('.founded_no').text().trim());
                                    attach_pagination_events();
                                   
                                    if($('[name=keywords]').val() == '')
                                        $('#keyword_highlight').hide();
                                    
                                    if($('[name=locations]').val() == '')
                                        $('#location_highlight').hide();
                            });
                        }else{
                            $.get('/search/?'+ q, function(data){
    
                                show_searching(false);
                                
                                $('#search_result').html(data);
                                leadfound= $('.founded_no').text().trim();
                                if (leadfound == '')
                                    $('[name=search_founded_no]').val ('0 ' + gettext("Leads found"));
                                 else
                                     $('[name=search_founded_no]').val($('.founded_no').text().trim());
                                attach_pagination_events();
                               
                                if($('[name=keywords]').val() == '')
                                    $('#keyword_highlight').hide();
                                
                                if($('[name=locations]').val() == '')
                                    $('#location_highlight').hide();
                                left_dyanmic_height();
                                        
                            });
                        }
                        $(document).ready(function() {
                        $('#showHiddenBlock').click(function() {
                        $('#form_search_filter').show();
                        left_dyanmic_height();
                        });
    });

}
function attach_pagination_events(){
    pagination_filter_align();
            $('[data-ajaxlink=true]').click(function(ele){
            $("html, body").animate({ scrollTop: 0 }, "slow");
                        $('[name=page]').val($(ele.currentTarget).attr('data-ajaxpage'));
                        perform_search();
                        return false;
            });
}
function filterhideandshow() {
    var shouldShow = $.cookie('show_desc') == 'yep';
    if( shouldShow ) { 
        $('.form_search_filter').show();
        $('#show_filter').hide();
        $('#hide_filter').show(); 
    }
    else { 
        $('.form_search_filter').hide();
        $('#show_filter').show();
        $('#hide_filter').hide(); 
    }
}
function show_filter(){
    $.cookie('show_desc', 'yep');
    $('.form_search_filter').show();
    $('#show_filter').hide();
    $('#hide_filter').show();
}

function hide_filters(){
    $.cookie('show_desc', 'nope');
    $('.form_search_filter').hide();
    $('#show_filter').show();
    $('#hide_filter').hide();
}

 $('#show_filter').live('click', function() {
        show_filter();
        left_dyanmic_height();
     });
 $('#hide_filter').live('click', function() {
        hide_filters();
        left_dyanmic_height();
 });    


$(function() {
            var smonth = 2 //start-month, start-year
            var b_start = 0;
            var b_end = 1000000;
            var r_start = 0;
            var r_end = 5;
            var p_start = 0;
            var p_end = 1000;
            var d_start = 0;
            var d_end = 20;
            var rat_start = 0;
            var rat_end = 5;
            var oneDay  = 24*60*60*1000;
            var currentDay = new Date();
            var dealEndDate = new Date();
            var vars = [], hash;
            var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
            if(hashes.length > 1)
            {
                       show_filter();
                        for(var i = 0; i < hashes.length; i++)
                        {
                                    hash = hashes[i].split('=');
                                    if(hash[0] == 'q' && hash[1] != '')

                                    {
                                            $('#q').val(decodeURIComponent(hash[1]));
                                            try{
                                                qValue = $('#q').val(); 
                                                // qValue = qValue.replace(/-/g,' ');
                                                while(qValue.indexOf('+') > -1)
                                                {
                                                    qValue = qValue.replace('+',' ');
                                                }
                                            }catch(e){}
                
                                            $('#q').val(qValue);
                                    }
    
                if(hash[0] == 'budget_start' && hash[1] != ''  && hash[1] != '0')

                                    {

                                                b_start = eval(hash[1]);

                                                $('[name=budget_start]').val(hash[1]);

                                    }

                if(hash[0] == 'budget_end' && hash[1] != ''  && hash[1] != '0')
                                    {

                                                b_end = eval(hash[1]);

                                                $('[name=budget_end]').val(hash[1]);

                                    }
                if(hash[0] == 'ranking_start' && hash[1] != '' && hash[1] != '0')
                                    {
                                                r_start = hash[1];
                                                $('[name=ranking_start]').val(hash[1]);
                                    }
                if(hash[0] == 'ranking_end' && hash[1] != ''&& hash[1] != '0')
                                    {
                                                r_end = hash[1];
                                                $('[name=ranking_end]').val(hash[1]);
                                    }
                if(hash[0] == 'price_start' && hash[1] != '' && hash[1] != '0')
                                    {
                                                p_start = hash[1];
                                                $('[name=price_start]').val(hash[1]);
                                    }

                if(hash[0] == 'price_end' && hash[1] != '' && hash[1] != '0')
                                    {
                                                p_end = hash[1];
                                                $('[name=price_end]').val(hash[1]);
                                    }

                                    if(hash[0] == 'deal_start' && hash[1] != '')
                                    {
                                                today=new Date();
                                                if(hash[1].indexOf('-') > 0)
                                                {
                                                            dates=hash[1].split('-');
                                                }
                                                else
                                                {
                                                            dates=hash[1].split('/');
                                                }
                                                dealstart=new Date(dates[2],dates[0]-1,dates[1]);
                                                diffDays = (dealstart.getTime() - today.getTime()) / oneDay;
                                                d_start=Math.round(diffDays/7);
                                                if(d_start<0)
                                                d_start=0;
                                                $('[name=deal_start]').val((dealstart.getMonth()+1) + '-' + dealstart.getDate() + '-' + dealstart.getFullYear());
                                    }

                                    if(hash[0] == 'deal_end' && hash[1] != '')
                                    {
                                                today=new Date();
                                                if(hash[1].indexOf('-') > 0)
                                                {
                                                            dates=hash[1].split('-');
                                                }

                                                else

                                                {
                                                            dates=hash[1].split('/');           
                                                }

                                                dealend=new Date(dates[2],dates[0]-1,dates[1]);
                                                diffDays = (dealend.getTime() - today.getTime()) / oneDay;
                                                d_end=Math.round(diffDays/7);
                                                if(d_end<0)
                                                d_end=20;
                                                $('[name=deal_end]').val((dealend.getMonth() +1) + '-' + dealend.getDate() + '-' + dealend.getFullYear());

                                    }

                if(hash[0] == 'rating_start' && hash[1] != '' && hash[1] != '0')
                                    {
                                                rat_start = hash[1];
                                                $('[name=rating_start]').val(hash[1]);
                                    }

            if(hash[0] == 'rating_end' && hash[1] != '' && hash[1] != '0')
                                    {
                                                rat_end = hash[1];
                                                $('[name=rating_end]').val(hash[1]);
                                    }

                                    if(hash[0] == 'locations' && hash[1] != '')
                                    {
                                                $('[name=filter_location]').val(hash[1])
                                    }
                                    if(hash[0] == 'keywords' && hash[1] != '')
                                    {
                                                $('[name=filter_keyword]').val(hash[1])
                                    }
                                    if(hash[0] == 'from' && hash[1] != '')
                                    {         
                                                if ($.inArray('-', hash[1]) > -1) 
                                                {
                                                            dates=hash[1].split('-')
                                                            $('[name=created_start]').val(dates[0] + '-' + dates[1] + '-' + dates[2])
                                                }
                                                else
                                                {
                                                            $('[name=created_start]').val(hash[1]);
                                                }
                                    }
                                    if(hash[0] == 'to' && hash[1] != '')
                                    {
                                                if ($.inArray('-', hash[1]) > -1) 
                                                {
                                                            dates=hash[1].split('-')
                                                            $('[name=created_end]').val(dates[0] + '-' + dates[1] + '-' + dates[2])
                                                }
                                                else
                                                {
                                                            $('[name=created_end]').val(hash[1]);
                                                }
                                    }
                        }
                        vars.push(hash[0]);
                        vars[hash[0]] = hash[1];
            }
            else
            {
                hashes = window.location.href.slice(window.location.href.indexOf('?') + 1);
                hash = hashes.split('=');
                if(hash[0] == 'q' && hash[1] != '')
                { 
                    $('#q').val(decodeURIComponent(hash[1])); 
                    try{
                        qValue = $('#q').val(); 
                        // qValue = qValue.replace(/-/g,' ');
                        while(qValue.indexOf('+') > -1)
                        {
                            qValue = qValue.replace('+',' ');                       
                        }
                    }catch(e){}                     
                    
                    $('#q').val(qValue);
                                            
                }

                if($('[name=budget_start]').val() != '' && $('[name=budget_start]').val() != '0')
                {
                     b_start = eval($('[name=budget_start]').val());
                }

                if($('[name=budget_end]').val() != ''  && $('[name=budget_end]').val() != '0')
                {
                    b_end = eval($('[name=budget_end]').val());
                }
                if($('[name=ranking_start]').val() != '' && $('[name=ranking_start]').val() != '0')
                {
                    r_start = $('[name=ranking_start]').val();
                }

        if($('[name=ranking_end]').val() != ''&& $('[name=ranking_end]').val() != '0')
                        {
                                    r_end = $('[name=ranking_end]').val();
                        }
        if($('[name=price_start]').val() != ''&& $('[name=price_start]').val() != '0')
                        {
                                    p_start = $('[name=price_start]').val();
                        }
        if($('[name=price_end]').val() != ''&& $('[name=price_end]').val() != '0')
                        {
                                    p_end = $('[name=price_end]').val();
                        }
        if($('[name=deal_start]').val() != '' && $('[name=deal_start]').val() != 'None')
                        {
                                    today=new Date();
                                    dealstart = ''
                                    if ($.inArray('-', $('[name=deal_start]').val()) > -1) 
                                    {
                                                dates=$('[name=deal_start]').val().split('-');
                                                dealstart=new Date(dates[0],dates[1]-1,dates[2]);
                                    }
                                    else
                                                dealstart = new Date($('[name=deal_start]').val());

                                    diffDays = (dealstart.getTime() - today.getTime()) / oneDay;
                                    d_start=Math.round(diffDays/7);
                                    if(d_start<0)
                                    d_start=0;

                                   

                                    $('[name=deal_start]').val((dealstart.getMonth()+1) + '-' + dealstart.getDate() + '-' + dealstart.getFullYear());

                        }

        if($('[name=deal_end]').val() != '' && $('[name=deal_end]').val() != 'None')

                        {
                                    today=new Date();
                                    dealend = ''
                                    if ($.inArray('-', $('[name=deal_end]').val()) > -1) 
                                    {

                                                dates=$('[name=deal_end]').val().split('-');

                                                dealend=new Date(dates[0],dates[1]-1,dates[2]);

                                    }
                                    else

                                                dealend = new Date($('[name=deal_end]').val());

                                    diffDays = (dealend.getTime() - today.getTime()) / oneDay;
                                    d_end=Math.round(diffDays/7);
                                    if(d_end<0)
                                    d_end=20;
                                    $('[name=deal_end]').val((dealend.getMonth() + 1) + '-' + dealend.getDate() + '-' + dealend.getFullYear());
                        }

        if($('[name=rating_start]').val() != ''&& $('[name=rating_start]').val() != '0')
                        {
                                    rat_start = $('[name=rating_start]').val();
                        }

        if($('[name=rating_end]').val() != ''&& $('[name=rating_end]').val() != '0')
                        {
                                    rat_end = $('[name=rating_end]').val();
                        }

            }

            var smonth = 2 //start-month, start-year
            $( ".rank" ).slider({     
                        range: true,
                        min: 0,
                        max: 5,
                        step:1, 
                        values:[r_start,r_end],
                        slide: function( event, ui ) {
                                    $( "#filter_rank" ).val( ui.values[ 0.0 ] + gettext(" to ") + (ui.values[ 1.0 ]));
                        },
                        change:function(event, ui){
                                    $('[name=ranking_start]').val(ui.values[ 0 ]);
                                    $('[name=ranking_end]').val(ui.values[ 1 ]);
                                    perform_search();
                        }
            });

            $( "#filter_rank" ).val( $( ".rank" ).slider( "values", 0.0 ) + gettext(" to ") + $( ".rank" ).slider( "values", 1.0 ) );

                        $( ".budget" ).slider({

                          range: true,

                          min: 0,

                          max: 1000000,

                          step: 50,

                          values: [ b_start, b_end ],

                          slide: function( event, ui ) {

                           $( "#filter_budget" ).val( ui.values[ 0 ] + gettext(" to ") + ui.values[ 1 ] + " SEK");

                          },

                          change:function(event, ui){

                           $('[name=budget_start]').val(ui.values[ 0 ]);

                           $('[name=budget_end]').val(ui.values[ 1 ]);

                           perform_search();

                          }

             });                  

 

            $( "#filter_budget" ).val( $( ".budget" ).slider( "values", 0 ) +
            gettext(" to ") + $( ".budget" ).slider( "values", 1 ) + " SEK" );         

            $( ".time" ).slider({

            range: true,

            min: 0,

            max: 20,

            step: 1,

            values: [ d_start, d_end ],

            slide: function( event, ui ) {

            $( "#filter_deal_time" ).val( ui.values[ 0 ] + gettext(" to ") + ui.values[ 1 ] + gettext(" weeks"));

            },

            change:function(event, ui){

            var day_start = parseInt(ui.values[ 0 ]) * 7;

            var day_end = parseInt(ui.values[ 1 ]) * 7;

           

            var date_start = new Date();

            var date_end = new Date();

           

            date_start.setDate(date_start.getDate()+day_start);

            date_end.setDate(date_end.getDate()+day_end);

           

                                    if(day_start > 0){

                                    $('[name=deal_start]').val((date_start.getMonth()+1) + '-' + date_start.getDate() + '-' + date_start.getFullYear());

                                    }else{

                                    $('[name=deal_start]').val('');

                                    }

                                    if(day_end > 0){

                                    $('[name=deal_end]').val((date_end.getMonth()+1) + '-' + date_end.getDate() + '-' + date_end.getFullYear());

                                    }else{
                                    $('[name=deal_end]').val('');
                                    }
                                    perform_search();

                        }

            });

            $( "#filter_deal_time" ).val( $( ".time" ).slider( "values", 0 ) +

            gettext(" to ") + $( ".time" ).slider( "values", 1 ) + gettext(" weeks") );

           

            $( ".price" ).slider({

            range: true,

            min: 0,

            max: 1000,

            step: 10,

            values: [ p_start, p_end ],

            slide: function( event, ui ) {

            $( "#filter_price_range" ).val( ui.values[ 0 ] + gettext(" to ") + ui.values[ 1 ] + " SEK");

            },

            change:function(event, ui){

            $('[name=price_start]').val(ui.values[ 0 ]);

            $('[name=price_end]').val(ui.values[ 1 ]);

            perform_search();

            }

            });

            $( "#filter_price_range" ).val( $( ".price" ).slider( "values", 0 ) +

            gettext(" to ") + $( ".price" ).slider( "values", 1 ) + " SEK" ); 

                                   

            $( ".rating_act" ).slider({

            range: true,

            min: 0,

            max: 5,

            values: [ rat_start, rat_end ],

            step: 1,

            slide: function( event, ui ) {

            $( "#filter_rating" ).val( ui.values[ 0.0 ] + gettext(" to ") + ui.values[ 1.0 ] );

            },

            change:function(event, ui){

            $('[name=rating_start]').val(ui.values[ 0 ]);

            $('[name=rating_end]').val(ui.values[ 1 ]);

            perform_search();

            }

            });

            $( "#filter_rating" ).val( $( ".rating" ).slider( "values", 0.0 ) +

            gettext(" to ") + $( ".rating" ).slider( "values", 1.0 ) ); 

           

            $( "#slider-range a:last, #slider-range1 a:last, #slider-range2 a:last, #slider-range3 a:last, #slider-range4 a:last").addClass("slider_right");

            $( "#from" ).datepicker({

                dateFormat: 'mm-dd-yy',                   
                defaultDate: "",
                changeMonth: true,
                changeYear: true,
                numberOfMonths: 1,

                onSelect: function( selectedDate ) {

                    $( "#to" ).datepicker( "option", "minDate", selectedDate );
                    perform_search();
                }
            });

            $( "#to" ).datepicker({

                dateFormat: 'mm-dd-yy',                   
                defaultDate: "",
                changeMonth: true,
                changeYear: true,
                numberOfMonths: 1,

                onSelect: function( selectedDate ) {

                    $( "#from" ).datepicker( "option", "maxDate", selectedDate );
                    perform_search();
                }
            });
            
            $( "#from_lead" ).datepicker({

                buttonImage: '/static/img/date_picker.png',
                defaultDate: "currentDate",
                buttonImageOnly: true,
                changeMonth: true,
                changeYear: true,
                numberOfMonths: 1,
                showOn: 'both',

                onSelect: function( selectedDate ) {
                    $( "#to_lead" ).datepicker( "option", "minDate", selectedDate );
                }
            });

            $( "#to_lead" ).datepicker({

                defaultDate: "",
                buttonImage: '/static/img/date_picker.png',
                buttonImageOnly: true,
                changeMonth: true,
                changeYear: true,
                numberOfMonths: 1,
                showOn: 'both',
                
                onSelect: function( selectedDate ) {
                    $( "#from_lead" ).datepicker( "option", "maxDate", selectedDate);
                }
            });

            $( "#auction_starts_at" ).datepicker({

                defaultDate: "",
                buttonImage: '/static/img/date_picker.png',
                buttonImageOnly: true,
                changeMonth: true,
                changeYear: true,
                numberOfMonths: 1,
                showOn: 'both',
                
                // onSelect: function( selectedDate ) {
                //     $( "#from_lead" ).datepicker( "option", "maxDate", selectedDate);
                // }
            });
                        $('.search').change(function() {
                            perform_search();
                        });
                   
                        $( "#date_bith" ).datepicker({

                                    defaultDate: "",

                                    buttonImageOnly: false,

                                    changeMonth: true,

                                    changeYear: true,

                                    yearRange:"-90:+0",

                                    numberOfMonths: 1,

                                    format: 'y m, D'

                        });

                        attach_pagination_events();
                        load_matching_lead()
                        load_lead_searchcount()
                       
            });       

function filter_show(){

    var url = window.location.href;
    if (url.indexOf('/dashboard/filters/#/newfilter') >= 0) {
        $('.my_filters, .tabs, .pagination').hide();
        $('.funct_menu').hide();
    
    } else {

        $('.my_filters, .tabs, .pagination').show();
    }

}

function left_dyanmic_height() {

            var profile_sidebar = $('.right_content_holder, .v2_dashboard_wrapper, .right_content_wrapper, .dashboard_content_wrapper, .filter_result_wrapper').height();

            profile_sidebar_height = profile_sidebar + 180;
            profile_sidebar_height_2 = profile_sidebar;
            
            $('.profile_sidebar').height(profile_sidebar_height);
            
            var shouldShow = $.cookie('show_desc') == 'yep';
                if( shouldShow ) {
                    if(profile_sidebar_height_2 > 700){
                        $('.filter_wrapper').height(profile_sidebar_height_2 + 120);
                    }
                    else{
                        $('.filter_wrapper').height(profile_sidebar_height_2 + 830);
                    } 
                     
                }
                else {
                    $('.filter_wrapper').height(profile_sidebar_height_2 + 120); 
                }
            
           

}

function addasfavorite(){
            $('.add_favorite_act').click(function() {
        $('.stars').show();
        $(this).hide();
        $('.remove_favorite_act').show();
            });

            $('.remove_favorite_act').click (function (){
                        $('.stars').hide();
                        $(this).hide();
                        $('.add_favorite_act').show();
            });
 }

function position_popup () {
                        var pop_pos = $(window).scrollTop() + 90;
                        $('.popup_pos').css('top', pop_pos);
}

 

function signin_position_popup() {
                        var pop_pos = $(window).pageYOffset
                        $('.popup_pos').css('top', pop_pos);
}                                 

 

function terms_position_popup() {
                        var pop_pos = $(window).scrollTop() + 300;
                        $('.terms_popup_pos').css('top', pop_pos);
            }                     

jQuery.fn.terms_position_center = function () {
    var pop_pos = $(window).scrollTop() + 50;
     $('.terms_popup_pos').css('top', pop_pos);
  }

/****************** joinus validation *********************/

function joinus_validation(){

                        /********joinus popup skip step************/

                        $('.joinus_popup_step1 .skip_step_act').click (function () {
                                    $('.joinus_popup_step2').show();
                                    $('.joinus_popup_step1').hide();
                                    $("#personal_address .select p").text("select");
                                    $('#copyaddress').attr('checked', false);
                                    $('.current').removeClass('current').hide()
                   .next().show().addClass('current');

               if ($('.current').hasClass('last')) {
                   $('.joinus_next').hide();
               }

               $('.joinus_prev').show();      
                        });

                       

                        $('.joinus_popup_step2 .skip_step_act').click (function () {
                                    $('.joinus_popup_step3').show();
                                    $('.joinus_popup_step2').hide();
                                    $("#company_address .select p").text("select");
                                    $('#copyaddress').attr('checked', false);
                                    $('.current').removeClass('current').hide()

                   .next().show().addClass('current');

                           if ($('.current').hasClass('last')) {
                               $('.joinus_next').hide();
                           }

                           $('.joinus_prev').show();
                        });

                        $('.joinus_popup_step3 .skip_step_act').click (function () {
                                    $('.popup_fade:first').show();
                                    $('.joinus_popup').hide();
                                    $('#copyaddress').attr('checked', false);

                        });

            /********* joinus popup next step ************/ 
                        $('.joinus_close_act').click (function (){
                                                $('.joinus_popup').hide();
                                                $('.first').addClass('current');
                                                $('.joinus_popup input[type="text"], .joinus_popup input[type="checkbox"], .joinus_popup textarea').val('');
                                                $('#div2').removeClass('current');
                                                $('#div3').removeClass('current');
                                                $('#div1').addClass('current');
                                                $('#copyaddress').attr('checked', false);

             });

                        $('.joinus_next').click(function() {
               if (cfFv.validate()){
               $('#div1 .validation_required').hide();        
               $('.current').removeClass('current').hide()
                   .next().show().addClass('current');
               if ($('.current').hasClass('last')) {
                   $('.joinus_next').hide();
                   $('.step3').hide();
               }

               $('.joinus_prev').show();
              }

               else{
                        $('#div1 .validation_required').show();
              }

              

            });

           

            $('.step3').click(function() {
               if (frFV.validate()){
                        $('#div2 .validation_required').hide();
               $('.current').removeClass('current').hide()
                   .next().show().addClass('current');
               if ($('.current').hasClass('last')) {
                   $('.joinus_next').hide();
                   $('.step3').hide();
               }
               $('.joinus_prev').show();
              }

              else{
                        $('#div2 .validation_required').show();
              }

              

            });

           

            $('.joinus_prev').click(function() {
                                    $('#div1 .validation_required').hide();
                                    $('#div2 .validation_required').hide();

               $('.current').removeClass('current').hide()

                   .prev().show().addClass('current');

               if ($('.current').hasClass('first')) {

                   $('.joinus_prev').hide();

               }

               $('.joinus_next').show();

                $('.step3').show();

            });
           

                        // Let's get a new form validator

                                    // Arguments: (boolean isSilent, text field error class, label error class, select error class, error display element class)

                                    var reFV = new FieldValidator(false, "inputError", "labelError", "selectError");

                                    // Add all the required fields
                                    // Arguments (ID, Type[select, checkbox, usPhone, email, zip, date, radio], Guide Text, Required?)

                                    reFV.add("fname", "", "",       true);
                                    reFV.add("lname","", "", true);
                                    reFV.add("email","email", "", true);
                                    reFV.add("pass","", "", true);

                                    // Setup the validation on submits

                                    jQuery('.signup_act').click (function (){
                                                if ($('.signup_btn').attr('data-emailexist') == 'true')
                                                {
                                                            $('.form_inputfileds').addClass("inputError");
                                                            $('.banner_signup_form label.validation_required').show();
                                                }
                                                else if (reFV.validate() && validatePwd()){
                                                            $('.popup_fade:first').show();
                                                           $('.first').show();
                                                           $('.joinus_popup').show();
                                                           $('#div2').hide();
                                                           $('#div3').hide();
                                                            $('.joinus_next').show();
                                                            $('.max_pwd_error').hide();
                                                            position_popup ();      
                                                            $('.banner_signup_form label.validation_required').hide();
                                                }
                                    });
                                    // Let's get a new form validator
                                    // Arguments: (boolean isSilent, text field error class, label error class, select error class, error display element class)
                                    var cfFv = new FieldValidator(false, "inputError", "labelError", "selectError");
                                    // Add all the required fields
                                    // Arguments (ID, Type[select, checkbox, usPhone, email, zip, date, radio], Guide Text, Required?)
                                    cfFv.add("street", "", "",         true);
                                    //myFV.add("company","", "Company", true);
                                    cfFv.add("postal_code","", "" , true);
                                    cfFv.add("city","", "" , true);
                                    cfFv.add("country","select", "" , true);
                                    cfFv.add("phone_number","", "" , true);
                                    // Let's get a new form validator
                                    // Arguments: (boolean isSilent, text field error class, label error class, select error class, error display element class)
                                    var frFV = new FieldValidator(false, "inputError", "labelError", "selectError");
                                    // Add all the required fields
                                    // Arguments (ID, Type[select, checkbox, usPhone, email, zip, date, radio], Guide Text, Required?)
                                    frFV.add("company_name", "", "Your name",           true);
                                    frFV.add("company_street","", "", true);
                                    frFV.add("company_postal_code","", "Case details..." , true);
                                    frFV.add("company_city","", "" , true);
                                    frFV.add("company_country","select", "" , true);
                                    frFV.add("phone_number","", "" , true);                               

}

 

function leadvalidation() {    
                               
    //required = ["leadtitle", "leadcategory", "leadkeywords", "from_lead", "to_lead",  "leadprice", "leadavailable", "leadbudget", "leaddescription", "consumeremail", "consumerphonenumber"];

    requestedlead_required = [ "i_want_title", "i_want_description", "i_want_leadcategory", 
                                "i_want_region", "i_want_country", "i_want_pricefrom", 
                                "i_want_first_name", "i_want_email", "i_want_password", 
                                "i_want_priceto", "i_want_leadsneeded", "i_want_last_name" ];

    $('#i_want_leadcategory, #i_want_leadkeyword')
        .live('focus', function() { if (this.value == "Comma separated keywords like ,") { this.value = '' }})
        .live('blur', function() { if (!this.value.trim().length) { this.value = "" }});

    // modified by karthikesh on 13/11/2013, for handling 'change' event when errors exist at js part
    $("#requestedlead").live('submit', function(event) {

        //Validate required fields
        for ( i = 0; i < requestedlead_required.length; i++) {

            var input = jQuery('#' + requestedlead_required[i]);

            if ((input.val() == "")) {
                event.preventDefault();
                input.addClass("inputError");
            } else {
                input.removeClass("inputError");
            }
        }

        //Code by Karthikesh to validate email
        var email_val = $('#i_want_email').val()
        if (IsEmail(email_val)) {
            $('#i_want_email').removeClass("inputError");
        } else {
            $('#i_want_email').addClass("inputError");
        }

        if ($('#i_want_leadkeyword').val() == "Comma separated keywords like ," ||
                $('#i_want_leadkeyword').val().trim() == '') {

            $('#i_want_leadkeyword').addClass("inputError");
        } else {
            $('#i_want_leadkeyword').removeClass("inputError");
        }

        if ($('#i_want_leadcategory').val() == "Select") {

            $('.leadcategory').addClass("inputError");
        } else {
            $('.leadcategory').removeClass("inputError");
        }

        if ($('#i_want_country').val() == "") {

            $('.leadcountry').addClass("inputError");
        } else {
            $('.leadcountry').removeClass("inputError");
        }

        if ($('#i_want_leadsneeded_unit').val() == "Select") {

            $('.lead_unit').addClass("inputError");
        } else {
            $('.lead_unit').removeClass("inputError");
        }

        //if any inputs on the page have the class 'inputError' the form will not submit
        if ($("#requestedlead:input, #requestedlead .select").hasClass("inputError")) {
            return false;
        } else {
            return true;
        }
    }); 

}

function msie_placeholder() {
    $('[placeholder]').focus(function() {
        var input = $(this);
        if (input.val() == input.attr('placeholder')) {
           input.val('');
           input.removeClass('placeholder');
        }

    }).blur(function() {
         var input = $(this);
         if (input.val() == '' || input.val() == input.attr('placeholder')) {
           input.addClass('placeholder');
           input.val(input.attr('placeholder'));
         }

    }).blur().parents('form').submit(function() {
         $(this).find('[placeholder]').each(function() {
           var input = $(this);
           if (input.val() == input.attr('placeholder')) {
             input.val('');
           }

         })
    });
}

function getBudget(val)
{
var s = '0'

            switch(val) {

                  case 0:

                    s = '0';

                    break;

                  case 100:

                    s = '62500';

                    break;  

                  case 200:

                    s = '125000';

                    break;

                  case 400:

                    s = '187500';

                    break;

                  case 800:

                    s = '250000';

                    break;

                  case 1600:

                    s = '312500';

                    break;

                  case 2400:

                    s = '375000';

                    break;

                  case 2800:

                    s = '437500';

                    break;

                  case 5600:

                    s = '500000';

                    break;    

                  case 12000:

                    s = '562500';

                    break;

                  case 24000:

                    s = '625000';

                    break;

                  case 48000:

                    s = '687500';

                    break;

                  case 96000:

                    s = '750000';

                    break;

                  case 192000:

                    s = '812500';

                    break;

                  case 384000:

                    s = '875000';

                    break;

                  case 768000:

                    s = '937500';

                    break;              

                  case 1000000:

                    s = '1000000';

                    break;     

               }

            return s;

}
function geolocation ()
{
    ipaddress =$('[name=givenip]').val();
    $.get('/testpage/?ipaddress='+ ipaddress, function(data){
        $('#inputblock').html(data);
    });

}
function validateDeposit () {
    validate = validatefields() 
    if (validate == true)
    {
        
        $('.paypal_btn').addClass('gry_out').attr('disabled', 'disabled') 
        $('[name=depositvalue]').val('apply_invoice')   
        var d = $('#validatedeposit').serialize();
        d=decodeURIComponent(d);
       
        $.get('depositcredit/?'+ d, function(data){
            $('#invoice_sucess').show();    
            $('#payment_block').hide();
            $('#main').hide();
            var url = window.location.href;
            //window.location.href = url +'?appliedforinvoice=1#invoice';
            var new_url = url +'?appliedforinvoice=1#invoice';
            history.pushState(null, null, new_url);
        
        });
    }
    
}
var spamError = {
    'background':'#ffdddd','border':'1px solid ','border-color':'#DD4B39'
};

var inputbox = {
    'background':'white','border-color':'#b8b8b8'
};
function validatefields()
{

    var errstr = ''
    
    if ($.trim($('[name=company_name]').val()) == '') { 
        $('[name=company_name]').css(spamError);
        errstr += 'company_name,'   
            }
    else{
        $('[name=company_name]').css(inputbox);
        
    }
    
    if ($.trim($('[name=company_address]').val()) == '') {  
        $('[name=company_address]').css(spamError);     
        errstr += 'company_address,'
            }
    
    else{
        $('[name=company_address]').css(inputbox);
         
    }
    if ($.trim($('[name=postal_code]').val()) == '') {  
        $('[name=postal_code]').css(spamError);     
        errstr += 'postal_code,'
            }
    else{
        $('[name=postal_code]').css(inputbox);
         
    }
    if ($.trim($('[name=city]').val()) == '') { 
        $('[name=city]').css(spamError);
        errstr += 'city,'       
            }
    else{
        $('[name=city]').css(inputbox);
         
    }
    
    if ($.trim($('[name=company_country]').val()) == '' || $('[name=company_country]').val() == 'Select')
    {   
        $('[name=company_country]').css(spamError);
        errstr += 'company_country,'            
            }
    else{
        $('[name=company_country]').css(inputbox);
         
    }
    
    if ($.trim($('[name=company_phone]').val()) == '') {    
        $('[name=company_phone]').css(spamError);
        errstr += 'company_phone,'
            }
    else{
        $('[name=company_phone]').css(inputbox);
         
    }
    
    if ($.trim($('[name=corporate_identity_number]').val()) == '') {    
        $('[name=corporate_identity_number]').css(spamError);
        errstr += 'corporate_identity_number'           
            }
    else{
        $('[name=corporate_identity_number]').css(inputbox);
         
    }
    
    if (errstr != '' ){
        return false
    }
    else
    {
        return true
    }
}

function validateSearch() {
   left_dyanmic_height();
   // code by Karthikesh on 30/10/2013, for search ajax issue
   var is_search_page = window.location.href.indexOf('/search')
   if(is_search_page > 1)
   {
        $('[name=q]').val($('#q').val());
        perform_search();
   }
   else
   {
        if($('#q').val() == ''){

             $('#q').val('');
        }   
        $("#f_search").submit();
   }
}

$('.search_btn').live('click', function() {
        validateSearch();
    });

function setSelectedLead(leadid)
{
            $('input[name="selected_lead"]').val(leadid)
            $('input[name="selected_lead2"]').val(leadid)
            $('#selected_leadbuy, #selected_autobuy').val(leadid)
            
            // Coded by Karthikesh on 23/10/2013, for auto buy issue
            var query_string = ''
            var query = $('#q').val();
            if(query.trim() != '') 
                query_string = '?q=' + query
            var next = '/leads/' + leadid + '/' + query_string 
            $('#request_path_lead').val(next);
            $('#redirect_path_lead').val(next);
            $('#register_path_lead').val(next);
}

function addSearch()
{
    perform_search();
}

function keywordSearchDelete()
{
    $('#keyword_highlight').hide();
    $('#filterkeyword').val('');
    perform_search();
    
}
$('#delete_location').click(function() {
        $.removecookie("locations");
        locationSearchDelete();

});
function locationSearchDelete()
{
    $('#location_highlight').hide();
    $('#filterlocation').val('');
    perform_search();
}

function pagination_filter_align(){
            logedin_footer_width = $('.step-links').width();
            $('#pagination_filter').width(logedin_footer_width+20+"px"); 
}

function paginate_alter_text(){
}

function btn_align() {
    
    btn_width = $('.empty_list_btn').width();
    alig_btn_width = btn_width/2;
    $('.empty_list_btn').css( "margin-left", +-+alig_btn_width );
}
 

function email_campaign(){

            $("#email_campaign_popup_swap td div").live('click', function(){

                        $('.popup_fade:first, .lead_details_popup').show();

                        $('.lead_details_popup_content').hide();

                        $("#"+$(this).attr("class")).show();
                        
            });       

}

function load_matching_lead(){
    
    var url = window.location.href;
    
    if (url.indexOf('/dashboard/edit_filter') >= 0) {
        
        var qranking_start  = $('[name=ranking_start]').val() == 0?'':$('[name=ranking_start]').val();
        var qranking_end    = $('[name=ranking_end]').val() == 0?'':$('[name=ranking_end]').val();
        var qbudget_start   = $('[name=budget_start]').val() == 0?'':$('[name=budget_start]').val(); 
        var qbudget_end     = $('[name=budget_end]').val() == 0?'':$('[name=budget_end]').val();        
        var qdeal_start     = $('[name=deal_start]').val();
        var qdeal_end       = $('[name=deal_end]').val();
        var qprice_start    = $('[name=price_start]').val() == 0?'':$('[name=price_start]').val();
        var qprice_end      = $('[name=price_end]').val() == 0?'':$('[name=price_end]').val();
        var qrating_start   = $('[name=rating_start]').val() == 0?'':$('[name=rating_start]').val();
        var qrating_end     = $('[name=rating_end]').val() == 0?'':$('[name=rating_end]').val();
        
        
        var q ='q='+$('[name=filtersearch]').val() + '&page=1&ranking_start='+qranking_start
                    +'&ranking_end='+qranking_end+'&budget_start='+qbudget_start+'&budget_end='+qbudget_end+'&deal_start='+qdeal_start+'&deal_end='+qdeal_end
                     +'&price_start='+qprice_start+'&price_end='+qprice_end+'&rating_start='+qrating_start
                     + '&rating_end='+qrating_end+'&created_start='+$('[name=created_start]').val() 
                     +'&created_end='+$('[name=created_end]').val() +'&locations='+$('[name=filter_location]').val()
                     +'&keywords='+$('[name=filter_keyword]').val()+'&lang='+$("#currentlanguage").val();
                    
        q = q.replace(/-/g,'/');
        $.get('/search/?'+ q, function(data){

            show_searching(false);
            $('#search_result').html(data);
            $('[name=search_founded_no]').val($('.founded_no').text().trim());
            attach_pagination_events();

        });
    }
}

function load_lead_searchcount()
{
    var url = window.location.href; 
    if (url.indexOf('/dashboard/filters') >= 0) {       

    $(".filtercount").each(function(index){
        
        count = index +1;       
        x = 'txtsearchparams'+count;
        q = $(eval(x)).val();
        
        $.ajax({
            
            url: '/search/?'+ q,
            type: 'get',
            dataType: 'html',
            async: false,
            success: function(data) {
            result = data;
            }
         
        });
    
        show_searching(false);
        $('#search_result').html(result);
        matchingText = q.split("dest=")     
        matchingCount = $('.founded_no').text().trim();
        matchingCount = matchingCount.split(" ");
        $(eval(matchingText[1])).val(matchingCount[0]==0?'0':matchingCount[0]);
        attach_pagination_events();
     
        
        }); 
     
    }
    
}

$(document).ready(function() {

    $('#showHiddenBlock').click(function() {

        $('#form_search_filter').show();

    });
    
        
    if($('[name=keywords]').val() == '')
        $('#keyword_highlight').hide();
        
    else
    {
        var url = window.location.href;             
        if (url.indexOf('/search') >= 0)
        {           
            
            if($('input[name=keywords]').val() == '')
            {
                $('#keyword_highlight').hide(); 
            }
            else
            {
                $('#keyword_highlight').show();
            }           
            
        }
        else
        {   
             $('#keyword_highlight').show();
         }      
        
    }
        
        
        
    if($('[name=locations]').val() == '')
        $('#location_highlight').hide();
    
    else
    {
        var url = window.location.href;             
        if (url.indexOf('/search') >= 0)
        {           
            $('#location_highlight').hide();
        }
        else
        {   
             $('#location_highlight').show();
         }      
        
    }
        

});

function searchOpen() {
    var search = $('#txtSearch').val()
    var data = {
        search: search
    };
    $.ajax({
        url: '/search.json',
        data: data,
        dataType: 'jsonp',
        jsonp: 'callback',
        jsonpCallback: 'searchResult'
    });
}


function searchResult(data) {
    $( "#txtSearch" ).autocomplete ({
        source: data
    });
}

function help_box_expansion(){
    var wi = $(window).width();
    var wht = $(window).height();
    var dht = $(document).height();
    var help_text = $('.help_texts').is(':visible');
    

    if (wi > 1366) {
        
        $('.recently_viewed_expand, .help_box_expand').show();
        $('.help_box_collapsed, .recently_viewed_colapsed').hide(); 
        $('.buy_now_slide').show();
        $(window).scroll(function (event) {
        // what the y position of the scroll is
        $('.buy_now_slide').show();
        
        
      });
    }
    else
    {
        
        $('.recently_viewed_expand, .help_box_expand').hide();
        $('.help_box_collapsed, .recently_viewed_colapsed').show(); 
        $('.buy_now_slide').hide();
        $(window).live('scroll', function (event) {
            // what the y position of the scroll is
            $('.buy_now_slide').hide();
            
          });
        
        var show_leftmenu = $.cookie('show_leftmenu');
        if (show_leftmenu == "OPENED") {
            $('.recently_viewed_expand').show();
            $('.recently_viewed_colapsed').hide();
        }
        else if (show_leftmenu == "CLOSED") {
            $('.recently_viewed_expand').hide();
            $('.recently_viewed_colapsed').show();
        }
        
    }
    
    if (wi < 1050) {        
        $('.help_box_collapsed').hide();
        $('.recently_viewed_colapsed').hide();

    }
    if(help_text){
        $('.help_box_collapsed').hide();
        $('.recently_viewed_colapsed').hide();
    }
    if (wi < 960) {
        
        // $('#help_box').hide();
        // $('#recently_viewed').hide();
        $('.back2top').hide();
        $(window).live('scroll', function (event) {
            // what the y position of the scroll is
            $('.back2top').hide();
            $('.buy_now_slide').hide();
            
          });
    }
    else
    {
        
        // $('#help_box').show();
        // $('#recently_viewed').show();
        $(window).live('scroll', function (event) {
            // what the y position of the scroll is
            $('.back2top').show();
            $('.buy_now_slide').show();
            
          });
    }
    
    if(dht >= wht && $('.back2top').is(':visible')){
            $('.back2top').hide();
        }
}

function help_box_expansion_2(){
    var top = $('#recently_viewed').offset().top - parseFloat($('#recently_viewed').css('marginTop').replace(/auto/, 0)) ;
    var wii = $(window).width();
    var whti = $(window).height();
    var dhti = $(document).height();
    var buy_height = 900
    $(".banner_home").siblings(".footer").hide();
    $(window).scroll(function(event) {
        // what the y position of the scroll is
        var y = $(this).scrollTop() ;
        // whether that's below the form
        if (y >= top) {
            // if so, ad the fixed class
            $('#recently_viewed').addClass('fixed');
            
            if (wii < 960){
                $('.back2top').hide();  
            }
            else{
                $('.back2top').show();
            }
             $(".banner_home").siblings(".footer").show();

        } else {
            // otherwise remove it
            $('#recently_viewed').removeClass('fixed');
            $('.back2top').hide();
            $(".banner_home").siblings(".footer").hide();
            
        }
        if(y == scroll_top){
            $('.footer').show();
        }
        
        if (y >= buy_height) {
            $('.buy_now_slide').show();
        }
        else{
            $('.buy_now_slide').hide();
        }
        
    });
}
jQuery.fn.center = function () {
    this.css("top", ( jQuery(window).height() - this.height() ) / 2+jQuery(window).scrollTop()-25 + "px");
    return this;
  }
  
//Code to validate email 
function IsEmail(email)
{
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,9})+$/;
    return regex.test(email);
}

$('.lead_buy_btn, .direct_buy_signin_alert').live('click', function(){

    $('.signin_alert1').removeClass('basket_lead').addClass('buynow_lead')
})

$('.add_to_basket').live('click', function(){

    $('.signin_alert1').addClass('basket_lead').removeClass('buynow_lead')
})

$('.close_btn').live('click', function(){ $('.error_msg').html('') })

$('#form_id').live('submit', function(){
     $('.buy_now').addClass('gry_out')
        .attr('disabled', 'disabled')
     $(this).submit()
})
