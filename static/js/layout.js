define(['jquery'], function(jquery) {

  function adjustSidebar () {
    jquery('.sidebar').height(jquery(document).height());
  }

  return {
    adjustSidebar: adjustSidebar
  };
});
