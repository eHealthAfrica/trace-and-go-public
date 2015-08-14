define(['jquery'], function(jquery) {

  function adjustSidebar () {
    var htmlHeight = jquery('html').height();
    jquery('.sidebar').height(htmlHeight);
  }

  return {
    adjustSidebar: adjustSidebar
  };
});
