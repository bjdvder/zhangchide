$(function () {
      var tasks = [], curInd = 0;

      var Task = function (opt) {
          this.index = opt.index;
          this.text = opt.text;
          this.con = this.draw();
      };
      Task.prototype.draw = function () {
          var con = $('#blank-li').clone().find('label').text(this.text).end().removeAttr('id').show();
          con[0].taskInst = this;
          return con;
      };
      Task.prototype.toggleComplete = function () {
          this.con.toggleClass('done');
      };
      Task.prototype.complete = function () {
          this.con.addClass('done');
          this.con.find('input[type=checkbox]').attr('checked', 'true');
      };
      Task.prototype.uncomplete = function () {
          this.con.removeClass('done');
          this.con.find('input[type=checkbox]').removeAttr('checked');
      };
      Task.prototype.delete = function () {
          this.con.remove();
          for(var i=0, len=tasks.length; i<len; i++) {
              var t = tasks[i];
              if (t.index == this.index) {
                  tasks.splice(i, 1);
                  break;
              }
          }
      };

      $('ul').delegate('li', 'click', function(e){
                           if (e.target.type === 'checkbox') {
                               this.taskInst && this.taskInst.toggleComplete();
                               return;
                           }

                           if (e.target.nodeName === 'A') {
                               this.taskInst && this.taskInst.delete();
                               return;
                           }
                       });

      $('#mark-all-done').click(
          function(e){
              for(var i=0, len=tasks.length; i<len; i++) {
                  var t = tasks[i];
                  if(e.target.checked)
                      t.complete();
                  else
                      t.uncomplete();
              }
          });

      $('#add-form').submit(
          function (e) {
              e.preventDefault();
              var textBox = $('#add-text');
              var text = textBox.val();
              textBox.val('');
              if (text) {
                  var t = new Task({text:text, index:curInd++});
                  $('#todo-list').append(t.con);
                  tasks.push(t);
              }
          });

  });
