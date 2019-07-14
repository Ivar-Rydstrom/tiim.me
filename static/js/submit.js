var submit = document.getElementById('submit');

var title = document.getElementById('title');
title.filled = false;

var description = document.getElementById('description');
description.filled = false;


var check_filled = function() {
  if (title.filled && description.filled) {
    submit.disabled = false;
  }
}
