/**
 * FavoriteCtrl
 * @namespace tvApp.favorite.controllers
 */
(function () {
    'use strict';

    angular
        .module('tvApp.favorite.controllers')
        .controller('FavoriteCtrl', FavoriteCtrl);

    FavoriteCtrl.$inject = ['Favorite', 'AlertNotification'];

    /**
     * @namespace FavoriteCtrl
     */
    function FavoriteCtrl(Favorite, AlertNotification) {
        var vm = this;


        vm.favorites = [];
        vm.request = false;
        vm.search_q = '';
        vm.remove_favorite = remove_favorite;

        getFavorites();

        function getFavorites(){
            vm.promiseRequest = Favorite.get_favorites().then(getFavoriteSuccess, getFavoriteError);

            function getFavoriteSuccess(data){
                console.log(data);
                vm.favorites = data.data;
                vm.request = true;
            }

            function getFavoriteError(data){
                vm.request = true;
                AlertNotification.error("Error al intentar traer tus favoritos. Vuelve a intentarlo mas tarde");
            }

        }


        function remove_favorite(favorite){

            vm.promiseRequest = Favorite.toggle_favorites(favorite).then(removeFavoriteSuccess, removeFavoriteError);

            function removeFavoriteSuccess(data){
                AlertNotification.info("El programa " + favorite.obj.title + " fue quitado de tus favoritos");
                vm.favorites.splice(vm.favorites.indexOf(favorite),1);
            }

            function removeFavoriteError(data){
                AlertNotification.error("Error al intentar quitar el favorito de tu lista, intenta mas tarde");
            }

        }


    }
})();