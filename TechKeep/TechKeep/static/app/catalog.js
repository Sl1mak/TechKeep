const buttons = document.querySelectorAll('.catalog_item');
const products = document.querySelectorAll('.catalog_product');
const newProductModalBtn = document.getElementById('newProductModalBtn');
const newProductModal = document.getElementById('newProductModal');
const newProductModalContent = document.getElementById('newProductModalContent');
const closeNewProductModal = document.getElementById('closeNewProductModal');

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

newProductModalBtn.onclick = function() {
  newProductModal.style.display = "block";
}

closeNewProductModal.onclick = function() {
  newProductModal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == newProductModal) {
    newProductModal.style.display = "none";
  }
}

newProductModal.addEventListener('submit', function (e) {
  e.preventDefault();

  const formdata = new FormData(newProductModal);

  fetch('/add_product/', {
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