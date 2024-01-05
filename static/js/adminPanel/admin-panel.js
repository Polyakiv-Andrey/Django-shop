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