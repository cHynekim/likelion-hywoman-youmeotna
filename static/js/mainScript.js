// 말풍선 fadeIn/Out
let bubble = document.querySelector('.bubble');
setInterval(()=>{
    bubble.classList.toggle('hid');
}, 4000);

//loop Carousel
let slide = document.querySelector('.list'),
    lists = document.querySelectorAll('.list li'),
    listLen = lists.length,
    currentIdx = 0,
    listWidth = lists[1].offsetLeft - lists[0].offsetLeft,
    rightBtn = document.querySelector('.right'),
    leftBtn = document.querySelector('.left');
console.log(slide, lists, listLen, currentIdx, listWidth);

makeClone();
function makeClone(){
    for(let i = 0; i<listLen; i++){
        let cloneList = lists[i].cloneNode(true);
        cloneList.classList.add('clone');
        slide.append(cloneList);
    }
    for(let i = listLen - 1; i >= 0; i--){
        let cloneList = lists[i].cloneNode(true);
        cloneList.classList.add('clone');
        slide.prepend(cloneList);
    }
    ModifySlideWidth();
    settingCarousel();
    //배치 완료 후
    setTimeout(function(){
        slide.classList.add('animate');
    }, 1000);    //1초 뒤에 함수 내용 실행
}
function ModifySlideWidth(){
    let currentLists = document.querySelectorAll('.list li');
    let newlistLen = currentLists.length;

    let newWidth = `${listWidth * newlistLen}px`;
    slide.style.width = newWidth;
}
function settingCarousel(){
    let zero = listWidth * listLen;
    slide.style.transform = `translateX(-${zero}px)`;
}
//btn click시, 이동
leftBtn.onclick = function(){
    move(currentIdx - 1);
}
rightBtn.onclick = function(){
    move(currentIdx + 1);
}
function move(num){
    slide.style.left = `${-num * listWidth}px`;
    currentIdx = num;
    console.log(currentIdx, listLen);
    if(currentIdx == listLen || currentIdx == -(listLen)){
        setTimeout(function(){
            slide.classList.remove('animate');
            slide.style.left = '0px';
            currentIdx = 0;
        }, 500);
        setTimeout(function(){
            slide.classList.add('animate');
        }, 540);
    }
}

//hover시, interval 멈춤 & infinity Carousel
let trigger = undefined;
function infinityCarousel(){
    if(trigger == undefined){
        trigger = setInterval(function(){
            move(currentIdx + 1);
        }, 4000);
    }
}
infinityCarousel(); //auto

function stopCarousel(){
    clearInterval(trigger);
    console.log(trigger);
    trigger = undefined;
}
slide.addEventListener('mouseenter', function(){
    stopCarousel()
}); //mouseover 시, pause
slide.addEventListener('mouseleave', function(){
    infinityCarousel()
}); //mouseout 시, start