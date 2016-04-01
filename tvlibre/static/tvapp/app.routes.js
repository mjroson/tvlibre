(function () {
    'use strict';

    angular
        .module('tvApp.routes')
        .config(config);

    config.$inject = ['$stateProvider', '$urlRouterProvider', '$locationProvider'];

    /**
     * @name config
     * @desc Define valid application routes
     */
    function config($stateProvider, $urlRouterProvider, $locationProvider) {
        // Definiendo rutas para la app.
        $stateProvider

            .state('programs', {
                url: '/',
                templateUrl: '/static/tvapp/program/templates/list.html',
                controller: 'ProgramCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [{url: 'programs', name:'Programas'}],
                    title: "Todos los programas"
                }
            })
            .state('nosotros', {
                url: '/nosotros/',
                templateUrl: '/static/tvapp/util/templates/nosotros.html',
                data:{
                    breadcumbs: [{url: 'nosotros', name:'Nosotros'}],
                    title: "Sobre nosotros"
                }
            })
            .state('register', {
                url: '/registrarse/',
                templateUrl: '/static/tvapp/user/templates/register.html',
                data:{
                    breadcumbs: [{url: 'register', name:'Registracion'}],
                    title: "Registrate"
                }
            })
            .state('profile', {
                url: '/perfil/',
                templateUrl: '/static/tvapp/user/templates/profile.html',
                data:{
                    breadcumbs: [{url: 'profile', name:'Perfil'}],
                    title: "Perfil"
                }
            })
            .state('favorites', {
                url: '/favoritos/',
                controller: 'FavoriteCtrl',
                controllerAs: 'vm',
                templateUrl: '/static/tvapp/favorite/templates/list.html',
                data:{
                    breadcumbs: [{url: 'favorite', name:'Mis favoritos'}],
                    title: 'Mis Favoritos'
                }
            })
            .state('notifications', {
                url: '/notificaciones/',
                controller: 'NotificationCtrl',
                controllerAs: 'vm',
                templateUrl: '/static/tvapp/notification/templates/list.html'
            })
            .state('search', {
                url: '/buscar/',
                templateUrl: '/static/tvapp/program/templates/search.html',
                controller: 'SearchCtrl',
                controllerAs: 'vm',
                data:{
                    breadcumbs: [{url: 'search', name:'Buscar'}],
                    title: "Buscar en todos los episodios"
                }
            })

        ;


        $urlRouterProvider.otherwise('/');

        $locationProvider.html5Mode(true);
    }
})();
