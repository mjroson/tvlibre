tinymce.init({
    selector: '.rich_text',
    theme: 'modern',
    plugins: [
        'advlist autolink lists link charmap print preview hr anchor pagebreak',
        'searchreplace wordcount visualblocks visualchars fullscreen',
        'insertdatetime nonbreaking save contextmenu directionality',
        'paste textcolor colorpicker textpattern'
    ],
    toolbar1: 'insertfile undo redo | styleselect | bold italic forecolor backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link',
    image_advtab: true,

    default_link_target: "_blank"
});
