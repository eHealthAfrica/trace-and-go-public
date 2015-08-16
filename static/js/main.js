requirejs.config({
  paths: {
    "jquery": "//ehealthafrica.github.io/ehealth-bootstrap/js/thirdparty/jquery.min",
    "jquery.validate": "//ajax.aspnetcdn.com/ajax/jquery.validate/1.9/jquery.validate.min",
    "underscore": "//cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore-min",
    "bootstrap": "//ehealthafrica.github.io/ehealth-bootstrap/js/bootstrap.min",
    // "viewport-fix": "//ehealthafrica.github.io/ehealth-bootstrap/js/thirdparty/ie10-viewport-bug-workaround",
    "patient": "patient",
    "validatePatientForm": "validatePatientForm",
    "layout": "layout",
    "alerts": "alerts",
    "initialize-ajax": "initialize-ajax",
    "load-patient-form": "load-patient-form"
  },
  shim: {
    'jquery.validate': {
      deps: ['jquery']
    },
    'bootstrap': {
      deps: ['jquery']
    },
    'patient': {
      deps: ['jquery']
    },
    'alerts': {
      deps: ['jquery']
    },
    'initialize-ajax': {
      deps: ['jquery']
    },
    'load-patient-form': {
      deps: ['jquery']
    }
  }
});

define([
  'jquery',
  'jquery.validate',
  'bootstrap',
  'patient',
], function (jquery, validate, bootstrap, patient) {
  jquery(function() {
    patient.initialize();
  });
});

