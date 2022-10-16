$(document).ready(function () {
  $(".increment-btn").click(function (e) {
    e.preventDefault();

    var inc_value = $(this).closest(".product_data").find(".qty-input").val();
    var value = parseInt(inc_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value < 10) {
      value++;
      $(this).closest(".product_data").find(".qty-input").val(value);
    }
  });

  $(".addToCartBtn").click(function (e) {
    e.preventDefault();

    var servicemen_id = $(this).closest(".liclass").find(".servicemanid").val();

    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      method: "POST",
      url: "/add-to-cart",
      data: {
        servicemen_id: servicemen_id,

        csrfmiddlewaretoken: token,
      },

      success: function (response) {
        console.log(response);
        alertify.success(response.status);
      },
    });
  });
});
