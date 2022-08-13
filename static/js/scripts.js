window.addEventListener('DOMContentLoaded', (event) => {
  chooseImg();
})


function loading() {
  $("#loading").show();
  $("#content").hide();
  $("#footer").hide();
}

function chooseImg() {
  var myImg = new Array("/static/img/loading-hamster.gif", "/static/img/loading-cat-01.gif")
  var randomNum = Math.floor(Math.random() * myImg.length);
  document.getElementById("loading-img").src = myImg[randomNum];
}