$().ready(function() {
  $('form').validate({
    rules: {
      firstName: {
        required: true
      },
      lastName: {
        required: true
      },
      phoneNumber: {
        required: true
      }
    },
    highlight: function(element) {
      $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
    },
    unhighlight: function(element) {
      $(element).closest('.form-group').removeClass('has-error').addClass('has-success');
    },
    errorElement: 'span',
    errorClass: 'help-block',
    errorPlacement: function(error, element) {
      if(element.length) {
        error.insertAfter(element);
      } else {
        error.insertAfter(element);
      }
    }
  });
});

