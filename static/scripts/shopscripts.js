document.addEventListener('DOMContentLoaded', function () {
    const productGrid = document.getElementById('productGrid');

    // Dummy data for product URLs and descriptions
    const products = Array.from({ length: 30 }, (_, index) => ({
        imageUrl: `https://via.placeholder.com/0500?text=Product${index + 1}`,
        description: `Product ${index + 1} Description`,
    }));

    // Create and append product items dynamically
    products.forEach(product => {
        const item = document.createElement('div');
        item.className = 'item';

        const anchor = document.createElement('a');
        anchor.href = '#';

        const img = document.createElement('img');
        img.src = product.imageUrl;
        img.alt = product.description;

        const p = document.createElement('p');
        p.textContent = product.description;

        // Append elements to the DOM
        anchor.appendChild(img);
        item.appendChild(anchor);
        item.appendChild(p);
        productGrid.appendChild(item);
    });
});
