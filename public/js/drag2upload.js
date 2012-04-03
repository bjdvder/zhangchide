$(function () {
      window.ondragover = function () {
          return false;
      };
      window.ondragend = function () {
          return false;
      };

      var getImgSize = function (imgSrc) {
          var newImg = new Image();
          newImg.src = imgSrc;
          return {'width': newImg.width, 'height': newImg.height};
      };

      window.ondrop = function (e) {
          var file = e.dataTransfer.files[0];
          if (file.type != 'image/png') {
              console.log('Please drag an image to me!');
              return;
          }
          console.log('file:', file);
          console.log('name:', file.name);
          console.log('size:', file.size);
          var reader = new FileReader();
          reader.onload = function (e) {
              var data = this.result;
              var imgSize = getImgSize(data);
              $('img').css(imgSize).attr('src', data);

          };
          reader.readAsDataURL(file);

          var binReader = new FileReader();
          binReader.onload = function (e) {
              var data = this.result;
              var token = $('#csrfmiddlewaretoken').val(),
              dataStr = 'csrfmiddlewaretoken='.concat(encodeURIComponent(token),
                                                      '&enctype=', encodeURIComponent('multipart/form-data'),
                                                      '&picfile=', encodeURIComponent(data),
                                                      '&name=', encodeURIComponent(file.name));
              console.log(data);
              console.log(encodeURIComponent(data));
              $.ajax({url:'/fun/j_upload/',
                      type: 'POST',
                      data: dataStr,
                      processData: false,
                      contentType: false,
                      cache: false});              
          };
          binReader.readAsDataURL(file);
          //binReader.readAsBinaryString(file);
      };
  });
