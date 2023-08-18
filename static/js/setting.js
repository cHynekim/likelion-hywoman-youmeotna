// 닉네임 불러오는 js

// 이벤트 리스너를 추가하여 문서가 완전히 로드될 때 실행될 함수를 등록합니다.
document.addEventListener("DOMContentLoaded", function() {
  // 닉네임 출력을 위한 요소를 선택합니다.
  var nicknameOutput = document.getElementById("nicknameOutput");

  // 닉네임 데이터를 설정합니다. 이 부분은 서버에서 데이터를 가져오거나 다른 방법으로 데이터를 동적으로 가져와야 합니다.
  var nicknameData = "블랙사파이어포도";

  // 선택한 요소에 닉네임 데이터를 적용합니다.
  nicknameOutput.textContent = nicknameData;
});


// 생일을 불러오는 js

document.addEventListener("DOMContentLoaded", function() {
  var birthdayOutput = document.getElementById("birthdayOutput");

  // 서버에 요청을 보내어 사용자 데이터를 가져옵니다.
  fetch("서버의_API_또는_엔드포인트_URL")
    .then(response => response.json())
    .then(data => {
      // 서버로부터 받아온 데이터 중 생일을 선택합니다.
      var birthdayData = data.birthday;

      // 선택한 요소에 생일 데이터를 적용합니다.
      birthdayOutput.textContent = birthdayData;
    })
    .catch(error => {
      console.error("데이터 가져오기 오류:", error);
    });
});


// 리뷰목록을 불러오는 js

document.addEventListener("DOMContentLoaded", function() {
  var comment1Text = document.querySelector(".comment1Text");
  var comment1Date = document.querySelector(".comment1Date");
  var comment2Text = document.querySelector(".comment2Text");
  var comment2Date = document.querySelector(".comment2Date");

  // 서버에 요청을 보내어 리뷰 목록 데이터를 가져옵니다.
  fetch("서버의_API_또는_엔드포인트_URL")
    .then(response => response.json())
    .then(data => {
      // 서버로부터 받아온 데이터 중 리뷰 목록을 선택합니다.
      var reviewList = data.reviews;

      // 리뷰 목록 데이터를 각각의 요소에 적용합니다.
      comment1Text.textContent = reviewList[0].text;
      comment1Date.textContent = " - " + reviewList[0].date;
      comment2Text.textContent = reviewList[1].text;
      comment2Date.textContent = " - " + reviewList[1].date;
    })
    .catch(error => {
      console.error("데이터 가져오기 오류:", error);
    });
});