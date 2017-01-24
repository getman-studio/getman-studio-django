$(document).ready(function() {
  cart = []
  if (localStorage["cart"]) {
    cart = JSON.parse(localStorage["cart"]);
  }
  validateCart();
});

function addItem(id, name, price, quantity = 1) {
  var item = findItem(id);
  if (!item) {
    item = {"id": id, "name": name, "price": price, "quantity": quantity};
    cart.push(item);
  } else {
    item.quantity += quantity;
  }

  localStorage["cart"] = JSON.stringify(cart);
  validateCart();
  return false;
}

function removeItem(id, quantity = 1) {
  var item = find(id);
  if (item) {
    item.quantity -= 1;

    if (item.quantity < 0) {
      var index = cart.indexOf(item);
      delete cart[index]
    }
  }

  localStorage["cart"] = JSON.stringify(cart);
  validateCart();
  return false;
}

function removeAllItems(id) {
  var item = find(id);
  var index = cart.indexOf(item);
  delete cart[index]

  localStorage["cart"] = JSON.stringify(cart);
  validateCart();
  return false;
}

function clearCart() {
  delete localStorage["cart"];
  validateCart();
  return false;
}

function validateCart() {
  var $cart = $(".cart");
  var cartEmpty = cart.length == 0;
  if (cartEmpty) {
    $cart.removeClass("icon-green");
  } else {
    $cart.addClass("icon-green");
  }
}

function findItem(id) {
  for (var i = 0; i < cart.length; ++i) {
    if (cart[i].id == id) {
      return cart[i];
    }
  }
  return undefined;
}
