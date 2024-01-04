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