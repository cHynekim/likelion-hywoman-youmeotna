function formCheck()
{
    let name = document.getElementById('name');
    let birth = document.getElementById('birth');
    let phoneNum = document.getElementById('phoneNum');
    let id = document.getElementById('id');
    let password = document.getElementById('password');

    if(name.value == ""){
        alert("이름을 입력해주세요");
        name.focus(); //커서가 깜빡이도록
        return false; // 아무것도 반환하지 않도록
    };

    if(birth.value == ""){
        alert("생년월일을 입력해주세요");
        name.focus(); //커서가 깜빡이도록
        return false; 
    };

    if(phoneNum.value == ""){
        alert("전화번호를 입력해주세요");
        name.focus(); //커서가 깜빡이도록
        return false; 
    };
    // let phonecheck = /^[0-9]{2,5}/g; //숫자만 입력하는 정규식 정의

    // if (!phonecheck.test(phoneNum.value)){
    //     alert("전화번호는 010부터 숫자만 입력해주세요")
    // };


    if(id.value == ""){
        alert("별명을 입력해주세요");
        name.focus(); //커서가 깜빡이도록
        return false; 
    };

    if(password.value == ""){
        alert("비밀번호를 입력해주세요");
        name.focus(); //커서가 깜빡이도록
        return false; 
    };

    let pswcheck = /^[0-9]+/g; //숫자만 입력하는 정규식 정의

    // if (!pswcheck.test(password.value)){
    //     alert("비밀번호는 숫자 6자리로 입력해주세요")
    // };

    //입력값 전송
    document.formcheck.submit();

}    

//휴대폰 번호 자릿수 자동맞춤 & '-' 넣어주기
const autoHyphen = (target) => {
    target.value = target.value
      .replace(/[^0-9]/g, '')
     .replace(/^(\d{0,3})(\d{0,4})(\d{0,4})$/g, "$1-$2-$3").replace(/(\-{1,2})$/g, "");
   };

//별명 한글만 되도록
function checkReg(event) {
    const regExp = /[^ㄱ-ㅎ|가-힣]/g; // 한글만 허용
    const del = event.target;
    if (regExp.test(del.value)) {
      del.value = del.value.replace(regExp, '');
    }
};

//비밀번호 확인
function chkPW(){

    var pw = $("#password").val();
    var num = pw.search(/[0-9]/g);
   
    if(pw.length < 1 || pw.length > 6){
     alert("10자리 ~ 20자리 이내로 입력해주세요.");
     return false;
    }else if(pw.search(/\s/) != -1){
     alert("비밀번호는 공백 없이 입력해주세요.");
     return false;}
    else {
       console.log("통과");	 
    }
   
}