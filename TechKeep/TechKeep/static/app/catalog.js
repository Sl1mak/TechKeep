document.querySelectorAll('.catalog_item').forEach(btn => {
    btn.addEventListener('click', () => {
        btn.classList.toggle('active');
    });
});