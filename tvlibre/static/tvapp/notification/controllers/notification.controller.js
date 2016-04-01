/**
 * NotificationCtrl
 * @namespace tvApp.notification.controllers
 */
(function () {
    'use strict';

    angular
        .module('tvApp.notification.controllers')
        .controller('NotificationCtrl', NotificationCtrl);

    NotificationCtrl.$inject = ['Notification', 'AlertNotification'];

    /**
     * @namespace NotificationCtrl
     */
    function NotificationCtrl(Notification, AlertNotification) {
        var vm = this;

        vm.notifications = [];

        init();

        function init(){
            Notification.query(function(data){
                console.log("NOTIFICATIONS ");
                console.log(data);
               vm.notifications = data;
            }, function(error){
                AlertNotification.error("Error al intentar recuperar las notificaciones");
            });
        }





    }
})();