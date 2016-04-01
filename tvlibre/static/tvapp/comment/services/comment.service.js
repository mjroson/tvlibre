/**
 * Comment
 * @namespace tvApp.program.services
 */
(function () {
    'use strict';

    angular
        .module('tvApp.program.services')
        .factory('Comment', Comment);

    Comment.$inject = ['$resource'];

    /**
     * @namespace Comment
     * @returns {Factory}
     */
    function Comment($resource) {

        return $resource("/api/v1/comments/:id/", null,
            {
                last: {
                    method: 'GET',
                    isArray:false,
                    url: '/api/v1/comments/last/'
                }
            }
        );
    }
})();