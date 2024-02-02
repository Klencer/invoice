$(document).ready(function () {

    // alert("We are all set!");

    $('#div_id_product_six, #div_id_quantity_of_product_six, #div_id_unit_price_of_product_six, #div_id_total_price_of_product_six, #div_id_product_seven, #div_id_quantity_of_product_seven, #div_id_unit_price_of_product_seven, #div_id_total_price_of_product_seven, #div_id_product_eight, #div_id_quantity_of_product_eight, #div_id_unit_price_of_product_eight, #div_id_total_price_of_product_eight, #div_id_product_nine, #div_id_quantity_of_product_nine, #div_id_unit_price_of_product_nine, #div_id_total_price_of_product_nine, #div_id_product_ten, #div_id_quantity_of_product_ten, #div_id_unit_price_of_product_ten, #div_id_total_price_of_product_ten').hide()

    $('#more-line').click(function () {

        $('#div_id_product_five, #div_id_quantity_of_product_five, #div_id_unit_price_of_product_five, #div_id_total_price_of_product_five').slideToggle(200)
        $('#div_id_product_six, #div_id_quantity_of_product_six, #div_id_unit_price_of_product_six, #div_id_total_price_of_product_six').slideToggle(200)
        $('#div_id_product_seven, #div_id_quantity_of_product_seven, #div_id_unit_price_of_product_seven, #div_id_total_price_of_product_seven').slideToggle(200)
        $('#div_id_product_eight, #div_id_quantity_of_product_eight, #div_id_unit_price_of_product_eight, #div_id_total_price_of_product_eight').slideToggle(200)
        $('#div_id_product_nine, #div_id_quantity_of_product_nine, #div_id_unit_price_of_product_nine, #div_id_total_price_of_product_nine').slideToggle(200)
        $('#div_id_product_ten, #div_id_quantity_of_product_ten, #div_id_unit_price_of_product_ten, #div_id_total_price_of_product_ten').slideToggle(200)
    });


    $('#id_quantity_of_product_one, #id_unit_price_of_product_one, #id_quantity_of_product_two, #id_unit_price_of_product_two, #id_quantity_of_product_three, #id_unit_price_of_product_three, #id_quantity_of_product_four, #id_unit_price_of_product_four, #id_quantity_of_product_five, #id_unit_price_of_product_five, #id_quantity_of_product_six, #id_unit_price_of_product_six, #id_quantity_of_product_seven, #id_unit_price_of_product_seven, #id_quantity_of_product_eight, #id_unit_price_of_product_eight, #id_quantity_of_product_nine, #id_unit_price_of_product_nine, #id_quantity_of_product_ten, #id_unit_price_of_product_ten').keyup(function () {
        let quantity_of_product_one_text = $('#id_quantity_of_product_one').val();
        let unit_price_of_product_one_text = $('#id_unit_price_of_product_one').val();
        let total_price_of_product_one = quantity_of_product_one_text * unit_price_of_product_one_text;

        let quantity_of_product_two_text = $('#id_quantity_of_product_two').val();
        let unit_price_of_product_two_text = $('#id_unit_price_of_product_two').val();
        let total_price_of_product_two = quantity_of_product_two_text * unit_price_of_product_two_text;

        let quantity_of_product_three_text = $('#id_quantity_of_product_three').val();
        let unit_price_of_product_three_text = $('#id_unit_price_of_product_three').val();
        let total_price_of_product_three = quantity_of_product_three_text * unit_price_of_product_three_text;

        let quantity_of_product_four_text = $('#id_quantity_of_product_four').val();
        let unit_price_of_product_four_text = $('#id_unit_price_of_product_four').val();
        let total_price_of_product_four = quantity_of_product_four_text * unit_price_of_product_four_text;

        let quantity_of_product_five_text = $('#id_quantity_of_product_five').val();
        let unit_price_of_product_five_text = $('#id_unit_price_of_product_five').val();
        let total_price_of_product_five = quantity_of_product_five_text * unit_price_of_product_five_text;

        let quantity_of_product_six_text = $('#id_quantity_of_product_six').val();
        let unit_price_of_product_six_text = $('#id_unit_price_of_product_six').val();
        let total_price_of_product_six = quantity_of_product_six_text * unit_price_of_product_six_text;

        let quantity_of_product_seven_text = $('#id_quantity_of_product_seven').val();
        let unit_price_of_product_seven_text = $('#id_unit_price_of_product_seven').val();
        let total_price_of_product_seven = quantity_of_product_seven_text * unit_price_of_product_seven_text;

        let quantity_of_product_eight_text = $('#id_quantity_of_product_eight').val();
        let unit_price_of_product_eight_text = $('#id_unit_price_of_product_eight').val();
        let total_price_of_product_eight = quantity_of_product_eight_text * unit_price_of_product_eight_text;

        let quantity_of_product_nine_text = $('#id_quantity_of_product_nine').val();
        let unit_price_of_product_nine_text = $('#id_unit_price_of_product_nine').val();
        let total_price_of_product_nine = quantity_of_product_nine_text * unit_price_of_product_nine_text;

        let quantity_of_product_ten_text = $('#id_quantity_of_product_ten').val();
        let unit_price_of_product_ten_text = $('#id_unit_price_of_product_ten').val();
        let total_price_of_product_ten = quantity_of_product_ten_text * unit_price_of_product_ten_text;

        const total = total_price_of_product_one + total_price_of_product_two + total_price_of_product_three +
            total_price_of_product_four + total_price_of_product_five + total_price_of_product_six +
            total_price_of_product_seven + total_price_of_product_eight + total_price_of_product_nine +
            total_price_of_product_ten

        $('#id_total_price_of_product_one').val(total_price_of_product_one);
        $('#id_total_price_of_product_two').val(total_price_of_product_two);
        $('#id_total_price_of_product_three').val(total_price_of_product_three);
        $('#id_total_price_of_product_four').val(total_price_of_product_four);
        $('#id_total_price_of_product_five').val(total_price_of_product_five);
        $('#id_total_price_of_product_six').val(total_price_of_product_six);
        $('#id_total_price_of_product_seven').val(total_price_of_product_seven);
        $('#id_total_price_of_product_eight').val(total_price_of_product_eight);
        $('#id_total_price_of_product_nine').val(total_price_of_product_nine);
        $('#id_total_price_of_product_ten').val(total_price_of_product_ten);
        $('#id_total').val(total);
    });

    $('.table').paging({limit:15});

         $(window).scroll(function() {
             if ($(this).scrollTop() > 50) {
                 $('.scrollToTop').fadeIn();
             }else {
                 $('.scrollToTop').fadeOut();
             }
         });

    $('.scrollToTop').click(function (){
      $('html, body').animate({scrollTop : 0},500);
      return false;
    });


});