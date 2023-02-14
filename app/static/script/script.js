function showLoader() {
    var form = document.querySelector('.testbox form');
    var btnBlock = document.querySelector('.btn-block');
  
    form.style.display = 'none';
    btnBlock.innerHTML = '<div class="loader"></div>';
  }
  
//document.querySelector('.btn-block button').addEventListener('click', showLoader);

document.getElementById("request-button").addEventListener("click", function() {
    document.getElementById("loading-screen").style.display = "block";
  })