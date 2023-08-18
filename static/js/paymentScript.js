//버튼 클릭 시 다음으로 이동
let wdu = document.querySelector('.paymentList'),
    list = document.querySelector('.paymentList ul'),
    lists = document.querySelectorAll('.process'),
    listsWidth = lists[1].offsetLeft - lists[0].offsetLeft,
    nextBtn = document.querySelector('.nextBtn'),
    currentIdx = 0;
//브라우저 창 크기 변경 유무 확인 변수
let check = false,
    isChecked = document.querySelector('.payAgree label input').checked;
//진행바
let circles = document.querySelectorAll(".circle"),
    progressBar = document.querySelector(".indicator"),
    button = document.getElementById("next");

//클릭 시, 브라우저 창 변경 유무 확인 후 페이지 이동
nextBtn.onclick = function(){
    if(check == false){
        next(currentIdx + 1);
    }
    else{   //브라우저 창 이동했을 시, 너비값 재할당
        list.style.transition = '0.8s';
        listsWidth = lists[1].offsetLeft - lists[0].offsetLeft;
        next(currentIdx + 1);
    }
}
//이동 애니메이션
function next(num){
    //동의 유무 확인, 동의 체크 안 할 시 페이지 이동 없음
    if(num == 4){
        isChecked = document.querySelector('.payAgree label input').checked;
        if(isChecked == false){
            alert('이용약관에 동의해야 결제 진행이 가능합니다.');
            return;
        }
        else{
            nextBtn.style.backgroundColor = 'ffcdc4';
        }
    }
    //끝에 도달하면 애니메이션 작동X
    if(num == 5){
        return;
    }
    lists[num-1].style.transform = 'scale(90%)';
    lists[num].style.transform = 'scale(90%)';
    setTimeout(function(){
        list.style.left = `${-num * listsWidth}px`;
        //진행바 애니메이션
        circles[num].classList.add('active');
        progressBar.style.width = `${((num) / (circles.length -1 )) * 100}%`;
    },300);
    setTimeout(function(){
        lists[num].style.transform = 'scale(100%)';
        //마지막 단계 도달 시 버튼 내용 변경
        if(lists[num] == lists[4]){
            nextBtn.style.display = 'none';
        }
    },1000);
    currentIdx = num;
}
//브라우저 창 변경 시, 변경되는 요소들의 크기에 맞추어 현재 단계의 화면이 고정되게끔 ul 이동
window.onresize = function(){
    let newlist = document.querySelector('.paymentList ul');
    let newlists = document.querySelectorAll('.process');
    let newlistsWidth = newlists[1].offsetLeft - newlists[0].offsetLeft;
    newlist.style.transition = 'none';
    newlist.style.left = `${-currentIdx * newlistsWidth}px`;
    check = true;
}
//이전 진행 단계로 클릭 시 이동
for(let i =0; i<circles.length; i++){
    circles[i].onclick = function(){
        if(circles[i].classList.contains('active') == true){
            list.style.left = `${-i * listsWidth}px`;
        }
    }
}
// 주문목록 드롭다운
function myFunction(event) {
    event.preventDefault();
    document.getElementById("myDropdown1").classList.toggle("show");
}
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn2')) {
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
//총 가격
let sumEl = document.querySelector('.paySum');
let productPrice = document.querySelectorAll('.product p:nth-of-type(3)'),
    productAmount = document.querySelectorAll('.product p:nth-of-type(2)'),
    product = document.querySelectorAll('.product'),
    paySum = 0;
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
for(let i = 0; i<productPrice.length; i++){
    let price = productPrice[i].innerText,
        intPrice = '';
    for(let j = 0; j<price.length; j++){
        if(price[j] == '원'){
            intPrice = parseInt(intPrice);
            break;
        }
        if(price[j] == ','){
            continue;
        }
        intPrice = intPrice.concat(price[j]);
    }
    paySum += intPrice * parseInt(productAmount[i].innerText);
}
sumEl.innerText = `${numberWithCommas(paySum)} 원`;
//결제 API
var IMP = window.IMP; // 생략 가능
    IMP.init("imp85415064"); // 예: imp00000000

