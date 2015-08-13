define(['jquery', 'jquery.validate'], function(jquery) {

  var errorMessages = {
    "phoneNumber": "This doesn't look like a phone number, please try again."
  };

  function validate () {
    jquery.validator.addMethod("phoneNumber", function (value, element) {
      return this.optional(element) || /^\+?\d{4,}$/i.test(value);
    }, errorMessages.phoneNumber);
    jquery('#patientForm').validate({
      rules: {
        first_name: {
          required: true
        },
        last_name: {
          required: true
        },
        contact_phone_number: {
          required: true,
          phoneNumber: true
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
  }

  return {
    validate: validate
  };

});
