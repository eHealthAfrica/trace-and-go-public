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
    var parentElem = jquery('#healthFacilitySelect');
    jquery.each(choices, function (i, item) {
      insertOption(parentElem, item);
    });
    choices = _.sortBy(
      getStatusChoices(response),
      function(choice) { return choice.display_name; }
    );
    parentElem.val(healthFacilityId);
    parentElem = jquery('#patientStatusSelect');
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
      parentElem.append(label);
    });
    jquery('input[name=status]').val([patientStatus]);
  }

  return {
    populate: populate
  };

});
