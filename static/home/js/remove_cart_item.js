function delete_cart_item(cart_id) {
    const url = `/api/remove-cart-item/${cart_id}`
    $.ajax({
        url,
        method: 'GET',
        mode: 'cors',
        success: function (result) {
            $(`#item_${cart_id}`).remove()
        }
    })
}