define([
  'jquery'
], function(jquery) {

  function getOptions() {
    return jquery.ajax({
      url: "/patients/.json",
      dataType: "json",
      type: "OPTIONS",
      success: function (data) {
        return data;
      }
    });
  }

  function getStatusChoices(obj) {
    return obj.actions.POST.status.choices;
  }

  function initSearchForm () {
    var searchForm = jquery('form[role=search]');
    var filterByStatusSelect = jquery('#filterByStatus');

    getOptions().done(function(data) {
      var choices = getStatusChoices(data);
      jquery.each(choices, function(i, item) {
        var option = jquery('<option/>', {
          value: item.value,
          text: item.display_name
        });
        filterByStatusSelect.append(option);
      });
    });

    searchForm.submit(function(e) {
      e.preventDefault();
      var searchString = jquery('#searchPatientList').val();
      var filterString = jquery('#filterByStatus').val();
      var queryStrings = [];
      if (searchString) {
        var strings = searchString.split(' ');
        strings.map(function(s) {
          if (s) {
            queryStrings.push("contains=" + s);
          }
        });
      };
      if (filterString) { queryStrings.push("status=" + filterString); };
      if (queryStrings) {
        var queryString = "?" + queryStrings.join("&");
        location.href = location.pathname + queryString;
      }
    });
  }

  return {
    initSearchForm: initSearchForm
  };

});
