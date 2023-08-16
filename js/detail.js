//탭 메뉴 넘어가기
const tabItem = document.querySelectorAll('.tab_item')
const tabInner = document.querySelectorAll('.tab_inner')

tabItem.forEach((tab, idx)=> {
    tab.addEventListener('click', function(){
        tabInner.forEach((inner)=> {
            inner.classList.remove('active')
        })

        tabItem.forEach((item)=> {
            item.classList.remove('active')
        })

        tabItem[idx].classList.add('active')
        tabInner[idx].classList.add('active')
    })
})
//수량변경
function count(type){
    //결과 표시할 요소
    const result = document.getElementById('result');
    //현재 화면에 표시된 값
    let number = result.innerText;

    if(type === 'minus'){
        if(parseInt(number -1) < 0 || parseInt(number) >99){
            alert('하어');
            return; //확인누르면 0으로
        }
        number = parseInt(number) - 1;
    }else if(type ==='plus'){
        number = parseInt(number) + 1;
    }
    result.innerText = number;
}

document.getElementById('star').onclick = function(){
    this.style.backgroundColor = 'rgb(253, 255, 126)';
}