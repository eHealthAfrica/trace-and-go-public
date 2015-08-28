define([
  'jquery'
], function(jquery) {

  function insertOption(parent, item) {
    parent.append(
      jquery('<option>', {
        value: item.value,
        text : item.display_name
      })
    );
  }

  function getHealthFacilityChoices(obj) {
    return obj.actions.POST.health_facility_id.choices;
  }

  function getStatusChoices(obj) {
    return obj.actions.POST.status.choices;
  }

  function getHealthFacilities() {
    return jquery.ajax({
      // TODO: deactivate pagination of response in a more elegant way.
      url: '/health-facilities/.json?limit=99999999',
      dataType: "json",
      type: "GET",
      success: function (data) {
        return data;
      }
    });
  }

  function getPatientOptions(d1, d2) {
    return jquery.ajax({
      url: "/patients/.json",
      dataType: "json",
      type: "OPTIONS",
      success: function (data) {
        return data;
      }
    });
  }

  function populateHealthFacilityList(healthFacilityId, deferred) {
    return getHealthFacilities().done(function(data) {
      var hfSelect = jquery('#healthFacilitySelect');
      var choices = data.results;
      choices = _.sortBy(
        choices,
        function(choice) { return choice.name; }
      );
      jquery.each(choices, function (i, item) {
        hfSelect.append(
          jquery('<option>', {
            value: item.pk,
            text : item.name
          })
        );
      });
      hfSelect.val(healthFacilityId);
      deferred.resolve();
    });
  }

  function populateStatusList(patientStatus, deferred) {
    return getPatientOptions().done(function(data) {
      var statusSelect = jquery('#patientStatusSelect');
      var choices = getStatusChoices(data);

      jquery.each(choices, function(i, item) {
        var label = jquery('<div/>', {
          class: "row"
        });
        label.append(jquery('<input/>', {
          type: "radio",
          width: 18,
          height: 14,
          name: "status",
          value: item.value
        }));
        label.append(jquery('<span/>', {
          text: item.display_name
        }));
        statusSelect.append(label);
      });
      jquery('input[name=status]').val([patientStatus]);
      deferred.resolve();
    });
  }

  function load(healthFacilityId, patientStatus) {

    var healthFacilityListDeferred = jquery.Deferred();
    var statusListDeferred = jquery.Deferred();
    populateHealthFacilityList(healthFacilityId, healthFacilityListDeferred);
    populateStatusList(patientStatus, statusListDeferred);

    var cancelButton = jquery('#cancelEdit');
    cancelButton.click(function() {
      location.href = '/patients';
    });

    return jquery.when(healthFacilityListDeferred, statusListDeferred);
  }

  return {
    load: load
  };

});
