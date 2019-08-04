
var popup_settings = document.getElementById("popup-settings");
var nav_settings = document.getElementById("nav-settings");

console.log(nav_settings.offsetTop)
popup_settings.style.top = nav_settings.offsetTop;

nav_settings.onmouseenter = function() {
  popup_settings.style.display = "block";
}
nav_settings.onmouseout = function() {
  popup_settings.style.display = "none";
}


var popup_help = document.getElementById("popup-help");
var nav_help = document.getElementById("nav-help");

console.log(nav_help.offsetTop)
popup_help.style.top = nav_help.offsetTop;

nav_help.onmouseenter = function() {
  popup_help.style.display = "block";
}
nav_help.onmouseout = function() {
  popup_help.style.display = "none";
}


var popup_information = document.getElementById("popup-information");
var nav_information = document.getElementById("nav-information");

console.log(nav_information.offsetTop)
popup_information.style.top = nav_information.offsetTop;

nav_information.onmouseenter = function() {
  popup_information.style.display = "block";
}
nav_information.onmouseout = function() {
  popup_information.style.display = "none";
}
