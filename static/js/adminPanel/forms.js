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
