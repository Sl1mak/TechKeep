const buttons = document.querySelectorAll('.catalog_item');
const products = document.querySelectorAll('.catalog_product');
const newProductModalBtn = document.getElementById('newProductModalBtn');
const newProductModal = document.getElementById('newProductModal');
const newProductModalContent = document.getElementById('newProductModalContent');
const closeNewProductModal = document.getElementById('closeNewProductModal');
const deleteProductBtn = document.querySelectorAll('.delete_button');
const exitBtn = document.getElementById('exitButton');

let activeCategories = new Set();

buttons.forEach(btn => {
    btn.addEventListener('click', () => {
        const category = btn.dataset.category;

        btn.classList.toggle('active');

        if (activeCategories.has(category)) {
            activeCategories.delete(category);
        } else {
            activeCategories.add(category);
        }

        filterProducts();
    });
});

function filterProducts() {
    products.forEach(product => {
        const productCategory = product.dataset.category;

        if (activeCategories.size === 0 || activeCategories.has(productCategory)) {
            product.style.display = 'flex';
        } else {
            product.style.display = 'none'
        }
    });
}

if (newProductModalBtn) {
  newProductModalBtn.onclick = function() {
    newProductModal.style.display = "block";
  }
}

if (closeNewProductModal) {
  closeNewProductModal.onclick = function() {
    newProductModal.style.display = "none";
  }
}

window.onclick = function(event) {
  if (event.target == newProductModal) {
    newProductModal.style.display = "none";
  }
}

newProductModal.addEventListener('submit', function (e) {
  e.preventDefault();

  const formdata = new FormData(newProductModal);
  const room_id = e.currentTarget.dataset.id;

  fetch(`/add_product/${room_id}/`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
    },
    "body": formdata,
    credentials: 'same-origin',
  })
  .then(responce => responce.json())
  .then(data => {
    if (data.success) {
      location.reload();
      alert(data.message);
    }
    else {
      alert(data.message);
    }
  })
})

deleteProductBtn.forEach(btn => {
  btn.addEventListener('click', function (e) {
    const product_id = e.target.dataset.id;

    fetch(`/delete_product/${product_id}/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
      },
      credentials: 'same-origin',
    })
    .then(responce => responce.json())
    .then(data => {
      alert(data.message);
      if (data.success) {
        location.reload();
      }
    })
  })
})

exitBtn.addEventListener('click', function (e) {
  const room_id = e.currentTarget.dataset.id;

  fetch(`/exit_room/${room_id}/`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
    },
    credentials: 'same-origin',
  })
  .then(responce => responce.json())
  .then(data => {
    alert(data.message);
    if (data.success) {
      window.location.href='/';
    }
  })
})

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}