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
    fetch('/catalog/catalog-item-add/')
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
            window.location.reload();
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


document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('catalogItemModal');

  document.getElementById('addProductItemBtn').addEventListener('click', function() {
    fetch('/products/create/')
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
            form.reset();
            window.location.reload();
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


function initializeAddImageButton() {
  var counterElement = document.getElementById('counter');
  var currentForm = parseInt(counterElement.value, 10);
  var maxForms = 20;
  var imagesFormContainer = document.getElementById('imagesFormContainer');

  if (currentForm < maxForms) {
    var nextForm = document.querySelector('.image' + (currentForm + 1));
    if (nextForm) {
      var allDeleteButtons = document.querySelectorAll('.images-form .deleteImage');
      allDeleteButtons.forEach(button => {
        button.style.display = 'none';
      });

      nextForm.style.display = 'block';

      var deleteButtonInNextForm = nextForm.querySelector('.deleteImage');
      if (deleteButtonInNextForm) {
        deleteButtonInNextForm.style.display = 'block';
      }

      currentForm++;

        var fileInput = nextForm.querySelector('input[type="file"]');
        if (fileInput) {
          fileInput.addEventListener('change', function(event) {
            let for_slice = fileInput.id.slice(-7)
            var file = event.target.files[0];
            if (file) {
              var reader = new FileReader();
              console.log(reader)
              reader.onload = function(e) {
                var label = document.querySelector(`label[for$="${for_slice}"]`);
                label.style.backgroundImage = 'url(' + e.target.result + ')';
                label.style.backgroundSize = 'cover';
                label.style.backgroundPosition = 'center';
                label.style.backgroundRepeat = 'no-repeat';
                label.style.color = 'transparent';
              };
              reader.readAsDataURL(file);
            }
          });
        }
    const inputs = document.querySelectorAll('[id$="-color"]');

    inputs.forEach(input => {
        input.placeholder = "Correct color change background";
        input.addEventListener('input', onInputChange);
    });

    function onInputChange(event) {
        const value = event.target.value;
        console.log(value);
        event.target.style.backgroundColor = value;
    }
    const checkbox = document.getElementById('priceDependsOnColor');
    const colorInputs = document.querySelectorAll('[id$="-color"]');
    const priceInputs = document.querySelectorAll('[id$="-price"]');
    colorInputs.forEach(input => {
        input.disabled = true;
        input.style.backgroundColor = "Gray";
        input.value = "";
    });
    priceInputs.forEach(input => {
        input.disabled = true;
        input.style.backgroundColor = "Gray";
        input.value = "";
    });
    checkbox.addEventListener('input', function (event) {
        if (!checkbox.checked) {
            colorInputs.forEach(input => {
                input.disabled = true;
                input.style.backgroundColor = "Gray";
                input.value = "";
            });
        priceInputs.forEach(input => {
        input.disabled = true;
        input.style.backgroundColor = "Gray";
        input.value = "";
    });

        } else {
            colorInputs.forEach(input => {
                input.disabled = false;
                input.style.backgroundColor = "White";
            });
            priceInputs.forEach(input => {
                input.disabled = false;
                input.style.backgroundColor = "White";
            });
        }
    });
    const mainCheckBoxes = document.querySelectorAll('[id$="-main"]')
    function updateCheckBoxes() {
    const allUnchecked = Array.from(mainCheckBoxes).every(chk => !chk.checked);

        if (allUnchecked) {
            mainCheckBoxes[0].checked = true;
        }
    }
    mainCheckBoxes.forEach((checkbox, index) => {
        checkbox.addEventListener('change', function() {
            if (index === 0 && !this.checked) {
                this.checked = true;
            } else {
                if (this.checked) {
                    Array.from(mainCheckBoxes).forEach((chk, idx) => {
                        if (idx !== index) {
                            chk.checked = false;
                        }
                    });
                }
            }
        });
    });

        updateCheckBoxes();

      if (currentForm > 0){
          imagesFormContainer.style.display = 'block';
      }
      console.log(currentForm);
      counterElement.value = currentForm.toString();
    }
  }
}

function closeAddImageBlock() {
  var counterElement = document.getElementById('counter');
  var currentForm = parseInt(counterElement.value, 10);
  var minForms = 0;
  var imagesFormContainer = document.getElementById('imagesFormContainer');

  if (currentForm > minForms) {
    var currentFormElement = document.querySelector('#formsContainer .image' + currentForm);
    if (currentFormElement) {
      var label = document.querySelector(`label[for$="${currentForm - 1}-image"]`);
      label.style.backgroundImage = "url('../static/images/uploude.png')";
      var inputs = currentFormElement.querySelectorAll('input');
      inputs.forEach(function(input) {
        input.value = '';
      });

      currentFormElement.style.display = 'none';
      currentForm--;
      counterElement.value = currentForm.toString();
      if (currentForm > 0) {
        var prevFormElement = document.querySelector('#formsContainer .image' + currentForm);
        if (prevFormElement) {
          var deleteButtonInPrevForm = prevFormElement.querySelector('.deleteImage');
          if (deleteButtonInPrevForm) {
            deleteButtonInPrevForm.style.display = 'block';
          }
        }
      } else {
        imagesFormContainer.style.display = 'none';
      }
    }
    const mainCheckBox = document.querySelector(`[id$="${currentForm - 1}-main"]`)
      console.log(currentForm - 1)
       if (mainCheckBox && !mainCheckBox.checked) {
            mainCheckBox.value = false;
             const mainCheckBoxes = document.querySelectorAll(`[id$="-main"]`)
           mainCheckBoxes.forEach(box => {
                box.checked = false;
            });
            const firstCheckBox = document.querySelector('[id$="0-main"]');
            if (firstCheckBox) {
                firstCheckBox.checked = true;
            }
        }
  }
}

function initializeAddAttributeButton() {
  var counterElement = document.getElementById('counterProperties');
  var currentForm = parseInt(counterElement.value, 10);
  var maxForms = 150;
  var propertiesFormContainer = document.getElementById('propertiesFormContainer');
  if (currentForm < maxForms) {
    var nextForm = document.querySelector('.property' + (currentForm + 1));
    if (nextForm) {
        nextForm.style.display = 'block';
        currentForm++

        let deleteCheckBoxes = document.querySelectorAll(`[id$="-DELETE"]`)
        deleteCheckBoxes.forEach((deleteCheckBox) => {
            deleteCheckBox.addEventListener('change', function() {
                if (deleteCheckBox.checked === true) {
                    console.log(`.property${+deleteCheckBox.id.split("-")[1] + 1}`)
                    let propertyBlock = document.querySelector(`.property${+deleteCheckBox.id.split("-")[1] + 1}`)
                    console.log(propertyBlock)
                    propertyBlock.style.display = "none"
                    let propertyForms = document.querySelectorAll('.propertyForm')
                    let allHidden = Array.from(propertyForms).every(form => form.style.display === 'none');
                    if (allHidden) {
                        propertiesFormContainer.style.display = 'none';
                    }
                }
            })
        })
        let keyInputs =  document.querySelectorAll(`[id$="-name"]`)
        keyInputs.forEach((element) => {
            element.style.width = "40%"
            element.placeholder = "Property"
            element.style.marginBottom = "10px"
            })
        let valueInputs =  document.querySelectorAll(`[id$="-value"]`)
        valueInputs.forEach((element) => {
            element.style.width = "40%"
            element.placeholder = "Value"
            })
        let titleInputs =  document.querySelectorAll(`[id$="-title"]`)
        titleInputs.forEach((element) => {
            element.addEventListener('change', function() {
                let valueInput =  document.querySelector(`[id$="${element.id.split("-")[1]}-value"]`)
                let keyInput =  document.querySelector(`[id$="${element.id.split("-")[1]}-name"]`)
                 if (element.checked === true) {
                     valueInput.disabled = true
                     valueInput.style.backgroundColor = "Gray"
                     valueInput.value = ""
                     valueInput.placeholder = ""
                     keyInput.placeholder = "Title"
                 } else {
                     valueInput.disabled = false;
                     valueInput.style.backgroundColor = "White"
                     valueInput.placeholder = "Value"
                     keyInput.placeholder = "Property"
                 }
            })
            element.style.transform = "scale(2)";
            element.style.margin = "2%"
            })
        let deleteInputs =  document.querySelectorAll(`[id$="-DELETE"]`)
       deleteInputs.forEach((element) => {
            element.style.transform = "scale(2)";
            element.style.margin = "2%"
            })
    }
          if (currentForm > 0){
          propertiesFormContainer.style.display = 'block';
          counterElement.value = currentForm.toString();
    }
  }
}

function initializeAddDiscountButton() {
      var discountFormContainer = document.getElementById('discountContainer');
      discountFormContainer.style.display = "block"
      var discountCansel = document.getElementById('cancelDiscount');
      var percentage = document.getElementById("id_discounts-0-percentage")
      var start_date = document.getElementById("id_discounts-0-start_date")
      var end_date = document.getElementById("id_discounts-0-end_date")
      let labels = document.querySelectorAll(".discounts-form label")
        labels.forEach((label) => {
            label.classList.add("file-upload-label");
        })
      console.log(labels)
        percentage.placeholder = 20
        start_date.placeholder = "YYYY-MM-DD HH:MM"
        start_date.style.width = "60%"
        end_date.placeholder = "YYYY-MM-DD HH:MM"
        end_date.style.width = "60%"
      discountCansel.addEventListener('click', function() {
          discountFormContainer.style.display = "none"
          percentage.value = ""
          start_date.value = ""
          end_date.value = ""
      })
}


