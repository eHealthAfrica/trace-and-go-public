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

  function populate(response, healthFacilityId, patientStatus) {
    var choices = _.sortBy(
      getHealthFacilityChoices(response),
      function(choice) { return choice.display_name; }
    );
    var hfSelect = jquery('#healthFacilitySelect');
    jquery.each(choices, function (i, item) {
      insertOption(hfSelect, item);
    });
    choices = _.sortBy(
      getStatusChoices(response),
      function(choice) { return choice.display_name; }
    );
    hfSelect.val(healthFacilityId);
    var statusSelect = jquery('#patientStatusSelect');
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
    var cancelButton = jquery('#cancelEdit');
    cancelButton.click(function() {
      location.href = '/patients';
    });
  }

  return {
    populate: populate
  };

});
