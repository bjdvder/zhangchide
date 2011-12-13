$(function () {
      var tasks = [];

      var Task = function (opt) {
          this.text = opt.text;
          this.con = this.draw();
      };
      Task.prototype.draw = function () {
          return $('#todo-list li').first().clone().find('label').text(this.text).end();
      };
      Task.prototype.close = function () {
          
      };

      $('#add-form').submit(
          function (e) {
              e.preventDefault();
              var text = $(this).find('#add-text').val();
              var t = new Task({text:text});
              t.con.appendTo('#todo-list');
          });
  });
