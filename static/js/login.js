let start = document.querySelector('.logoBox');
let login = document.querySelector('#wrap');


setTimeout(function(){
    start.style.transition = '1s';
    start.style.width = '35%';
    start.style.height = '35%';
    start.style.maxWidth = '330px';
    start.style.minWidth = '280px';
    start.style.transform = 'translate(-50%, -140%)';
    login.style.opacity = '1';
}, 2000);