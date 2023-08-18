//휴대폰 번호 자릿수 자동맞춤 & '-' 넣어주기
const autoHyphen = (target) => {
    target.value = target.value
      .replace(/[^0-9]/g, '')
     .replace(/^(\d{0,3})(\d{0,4})(\d{0,4})$/g, "$1-$2-$3").replace(/(\-{1,2})$/g, "");
   };

//별명, 이름 한글만 되도록
//function checkReg(event) {
//    const regExp = /[^ㄱ-ㅎ|가-힣]/g; // 한글만 허용
//    const del = event.target;
//    if (regExp.test(del.value)) {
//      del.value = del.value.replace(regExp, '');
//    }
//};
//const numericInput = document.getElementById("password");
//
//numericInput.addEventListener("input", function(event) {
//    const inputValue = event.target.value;
//    const sanitizedValue = inputValue.replace(/\D/g, ""); // 숫자가 아닌 문자 제거
//    const maxLength = 6;
//    event.target.value = sanitizedValue.substring(0, maxLength); // 최대 길이 제한
//});


// 가입하기 눌렀을 때 공백 확인
document.querySelector('.agree').onclick = function(){

    let nameError = document.querySelector("#nameError");
    let birthError = document.querySelector("#birthError");
    let phoneNumError = document.querySelector("#phoneNumError");
    let idError = document.querySelector("#idError");


    let name = document.getElementById('name');
    let birth1 = document.getElementById('birth1');
    let birth2 = document.getElementById('birth2');
    let birth3 = document.getElementById('birth3');
    let phoneNum = document.getElementById('phoneNum');
    let id = document.getElementById('id');

    let check=false;

    if(name.value == ""){
        nameError.style.opacity = "1";
        check = false
    }
    else{
        nameError.style.opacity = "0";

    }

    if (birth1.value === "" || birth2.value === "" || birth3.value === "") {
        birthError.style.opacity = "1";
        check = false;
    } else {
        birthError.style.opacity = "0";
    }
    
    if(phoneNum.value == ""){
        phoneNumError.style.opacity = "1";
        check = false
    }
    else{
        phoneNumError.style.opacity = "0";

    }

    if(id.value == ""){
        idError.style.opacity = "1";
        check = false
    }
    else{
        idError.style.opacity = "0";

    }
    //비밀번호 같은지 확인
    let passwordError = document.querySelector("#passwordError");
    let passwordCheckError = document.querySelector("#passwordCheckError");
    
    let password = document.getElementById("password");
    let passwordCheck = document.getElementById("passwordCheck");

    if (password.value !== passwordCheck.value) {
        passwordError.style.opacity = 0;
        passwordCheckError.style.opacity = "1";
        check = false;
    } else if (password.value === "") {
        passwordError.style.opacity = 1;
        passwordCheckError.style.opacity = 0;
        check = false;
    } else if (passwordCheck.value === "") {
        passwordError.style.opacity = 0;
        passwordCheckError.style.opacity = 1;
        check = false;
    } else {
        passwordError.style.opacity = 0;
        passwordCheckError.style.opacity = 0;
        check = true;
    }
    

        // If all checks pass, you can proceed with further actions
    if (check) {
        // Do something here
    }
    
};