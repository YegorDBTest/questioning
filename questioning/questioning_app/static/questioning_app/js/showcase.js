function setInitialButtonsState() {
  for (let id of getOrderProductIdsFromCookie()) {
    $(`button[data-product-id="${id}"]`).addClass('product-button-selected');
  }
  $('.product-button').removeClass('product-button-hidden');
}


function refreshMoveToOrderButton() {
  $('#move-to-order-button').attr('disabled', getOrderProductIdsFromCookie().length == 0);
}


function setOrderProductsCookie() {
  let productsIds = [];
  for (let button of $('.product-button.product-button-selected')) {
    productsIds.push($(button).attr('data-product-id'));
  }
  document.cookie = `order-products=${productsIds.join()}; path=/`;
  refreshMoveToOrderButton();
}


$(document).ready(function() {
  setInitialButtonsState();
  refreshMoveToOrderButton();

  $('.product-button').on('click', function(e) {
    $(this).toggleClass('product-button-selected');
    setOrderProductsCookie();
  });
});
