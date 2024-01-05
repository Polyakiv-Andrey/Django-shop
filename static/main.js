function toggleHeaders() {

  var mainHeader = document.getElementById("main-header");
  var adminHeader = document.getElementById("admin-header");

  if (mainHeader.style.display === "none") {
    mainHeader.style.display = "block";
    adminHeader.style.display = "none";
  } else {
    mainHeader.style.display = "none";
    adminHeader.style.display = "block";
  }
}

function toggleMenu() {
    var navigation = document.getElementById("navigation");
    var logo = document.getElementById("logo");
    var companyName = document.querySelector(".company-name");
    var admin = document.querySelector(".admin-button");
    var icon = document.getElementById("burger");
    var basket = document.getElementById("basket");

    if (navigation.style.display === "block") {
        navigation.style.display = "none";
        if (logo) logo.style.display = "block";
        if (companyName) companyName.style.display = "block";
        if (admin) admin.style.display = "block";
        if (basket) basket.style.display = "block";
        icon.classList.remove('fa-arrow-right');
        icon.classList.add('fa-bars');
    } else {
        navigation.style.display = "block";
        if (logo) logo.style.display = "none";
        if (companyName) companyName.style.display = "none";
        if (admin) admin.style.display = "none";
        if (basket) basket.style.display = "none";
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-arrow-right');
    }
}


function toggleAdminMenu() {
    var navigation = document.querySelector(".admin-navigation");
    var logo = document.querySelector(".logo");
    var companyName = document.querySelector(".company-name-admin");
    var admin = document.querySelector(".admin-button-panel");
    var icon =document.querySelector(".burger");
    if (navigation.style.display === "block") {
        navigation.style.display = "none";
        if (logo) logo.style.display = "block";
        if (companyName) companyName.style.display = "block";
        if (admin) admin.style.display = "block";
        icon.classList.remove('fa-arrow-right');
        icon.classList.add('fa-bars');
    } else {
        navigation.style.display = "block";
        if (logo) logo.style.display = "none";
        if (companyName) companyName.style.display = "none";
        if (admin) admin.style.display = "none";
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-arrow-right');
    }
}

document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('catalogItemModal');

  document.getElementById('addCatalogItemBtn').addEventListener('click', function() {
    fetch('/admin_panel/catalog-item-add/')
      .then(response => response.text())
      .then(html => {
        document.getElementById('catalogItemModalContent').innerHTML = html;
        modal.style.display = 'block';
        addFormSubmitHandler();
        addCancelEventHandler()
      });
  });

  function showNotification(message, isSuccess = true) {
  const notification = document.getElementById('notification');
  notification.textContent = message;
  notification.style.backgroundColor = isSuccess ? '#4CAF50' : '#f44336';
  notification.classList.add('show');

  setTimeout(() => {
    notification.classList.remove('show');
  }, 3000);
}

  function addFormSubmitHandler() {
    const form = document.getElementById('catalogItemForm');
    if (form) {
      form.addEventListener('submit', function(e) {
        e.preventDefault();

        fetch(form.action, {
          method: 'POST',
          body: new FormData(form),
          headers: {
            'X-Requested-With': 'XMLHttpRequest'
          }
        })
        .then(response => response.json())
        .then(data => {
          if (data.status === 'success') {
            modal.style.display = 'none';
            showNotification('Success', true);
          } else if (data.status === 'error') {
            showNotification(Object.values(data.errors).join(', '), false);
          }
        })
        .catch(error => {
          console.error('Error:', error);
          alert('Error: ' + error);
        });
      });
    } else {
      console.error('Form not found');
    }
  }
});

function addCancelEventHandler() {
  const cancelButton = document.getElementById('cancelButton');
  if (cancelButton) {
    cancelButton.addEventListener('click', function() {
      document.getElementById('catalogItemModal').style.display = 'none';
    });
  } else {
    console.error('Cancel button not found');
  }
}


document.addEventListener('DOMContentLoaded', function() {
  var toggleButtons = document.querySelectorAll('.toggleButton');
  var leftColumn = document.querySelector('.grid-item.left');
  var rightColumn = document.querySelector('.grid-item.right');

  function toggleColumns() {
    if (window.getComputedStyle(leftColumn).display === 'none') {
      rightColumn.style.display = 'none';
      leftColumn.style.display = 'block';
      rightColumn.style.transform = 'translateX(100%)';
      leftColumn.style.transform = 'translateX(0)';
    } else {
      leftColumn.style.display = 'none';
      rightColumn.style.display = 'block';
      leftColumn.style.transform = 'translateX(-100%)';
      rightColumn.style.transform = 'translateX(0)';
    }
  }

  toggleButtons.forEach(function(btn) {
    btn.addEventListener('click', toggleColumns);
  });
});