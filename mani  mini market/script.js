// Enhanced English product data with categories and inline SVG images (represented by emoji here)
const products = [
  { id:1, name:'Apple', emoji:'🍎', price:0.80, desc:'Fresh red apple', category:'fruits' },
  { id:2, name:'Banana', emoji:'🍌', price:0.60, desc:'Sweet yellow banana', category:'fruits' },
  { id:3, name:'Carrot', emoji:'🥕', price:0.30, desc:'Crunchy carrot', category:'veggies' },
  { id:4, name:'Tomato', emoji:'🍅', price:0.45, desc:'Juicy tomato', category:'veggies' },
  { id:5, name:'Cucumber', emoji:'🥒', price:0.50, desc:'Crisp cucumber', category:'veggies' },
  { id:6, name:'Orange', emoji:'🍊', price:0.70, desc:'Vitamin C orange', category:'fruits' },
  { id:7, name:'Organic Banana', emoji:'🍌', price:0.95, desc:'Organic banana', category:'organic' },
  { id:8, name:'Spinach', emoji:'🥬', price:0.55, desc:'Fresh spinach leaves', category:'veggies' }
];

// Cart stored in localStorage for persistence
let cart = JSON.parse(localStorage.getItem('market_cart') || '{}');

function fmt(value){ return '$' + value.toFixed(2); }

// Render products with category data and add tilt effect listeners
const productsRoot = document.getElementById('products');
function renderProducts(filter='all'){
  productsRoot.innerHTML = '';
  const list = products.filter(p => filter === 'all' ? true : p.category === filter);
  list.forEach(p => {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
      <div class="card-inner">
        <div class="prod-image" aria-hidden="true"><div class="prod-emoji">${p.emoji}</div></div>
        <div class="prod-name">${p.name}</div>
        <div class="prod-desc">${p.desc}</div>
        <div class="price-row">
          <div><strong>${fmt(p.price)}</strong></div>
          <div class="qty-controls">
            <button class="small" onclick="addToCart(${p.id},1)" aria-label="Add one ${p.name}">+1</button>
            <button class="add-btn" onclick="addToCart(${p.id},3)" aria-label="Add three ${p.name}">Add to Cart</button>
          </div>
        </div>
      </div>
    `;
    // Tilt effect on mouse move
    card.addEventListener('mousemove', e => {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      const rx = -y * 8; // rotateX
      const ry = x * 10; // rotateY
      card.style.transform = `translateY(-8px) rotateX(${rx}deg) rotateY(${ry}deg) scale(1.02)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
    productsRoot.appendChild(card);
  });
}

renderProducts();

// Filter buttons
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderProducts(btn.dataset.cat);
  });
});

// Save cart to localStorage
function saveCart(){ localStorage.setItem('market_cart', JSON.stringify(cart)); updateCartSummary(); }

// Add to cart
function addToCart(productId, amount=1){
  cart[productId] = (cart[productId] || 0) + amount;
  if(cart[productId] > 99) cart[productId] = 99;
  saveCart();
  renderCart();
}

// Increase / decrease
function decrease(productId){
  if(!cart[productId]) return;
  cart[productId]--;
  if(cart[productId] <= 0) delete cart[productId];
  saveCart();
  renderCart();
}

function increase(productId){ addToCart(productId,1); }

function removeItem(productId){ delete cart[productId]; saveCart(); renderCart(); }

function clearCart(){ cart = {}; saveCart(); renderCart(); }

