document.addEventListener("DOMContentLoaded", function() {
  //드롭다운에 화살표 이미지랑 첫번째 요소 같이 보이도록
  var dropdownContent1 = document.getElementById("myDropdown1");
  var firstItem1 = dropdownContent1.querySelector("a:first-child");
  var dropbtn1 = document.querySelector(".dropbtn");
  var image1 = dropbtn1.querySelector("img");


  dropbtn1.innerHTML = ""; // Clear the existing content
  dropbtn1.appendChild(firstItem1.cloneNode(true));
  dropbtn1.appendChild(image1);

  var dropdownContent2 = document.getElementById("myDropdown2");
  var firstItem2 = dropdownContent2.querySelector("a:first-child");
  var dropbtn2 = document.getElementById("dropbtn2"); // Use the ID of the second dropbtn

  var image2 = dropbtn2.querySelector("img");
  dropbtn2.innerHTML = ""; // Clear the existing content
  dropbtn2.appendChild(firstItem2.cloneNode(true));
  dropbtn2.appendChild(image2);


});

/* 토글 보이도록*/
function myFunction(event) {
    event.preventDefault();
    document.getElementById("myDropdown1").classList.toggle("show");
}
function myFunction2(event) {
    event.preventDefault();
    document.getElementById("myDropdown2").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}