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
            const catalogItemsContainer = document.getElementById('catalogItemsContainer');
            const firstItem = catalogItemsContainer.querySelector('.catalog-item:not(:first-child)');

            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = data.html;
            const newItem = tempDiv.firstElementChild;
            newItem.classList.add('fade-in-scale-up');

            if (firstItem) {
                firstItem.insertAdjacentElement('beforebegin', newItem);
                newItem.classList.add('catalog-item');
            } else {
                catalogItemsContainer.insertAdjacentElement('beforeend', newItem);
            }
            const items = catalogItemsContainer.getElementsByClassName('catalog-item');
            const itemsPerPage = 11;
            if (items.length > itemsPerPage) {
                catalogItemsContainer.removeChild(items[itemsPerPage]);
            }

            modal.style.display = 'none';
            form.reset();
            showNotification('Item added successfully!', true);
            setTimeout(() => {
            newItem.classList.remove('fade-in-scale-up');
             }, 2000);
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

document.addEventListener('DOMContentLoaded', () => {
  const catalogItemsContainer = document.getElementById('catalogItemsContainer');

  catalogItemsContainer.addEventListener('click', function(event) {
    const item = event.target.closest('.catalog-item');
    if (item) {
      item.classList.toggle('expanded');

      if (!item.querySelector('.close-button')) {

        closeButton.addEventListener('click', function(closeEvent) {
          closeEvent.stopPropagation();
          item.classList.remove('expanded');
        });
      }
    }
  });
});

document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.delete-button').forEach(function(button) {
    button.addEventListener('click', function(event) {
      event.stopPropagation();

      var catalogItem = this.closest('.catalog-item');
      if (catalogItem.classList.contains('expanded')) {
        catalogItem.classList.remove('expanded');
      }
      });
  });
});


// фывафыва


function rearrangeElements() {
    const catalogItems = document.querySelectorAll('.catalog-item');

    catalogItems.forEach(item => {
        const deleteButtonContainer = item.querySelector('.delete-button-container');
        const imageContainer = item.querySelector('.catalog-image-container');

        if (window.innerWidth < 768) {
            item.insertBefore(deleteButtonContainer, imageContainer);
        } else {
            imageContainer.insertBefore(deleteButtonContainer, imageContainer.firstChild);
        }
    });
}

document.addEventListener('DOMContentLoaded', rearrangeElements);
window.addEventListener('resize', rearrangeElements);

rearrangeElements();