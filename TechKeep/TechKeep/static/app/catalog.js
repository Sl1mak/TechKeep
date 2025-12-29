const buttons = document.querySelectorAll('.catalog_item');
const products = document.querySelectorAll('.catalog_product');

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