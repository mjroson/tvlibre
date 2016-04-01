(function () {
    'use strict';

    angular
        .module('tvApp.config')
        .config(config);

    config.$inject = ['$locationProvider', '$httpProvider', '$resourceProvider'];

    /**
     * @name config
     * @desc Enable HTML5 routing
     */
    function config($locationProvider, $httpProvider, $resourceProvider) {
        // CSRF Support
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $resourceProvider.defaults.stripTrailingSlashes = false;
        // This only works in angular 3!
        // It makes dealing with Django slashes at the end of everything easier.
        //$resourceProvider.defaults.stripTrailingSlashes = false;

        $locationProvider.html5Mode(true).hashPrefix('!');

    }
})();
