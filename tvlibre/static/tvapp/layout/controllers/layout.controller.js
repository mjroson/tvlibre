/**
 * LayoutCtrl
 * @namespace tvApp.layout.controllers
 */
(function () {
    'use strict';

    angular
        .module('tvApp.layout.controllers')
        .controller('LayoutCtrl', LayoutCtrl);

    LayoutCtrl.$inject = ['Authentication', 'Notification', 'AlertNotification'];

    /**
     * @namespace LayoutCtrl
     */
    function LayoutCtrl(Authentication, Notification, AlertNotification) {
        var vm = this;

        vm.auth = false;
        vm.notifications = [];

        init();

        function init(){
            if(Authentication.is_authenticated()){
                vm.auth = true;
                Notification.query(function(data){
                    vm.notifications = data.results;
                }, function(error){
                    AlertNotification.error("Error al intentar traer las notificaciones");
                });
            }

        }
        //$rootScope.$on('$stateChangeStart', function (event, toState, toParams) {
        //    vm.data = toState.data;
        //});

    }

})();
