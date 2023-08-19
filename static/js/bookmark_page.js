let basket = {
  //화면 업데이트
  updateUI: function () {
      document.querySelector('#sum_p_price').textContent = '합계금액: ' + this.totalPrice.formatNumber() + '원';
  },
  //삭제버튼
  delItem: function () {
      event.target.parentElement.parentElement.parentElement.remove();
      this.updateUI();
  }
}

// 숫자 3자리 콤마찍기
Number.prototype.formatNumber = function(){
  if(this==0) return 0;
  let regex = /(^[+-]?\d+)(\d{3})/;
  let nstr = (this + '');
  while (regex.test(nstr)) nstr = nstr.replace(regex, '$1' + ',' + '$2');
  return nstr;
};