// Render cart
function renderCart(){
  const cartItemsRoot = document.getElementById('cart-items');
  cartItemsRoot.innerHTML = '';
  let subtotal = 0;
  let totalItems = 0;

  Object.keys(cart).forEach(id => {
    const qty = cart[id];
    const product = products.find(p => p.id === Number(id));
    const lineTotal = product.price * qty;
    subtotal += lineTotal;
    totalItems += qty;

    const item = document.createElement('div');
    item.className = 'cart-item';
    item.innerHTML = `
      <div class="meta">
        <b>${product.emoji} ${product.name} × ${qty}</b>
        <div class="muted">${fmt(product.price)} each • ${fmt(lineTotal)}</div>
      </div>
      <div class="controls">
        <button class="small" onclick="decrease(${product.id})" aria-label="Decrease ${product.name}">-</button>
        <button class="small" onclick="increase(${product.id})" aria-label="Increase ${product.name}">+</button>
        <button class="small" style="background:#ffdede;color:#a33" onclick="removeItem(${product.id})" aria-label="Remove ${product.name}">Remove</button>
      </div>
    `;
    cartItemsRoot.appendChild(item);
  });

  // Discount rule: $10+ => 5% off
  let discount = 0;
  if(subtotal > 10) discount = +(subtotal * 0.05).toFixed(2);
  // Tax 8%
  const tax = +((subtotal - discount) * 0.08).toFixed(2);
  const grand = +(subtotal - discount + tax).toFixed(2);

  document.getElementById('subtotal').textContent = fmt(subtotal);
  document.getElementById('tax-amount').textContent = fmt(tax);
  if(discount > 0){
    document.getElementById('discount-row').style.display = 'block';
    document.getElementById('discount-amount').textContent = '-'+fmt(discount);
  } else {
    document.getElementById('discount-row').style.display = 'none';
  }
  document.getElementById('grand-total').textContent = fmt(grand);

  document.getElementById('cart-count').textContent = totalItems;
  document.getElementById('cart-total').textContent = fmt(grand);

  if(totalItems === 0){
    cartItemsRoot.innerHTML = '<div style="color:var(--muted); padding:8px">Your cart is empty — pick something fresh!</div>';
  }
}

// Checkout modal controls
function openCheckout(){
  const total = document.getElementById('grand-total').textContent;
  document.getElementById('checkout-total').textContent = total;
  const modal = document.getElementById('checkout-modal');
  modal.setAttribute('aria-hidden','false');
  document.body.style.overflow = 'hidden';
}

function closeCheckout(){
  const modal = document.getElementById('checkout-modal');
  modal.setAttribute('aria-hidden','true');
  document.body.style.overflow = '';
}

// Checkout submission: create order and redirect to account page
function submitCheckout(e){
  e.preventDefault();
  const form = e.target;
  const fullname = form.fullname.value.trim();
  const email = form.email.value.trim();
  const address = form.address.value.trim();
  if(!fullname || !email || !address){
    alert('Please fill name, email and address.');
    return;
  }
  const subtotal = Object.keys(cart).reduce((s,id)=>{
    const p = products.find(x=>x.id===Number(id));
    return s + p.price * cart[id];
  }, 0);
  let discount = 0;
  if(subtotal > 10) discount = +(subtotal * 0.05).toFixed(2);
  const tax = +((subtotal - discount) * 0.08).toFixed(2);
  const total = +(subtotal - discount + tax).toFixed(2);

  const order = {
    id: 'ORD-' + Date.now(),
    customer: { fullname, email, address },
    items: Object.keys(cart).map(id=>{
      const p = products.find(x=>x.id===Number(id));
      return { id: p.id, name: p.name, qty: cart[id], price: p.price, lineTotal: +(p.price * cart[id]).toFixed(2) };
    }),
    subtotal: +subtotal.toFixed(2),
    discount,
    tax,
    total,
    createdAt: new Date().toISOString()
  };

  // Save order to orders list
  const orders = JSON.parse(localStorage.getItem('market_orders') || '[]');
  orders.push(order);
  localStorage.setItem('market_orders', JSON.stringify(orders));

  // Clear cart
  clearCart();
  closeCheckout();

  // Redirect to account page with order id
  window.location.href = 'account.html?order=' + encodeURIComponent(order.id);
}

// Update cart summary in header
function updateCartSummary(){
  const subtotal = Object.keys(cart).reduce((s,id)=>{
    const p = products.find(x=>x.id===Number(id));
    return s + p.price * cart[id];
  }, 0);
  let discount = 0;
  if(subtotal > 10) discount = +(subtotal * 0.05).toFixed(2);
  const tax = +((subtotal - discount) * 0.08).toFixed(2);
  const grand = +(subtotal - discount + tax).toFixed(2);
  document.getElementById('cart-count').textContent = Object.values(cart).reduce((s,n)=>s+n,0);
  document.getElementById('cart-total').textContent = fmt(grand || 0);
}

// Initial render and save
renderCart();
saveCart();
