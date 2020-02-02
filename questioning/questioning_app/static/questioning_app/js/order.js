$(document).ready(function() {
  $("#id_user").val(userId);
  $("#id_products").val(getOrderProductIdsFromCookie());

  $('#cancel-order-button').on("click", function() {
  	document.cookie = `order-products=; path=/`;
  });
});
