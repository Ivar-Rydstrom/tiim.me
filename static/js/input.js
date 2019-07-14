
var title = document.getElementById('title');

title.onfocus = function() {
  if (title.value == default_event) {
    title.value = '';
  }
}

title.onblur = function() {
  if (title.value == '') {
    title.filled = false;
    title.value = default_event;
  } else {
    title.filled = true;
    check_filled();
  }
}


var description = document.getElementById('description');

description.onfocus = function() {
  if (description.value == default_description) {
    description.value = '';
  }
}

description.onblur = function() {
  if (description.value == '') {
    description.filled = false;
    description.value = default_description;
  } else {
    description.filled = true;
    check_filled()
  }
}


var end_time = document.getElementById('end_time');
end_time.value = get_current_time_ISO();
