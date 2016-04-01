/**
 * LayoutCtrl
 * @namespace dashBoardApp.layout.controllers
 */
(function () {
    'use strict';

    angular
        .module('tvApp.layout.controllers')
        .controller('SidebarCtrl', SidebarCtrl);

    SidebarCtrl.$inject = ['Authentication'];

    /**
     * @namespace SidebarCtrl
     */
    function SidebarCtrl(Authentication) {
        var vm = this;

        vm.logout = logout;

        function logout(){
            Authentication.unauthenticate();
            window.location = '/users/logout/';
        }

        $rootScope.$on('$stateChangeStart', function (event, toState, toParams) {
            vm.data = toState.data;
        });
    }

})();
