function getOrderProductIdsFromCookie() {
  if (document.cookie.indexOf('order-products=') == -1) return [];
  let value = document.cookie.split('order-products=')[1].split(';')[0];
  if (value.length == 0) return [];
  return value.split(',');
}
