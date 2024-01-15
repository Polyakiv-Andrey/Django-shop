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
            if (firstItem) {
              firstItem.insertAdjacentHTML('beforebegin', data.html);
            } else {

                catalogItemsContainer.insertAdjacentHTML('beforeend', data.html);
            }
            const items = catalogItemsContainer.getElementsByClassName('catalog-item');
            const itemsPerPage = 11;
            if (items.length > itemsPerPage) {
              catalogItemsContainer.removeChild(items[items.length - 1]);
            }
            modal.style.display = 'none';
            form.reset();
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

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.edit-button').forEach(button => {
    button.addEventListener('click', function(event) {
      event.stopPropagation();

      document.querySelectorAll('.catalog-item.expanded').forEach(item => {
        item.classList.remove('expanded');
      });

      const itemId = this.getAttribute('data-id');
      openEditForm(itemId);

});
    });
  });


function openEditForm(itemId) {
  fetch(`../catalog/${itemId}/update/`)
    .then(response => response.text())
    .then(html => {
      const modalContent = document.getElementById('catalogItemModalContent');
      modalContent.innerHTML = html;

      const modal = document.getElementById('catalogItemModal');
      modal.style.display = 'block';

      updateFormSubmitHandler()
        addCancelEventHandler()
    })
    .catch(error => {
      console.error('Error loading edit form:', error);
    });
}

function updateFormSubmitHandler() {
  const form = document.getElementById('catalogItemForm');
  if (form) {
    form.addEventListener('submit', function(event) {
      event.preventDefault();

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
            window.location.reload();
        } else if (data.status === 'error') {
          showNotification(Object.values(data.errors).join(', '), false);
        }
      })
      .catch(error => {
        console.error('Error:', error);
        showNotification('Error: ' + error, false);
      });
    });
  } else {
    console.error('Form not found');
  }
}

function showNotification(message, isSuccess) {
  const notification = document.getElementById('notification');
  notification.textContent = message;
  notification.style.backgroundColor = isSuccess ? '#4CAF50' : '#f44336';
  notification.classList.add('show');

  setTimeout(() => {
    notification.classList.remove('show');
  }, 3000);
}
