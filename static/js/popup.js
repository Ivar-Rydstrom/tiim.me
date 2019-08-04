
var popup_settings = document.getElementById("popup-settings");
var nav_settings = document.getElementById("nav-settings");

nav_settings.onmouseenter = function() {
  popup_settings.style.display = "block";
}
nav_settings.onmouseout = function() {
  popup_settings.style.display = "none";
}


var popup_help = document.getElementById("popup-help");
var nav_help = document.getElementById("nav-help");

nav_help.onmouseenter = function() {
  popup_help.style.display = "block";
}
nav_help.onmouseout = function() {
  popup_help.style.display = "none";
}


var popup_information = document.getElementById("popup-information");
var nav_information = document.getElementById("nav-information");

nav_information.onmouseenter = function() {
  popup_information.style.display = "block";
}
nav_information.onmouseout = function() {
  popup_information.style.display = "none";
}
