$(function () {
      var slider = $('#gallery .slider'),
      features = $('.feature');
      var moveSlider = function (name) {
          var p = $('#photo-'.concat(name));
          if (p) {
              var newLeft = -p.position().left;
              slider.animate({'left': newLeft}, 700);
          }
      },
      activeFeature = function (name) {
          features.removeClass('active');
          $('#'.concat(name)).addClass('active');
          moveSlider(name);
      };
      $('.feature').mouseenter(
          function () {
              activeFeature($(this).attr('id'));
          });
  });
