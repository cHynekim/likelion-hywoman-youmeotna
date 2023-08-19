from django import forms

class AddCartForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    # 상품 상세 페이지, 장바구니에서 수량 변경 시 동작 방식이 다르도록 설정
    # 상세 페이지에서 수량을 선택하고 추가할 때는 현재 장바구니 수량에 더해지는 방식으로 is_update=False
    # 장바구니에서 수량을 변경할 때는 값을 그대로 현재 수량에 반영해 바로 업데이트 되는 방식으로 is_update=True