//결제건에 대한 정보 변수 설정
let productName = document.querySelector('.dropbtn2').innerText;
let address = document.querySelectorAll('.second p'),
    allAddress = address[0].innerText+' '+address[1].innerText;
let succeed = true;
document.querySelector('.inicis_pay').onclick = function requestPay() {
    // IMP.request_pay(param, callback) 결제창 호출
    IMP.request_pay({ // param
        pg: "html5_inicis",
        pay_method: "card",
        merchant_uid: "ORD20180131-0000013",
        name: `${productName}`,
        amount: 100,
        buyer_email: "liaco819@naver.com",
        buyer_name: "광장동물주먹",
        buyer_tel: "010-9265-7224",
        buyer_addr: `${allAddress}`,
        buyer_postcode: "01181"
    }, function (rsp) { // callback
        if (rsp.success) {
            alert('정상적으로 결제되었습니다');
            document.querySelector('#success-modal').classList.remove('hidden');
        } else {
            succeed = false;
            var msg = '결제에 실패하였습니다. ';
            msg += 'Error : ' + rsp.error_msg;
            alert(msg);
        }
    });
  }
$(".kakao_pay").click(function(){
    IMP.request_pay({ // param
        pg: "kakaopay",
        pay_method: "card",
        merchant_uid: "ORD20180131-0000011",
        name: `${productName}`,
        amount: 100,
        buyer_email: "liaco819@naver.com",
        buyer_name: "광장동물주먹",
        buyer_tel: "010-9265-7224",
        buyer_addr: `${allAddress}`,
        buyer_postcode: "01181"
    }, function (rsp) { // callback
        if (rsp.success) {
            alert('정상적으로 결제되었습니다');
            document.querySelector('#success-modal').classList.remove('hidden');
        }
        else {
            succeed = false;
            var msg = '결제에 실패하였습니다. ';
            msg += 'Error : ' + rsp.error_msg;
            alert(msg);
        }
    })
});

//loop Carousel
let slide = document.querySelector('.list'),
    tags = document.querySelectorAll('.list li'),
    tagLen = tags.length,
    idx = 0,
    tagHeight = 40;

makeClone();
function makeClone(){
    for(let i = 0; i<tagLen; i++){
        let clonetag = tags[i].cloneNode(true);
        clonetag.classList.add('clone');
        slide.append(clonetag);
    }
    for(let i = tagLen - 1; i >= 0; i--){
        let clonetag = tags[i].cloneNode(true);
        clonetag.classList.add('clone');
        slide.prepend(clonetag);
    }
    ModifySlideWidth();
    settingCarousel();
    //배치 완료 후
    setTimeout(function(){
        slide.classList.add('animate');
    }, 500);    //1초 뒤에 함수 내용 실행
}
function ModifySlideWidth(){
    let currentTags = document.querySelectorAll('.list li');
    let newtagLen = currentTags.length;

    let newHeight = `${tagHeight * newtagLen}px`;
    slide.style.height = newHeight;
}
function settingCarousel(){
    let zero = tagHeight * tagLen;
    slide.style.transform = `translateY(-${zero}px)`;
}
function move(num){
    slide.style.top = `${-num * tagHeight}px`;
    idx = num;
    if(idx == tagLen || idx == -(tagLen)){
        setTimeout(function(){
            slide.classList.remove('animate');
            slide.style.top = '0px';
            idx = 0;
        }, 2000);
        setTimeout(function(){
            slide.classList.add('animate');
        }, 2030);
    }
}

//infinity Carousel
let trigger = undefined;
function infinityCarousel(){
    if(trigger == undefined){
        trigger = setInterval(function(){
            move(idx + 1);
        }, 2000);
    }
}
infinityCarousel(); //auto
document.querySelector('#success-modal button').onclick = function(){
    this.parentElement.parentElement.classList.add('hidden');
}