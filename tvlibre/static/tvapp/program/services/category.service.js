/**
 * Category
 * @namespace tvApp.program.services
 */
(function () {
    'use strict';

    angular
        .module('tvApp.program.services')
        .factory('Category', Category);

    Category.$inject = ['$resource'];

    /**
     * @namespace Category
     * @returns {Factory}
     */
    function Category($resource) {

        return $resource("/api/v1/categories/:id",{id: '@id'}, {
            query: {method: 'get', isArray: false }
        });
    }
})();