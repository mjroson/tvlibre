/**
 * Episode
 * @namespace tvApp.program.services
 */
(function () {
    'use strict';

    angular
        .module('tvApp.program.services')
        .factory('Episode', Episode);

    Episode.$inject = ['$resource'];

    /**
     * @namespace Episode
     * @returns {Factory}
     */
    function Episode($resource) {

        return $resource("/api/v1/episodes/:id",{id: '@id'}, {
            query: {method: 'get', isArray: false }
        });
    }
})();