/**
 * whenScrollEnds
 * @namespace tvApp.util.directives
 */
(function ($, _) {
    'use strict';

    angular
        .module('tvApp.util.directives')
        .directive('whenScrollEnds', ScrollEnd);


    ScrollEnd.$inject = [];

    /**
     * @namespace ScrollEnd
     */
    function ScrollEnd() {
        return {
            restrict: "A",
            link: function(scope, element, attrs) {
                var visibleHeight = element.height();
                var threshold = 100;
                var flag_change = false;
                element.scroll(function() {
                    var scrollableHeight = element.prop('scrollHeight');
                    var hiddenContentHeight = scrollableHeight - visibleHeight;

                    if (hiddenContentHeight - element.scrollTop() <= threshold) {
                        // Scroll is almost at the bottom. Loading more rows
                        if(flag_change == false){
                            scope.$apply(attrs.whenScrollEnds);
                            flag_change = true;
                        }

                    }else{
                        flag_change = false;
                    }
                });
            }
        };


    }
})();