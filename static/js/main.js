requirejs.config({
  paths: {
    'jquery': '../bower_components/ehealth-bootstrap/js/thirdparty/jquery.min',
    'jquery.validate': '../bower_components/jquery-validation/jquery.validate',
    'underscore': '../bower_components/underscore/underscore-min',
    'bootstrap': '../bower_components/ehealth-bootstrap/js/bootstrap.min',
    'viewport-fix': '../bower_components/ehealth-bootstrap/js/thirdparty/ie10-viewport-bug-workaround',
    'patient': 'patient',
    'validate-patient-form': 'validate-patient-form',
    'layout': 'layout',
    'alerts': 'alerts',
    'initialize-ajax': 'initialize-ajax',
    'load-patient-form': 'load-patient-form',
    'search': 'search',
    'submit-patient-form': 'submit-patient-form'
  } ,
  shim: {
    'jquery.validate': {
      deps: ['jquery']
    },
    'bootstrap': {
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

