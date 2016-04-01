

/**
 * EpisodeDialogCtrl
 * @namespace tvApp.program.controllers
 */
(function () {
    'use strict';

    angular
        .module('tvApp.program.controllers')
        .controller('EpisodeDialogCtrl', EpisodeDialogCtrl);

    EpisodeDialogCtrl.$inject = ['stBlurredDialog', '$sce', '$location', 'Comment'];

    /**
     * @namespace EpisodeDialogCtrl
     */
    function EpisodeDialogCtrl(stBlurredDialog, $sce, $location, Comment) {
        var vm = this;

        vm.episode = stBlurredDialog.getDialogData();
        vm.url = '';
        vm.host = '';
        vm.comments = [];
        vm.new_comment = {};
        init();
        function init(){
            vm.host = $location.host();
            vm.url = 'http://' + vm.host + '/';
            vm.url += '?watch=' + vm.episode.slug + '#' + vm.episode.parent_slug;
            vm.new_comment.object_pk = vm.episode.id;

            // Trae los ultimos comentarios
            Comment.last({'object_pk': vm.episode.id }, function(data){
                vm.comments = data.results;
            });
        }

        /**
         * Envia un comentario
         */
        vm.submitComment = function(){
            var comment = new Comment(vm.new_comment);
            comment.$save(function(data){
                if(vm.reply_comment){
                    console.log(vm.reply_comment.children);
                    vm.reply_comment.children += 1;
                    if(vm.reply_comment.comments){
                        vm.reply_comment.comments.splice(0, 0, data);
                    }
                }else{
                    vm.comments.splice(0, 0, data);
                }

                vm.new_comment = {'object_pk':vm.episode.id};
                delete(vm.reply_comment);
            });
        };

        vm.trustSrc = function(src) {
            return $sce.trustAsResourceUrl(src);
        };

        vm.safeHtml = function(html){
            return $sce.trustAsHtml(html);
        };

        vm.getChildren = function(comment){
            Comment.query({'parent_id': comment.id, 'id_not': comment.id}, function(data){
                comment.comments = data.results;
            })
        };
        vm.reply_comment = null;
        vm.reply = function(comment){
            vm.reply_comment = comment;
            vm.new_comment['parent_id'] = comment.id;
        };
    }
})();