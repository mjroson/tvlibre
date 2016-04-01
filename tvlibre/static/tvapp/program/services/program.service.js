/**
 * Program
 * @namespace tvApp.program.services
 */
(function () {
    'use strict';

    angular
        .module('tvApp.program.services')
        .factory('Program', Program);

    Program.$inject = ['$resource'];

    /**
     * @namespace Program
     * @returns {Factory}
     */
    function Program($resource) {

        return $resource("/api/v1/programs/:id",{id: '@id'}, {
            query: {method: 'get', isArray: false }
        });
    }
})();