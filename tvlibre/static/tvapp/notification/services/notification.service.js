/**
 * Notification
 * @namespace tvApp.notification.services
 */
(function () {
    'use strict';

    angular
        .module('tvApp.notification.services')
        .factory('Notification', Notification);

    Notification.$inject = ['$resource'];

    /**
     * @namespace Notification
     * @returns {Factory}
     */
    function Notification($resource) {
        return $resource("/api/v1/notifications/:id",{id: '@id'}, {
            query: {method: 'get', isArray: false }
        });

    }
})();