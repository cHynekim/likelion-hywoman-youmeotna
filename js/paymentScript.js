//버튼 클릭 시 다음으로 이동
let wdu = document.querySelector('.paymentList');
let list = document.querySelector('.paymentList ul');
let lists = document.querySelectorAll('.process');
let listsWidth = lists[1].offsetLeft - lists[0].offsetLeft;
let nextBtn = document.querySelector('.nextBtn');
let currentIdx = 0;
//브라우저 창 크기 변경 유무 확인 변수
let check = false;
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
    //끝에 도달하면 애니메이션 작동X
    if(num == 5){
        return;
    }
    lists[num-1].style.transform = 'scale(90%)';
    lists[num].style.transform = 'scale(90%)';
    setTimeout(function(){
        list.style.left = `${-num * listsWidth}px`;
    },300);
    setTimeout(function(){
        lists[num].style.transform = 'scale(100%)';
        //마지막 단계 도달 시 버튼 내용 변경
        if(lists[num] == lists[4]){
            nextBtn.innerText = '결제완료';
            nextBtn.style.backgroundColor = '#FEAF96';
            nextBtn.style.color = '#2A343D';
            let css = '.nextBtn:hover{background-color: #FEAF96; color: #2A343D;}';
            nextBtn.styleSheet.cssText = css;
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