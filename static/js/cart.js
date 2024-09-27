document.querySelectorAll('.ezy__epcart6_P6mymb4f-qty .btn').forEach(function (button) {
    button.addEventListener('click', function () {
        const input = this.parentElement.querySelector('input');
        let value = parseInt(input.value);
        if (this.textContent === '+') {
            value += 1;
        } else if (this.textContent === '-' && value > 1) {
            value -= 1;
        }
        input.value = value;
    });
});


document.querySelectorAll('.ezy__epcart6_P6mymb4f-qty .btn').forEach(function (button) {
    button.addEventListener('click', function () {
        const input = this.parentElement.querySelector('input');
        let value = parseInt(input.value);
        if (this.textContent === '+') {
            value += 1;
        } else if (this.textContent === '-' && value > 1) {
            value -= 1;
        }
        input.value = value;
    });
});

function removeItem(itemId) {
  // Пример запроса удаления товара
  fetch(`/cart/remove/${itemId}/`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken,  // Django CSRF-токен
    },
  }).then(response => {
    if (response.ok) {
      location.reload();  // Обновить страницу после успешного удаления
    }
  });
}
function updateBuyButton() {
  const selectedItems = document.querySelectorAll('.form-check-input:checked').length;
  document.querySelector('.btn.ezy__epcart6_P6mymb4f-btn.w-100').textContent = `BUY (${selectedItems})`;
}

document.querySelectorAll('.form-check-input').forEach(function(input) {
  input.addEventListener('change', updateBuyButton);
});

