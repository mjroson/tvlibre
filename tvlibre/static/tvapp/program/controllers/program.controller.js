/**
 * ProgramCtrl
 * @namespace tvApp.program.controllers
 */
(function () {
    'use strict';

    angular
        .module('tvApp.program.controllers')
        .controller('ProgramCtrl', ProgramCtrl);

    ProgramCtrl.$inject = ['Program', 'Episode', 'Favorite', 'AlertNotification', 'stBlurredDialog', '$location'];

    /**
     * @namespace ProgramCtrl
     */
    function ProgramCtrl(Program, Episode, Favorite, AlertNotification, stBlurredDialog, $location) {
        var vm = this;

        vm.search_q = "";
        vm.programs = [];
        vm.program = {};
        vm.episodes = [];

        vm.query = {};
        var next = null;
        var previous = null;
        vm.query.page = 1;

        init();
        function init(){
            Program.query(function(data) {
                vm.programs = data.results;
                next = data.next;
                previous = data.previous;
                var hash = $location.hash();
                if(vm.programs.length > 0){
                    if(hash){
                        for(var i=0; i < vm.programs.length; i++){
                            if (vm.programs[i].slug == hash){
                                vm.selectProgram(vm.programs[i]);
                                break;
                            }
                        }
                    }else{
                        vm.selectProgram(vm.programs[0]);
                        $location.hash(vm.programs[0].slug);
                    }
                }
            });
        }


        function get_programs(){
            Program.query(vm.query, function(data) {
                vm.programs = data.results;
                next = data.next;
                previous = data.previous;
            });
        }

        vm.selectProgram = function(program){
            vm.program.selected = false;
            vm.program = program;
            program.selected = true;

            Episode.query({ program__slug: program.slug }, function(data){
                vm.episodes = data.results;

                var query = angular.copy($location.search());
                if(query['watch']){
                    for(var i=0; i < vm.episodes.length; i++){
                        if (vm.episodes[i].slug == query['watch']){
                            vm.openEpisode(vm.episodes[i]);
                            break;
                        }
                    }
                }
            });
        };


        vm.toggleFavorite = function(program){
            Favorite.toggle_favorites({obj: {'id': program.id}}).then(function(data){
                console.log(data);
                AlertNotification.success("El programa se cambio favoritos con exito");
                program.is_favorite = !program.is_favorite;
            }, function(error){
               AlertNotification.error("Error al tratar de cambiar a favoritos");
            });
        };

        vm.openEpisode = function(episode){
            $location.search({ watch: episode.slug});
            stBlurredDialog.open('/static/tvapp/program/templates/dialog_episode.html', episode);
        };

        vm.loadMore = function(){
            if(next){
                vm.query.page ++;
                get_programs();
            }
        };

    }
})();