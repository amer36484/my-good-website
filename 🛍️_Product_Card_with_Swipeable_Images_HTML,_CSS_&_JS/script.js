const colorOptions = document.querySelectorAll('.color-option input');
const productImages = document.querySelectorAll('.product-images img');
const addToCartBtn = document.getElementById('add-to-cart'); // Add to Cart button

let selectedColor = null;

// Change product image based on selected color
colorOptions.forEach((option) => {
    option.addEventListener('change', (event) => {
        selectedColor = event.target.value;

        // Hide all images
        productImages.forEach((image) => {
            image.classList.remove('active');
        });

        // Show the selected image
        const selectedImage = document.querySelector(`.product-images img.${selectedColor}`);
        if (selectedImage) {
            selectedImage.classList.add('active');
        }
    });
});

// Add to Cart alert
addToCartBtn.addEventListener('click', () => {
    if (selectedColor) {
        alert(`Product added to cart! Color: ${selectedColor}`);
    } else {
        alert("Please select a color first!");
    }
});
