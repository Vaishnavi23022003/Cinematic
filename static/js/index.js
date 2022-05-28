$(document).on("click", 'a[href^="#"]', function (event) {
  event.preventDefault();

  $("html, body").animate(
    {
      scrollTop: $($.attr(this, "href")).offset().top,
    },
    500
  );
});

var play_event;
var player;
function onYouTubePlayerAPIReady() {
  player = new YT.Player("ytplayer", {
    videoId: youtube_id,
    events: {
      onReady: onPlayerReady,
      onStateChange: onPlayerStateChange,
    },
  });
}

// autoplay video
function onPlayerReady(event) {
  play_event = event.target;
}

// when video ends
function onPlayerStateChange(event) {
  if (event.data === 0) {
    $("#ytplayer").css("display", "none");
  }
}
$(":radio").change(function () {
  console.log("New star rating: " + this.value);
  $(".rating__old_rate").css("z-index", "0");
  $.ajax({
    type: "POST",
    url: post_url,
    data: {
      stars: this.value,
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
    },
  });
});

$(".movie-header__trailer").click(function () {
  console.log("ya ya working");
  console.log($("#ytplayer").attr("id"));
  $("#ytplayer").css("display", "block");
  play_event.playVideo();
});

var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
};
