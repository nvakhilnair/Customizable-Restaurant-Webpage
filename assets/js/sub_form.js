$(document).on('submit','#task-form',function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url: 'add_subcriber/',
        data:
        {
            task:$("#subs-email").val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
              alert('Saved');
                }
        })
    });