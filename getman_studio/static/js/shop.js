$(document).ready(function() {
  cart = []
  if (localStorage["cart"]) {
    cart = JSON.parse(localStorage["cart"]);
  }
  validateCart();
  fillCart();
});

function addItem(id, quantity = 1) {
  var item = findItem(id);
  if (item) {
    item.quantity += quantity;
  }

  validateCart();
  fillCart();

  return false;
}

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
  fillCart();
  return false;
}

function removeItem(id, quantity = 1) {
  var item = findItem(id);
  if (item) {
    item.quantity -= 1;

    if (item.quantity <= 0) {
      var index = cart.indexOf(item);
      cart.splice(index, 1);
    }
  }

  localStorage["cart"] = JSON.stringify(cart);
  validateCart();
  fillCart();
  return false;
}

function removeAllItems(id) {
  var item = findItem(id);
  var index = cart.indexOf(item);
  cart.splice(index)

  localStorage["cart"] = JSON.stringify(cart);
  validateCart();
  fillCart();
  return false;
}

function clearCart() {
  delete localStorage["cart"];
  validateCart();
  fillCart();
  return false;
}

function validateCart() {
  var $cart = $(".cart");
  var cartEmpty = cart.length == 0;
  if (cartEmpty) {
    $cart.removeClass("icon-blue");
  } else {
    $cart.addClass("icon-blue");
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

function fillCart() {
  var list = $("#cart_list");
  list.empty();
  for (var i = 0; i < cart.length; ++i) {
    list.append(
      "<tr>" +
        "<td>" + cart[i]["name"] + "</td>" +
        "<td>₴" + cart[i]["price"] + "</td>" +
        "<td>" + cart[i]["quantity"] + "</td>" +
        "<td>" +
          "<a href='javascript:void(0);' onclick=addItem(" + cart[i]["id"] + ") class='black-text waves-effect waves-blue btn-flat'><i class='material-icons'>add</i></a>"+
          "<a href='javascript:void(0);' onclick=removeItem(" + cart[i]["id"] + ") class='black-text waves-effect waves-blue btn-flat'><i class='material-icons'>remove</i></a>"+
          "<a href='javascript:void(0);' onclick=removeAllItems(" + cart[i]["id"] + ") class='black-text waves-effect waves-blue btn-flat'><i class='material-icons'>delete</i></a>"+
        "</td>" +
      "</tr>");
  }

  return false;
}
