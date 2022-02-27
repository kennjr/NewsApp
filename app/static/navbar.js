$(document).ready(() => {
    $(function() {
          $('#btn_top_headlines').on('click', function(e) {
            e.preventDefault()
            $('#btn_everything').removeClass("img_btn_selected");
            $('#btn_top_headlines').addClass("img_btn_selected");
            return false;
          });

          $('#btn_everything').on('click', function(e) {
            e.preventDefault()
            $('#btn_top_headlines').removeClass("img_btn_selected");
            $('#btn_everything').addClass("img_btn_selected");
            return false;
          });
    });
})