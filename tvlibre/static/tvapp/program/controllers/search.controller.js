/**
 * SearchCtrl
 * @namespace tvApp.program.controllers
 */
(function () {
    'use strict';

    angular
        .module('tvApp.program.controllers')
        .controller('SearchCtrl', SearchCtrl);

    SearchCtrl.$inject = ['Episode', 'stBlurredDialog', 'Program', '$location', 'Category'];

    /**
     * @namespace SearchCtrl
     */
    function SearchCtrl(Episode, stBlurredDialog, Program, $location, Category) {
        var vm = this;

        vm.search_q = "";
        vm.episodes = [];
        vm.programs = [];
        init();

        vm.query = {};
        vm.query = $location.search();
        var hash = $location.hash();

        vm.categories = [];

        var next = null;
        var previous = null;
        vm.query.page = 1;


        function init(){

            vm.episodes = Episode.query(function(data){
                vm.episodes = data.results;
                next = data.next;
                previous = data.previous;
            });
            // PORQUE HAGO ESTO????
            if(vm.query){
                vm.programs = Program.query(vm.query, function(data){
                    vm.programs = data.results;
                });
            }else{
                vm.programs = Program.query(function(data){
                    vm.programs = data.results;
                });
            }

            Category.query(function(data){
                vm.categories = data.results;
            });
        }

        vm.search = function(acumulate){
            console.log(vm.episodes);
            Episode.query(vm.query, function(data){
                if(acumulate){
                    vm.episodes = vm.episodes.concat(data.results);
                    console.log(vm.episodes);
                }else{
                    vm.episodes = data.results;
                }
                next = data.next;
                previous = data.previous;
            });
        };

        vm.openEpisode = function(episode){
            stBlurredDialog.open('/static/tvapp/program/templates/dialog_episode.html', episode);
        };

        vm.loadMore = function(){
            if(next){
                vm.query.page ++;
                vm.search(true)
            }
        };
    }
})();