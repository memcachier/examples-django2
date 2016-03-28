$(function() {
  $("input[data-submit-item]").live("click", function(e) {
    $.ajax({
      type: "POST",
      url: "/add",
      data: {
        "text": $("#item").val(),
        "csrfmiddlewaretoken": $('input[name~="csrfmiddlewaretoken"]').val()
      },
      success: function(data) {
        $("<li/>", { class: 'lead text-info', html: data }).
          appendTo($("#item-list"));
        $("#item").val("");
      }
    });
  });
});
