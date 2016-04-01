(function () {
    'use strict';

    angular.module('tvApp', [
            // Third lib
            'ui.router',
            'cgBusy',
            '720kb.socialshare',
            'ngResource',
            'ngSanitize',
            'tvApp.config',
            'tvApp.routes',
            'stBlurredDialog',
            // My lib
            'authentication',
            'tvApp.notification',
            'tvApp.layout',
            'tvApp.util',
            'tvApp.favorite',
            'tvApp.program'
        ])
        // Configurando spinner
        .value('cgBusyDefaults',{
            message:'Procesando solicitud...',
            backdrop: false,
            templateUrl: '/static/templates-utils/spinner.html',
            delay: 100,
            minDuration: 500,
            wrapperClass: 'cg-busy cg-busy-backdrop'
        });

    angular
        .module('tvApp.routes', ['ui.router']);

    angular
        .module('tvApp.config', []);

    angular
        .module('tvApp')
        .run(function(){

        });

})();