function getOrderProductIdsFromCookie() {
  if (document.cookie.indexOf('order-products=') == -1) return [];
  let value = document.cookie.split('order-products=')[1].split(';')[0];
  if (value.length == 0) return [];
  return value.split(',');
}


function setInitialButtonsState() {
  for (let id of getOrderProductIdsFromCookie()) {
    $(`button[data-product-id="${id}"]`).addClass('product-button-selected');
  }
  $('.product-button').removeClass('product-button-hidden');
}


function setOrderProductsCookie() {
  let productsIds = [];
  for (let button of $('.product-button.product-button-selected')) {
    productsIds.push($(button).attr('data-product-id'));
  }
  document.cookie = `order-products=${productsIds.join()}`;
}


$(document).ready(function() {
  setInitialButtonsState();

  $('.product-button').on('click', function(e) {
    $(this).toggleClass('product-button-selected');
    setOrderProductsCookie();
  });
});
