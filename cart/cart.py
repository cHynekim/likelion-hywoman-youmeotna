from decimal import Decimal

from django.conf import settings
from shop.models import Product

# 카트 클래스
class Cart(object):
    # 카트 생성자, 카트 정보
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)

        if not cart: # 만약 카트 정보가 없다면
            cart = self.session[settings.CART_ID] = {} # 새로운 딕셔너리를 생성해 카트에 저장한다. 즉, 빈 마트 정보를 생성한다.
        self.cart = cart

    # 총 개수
    def __len__(self):
        # 장바구니에 있는 상품의 수량을 전부 더한 결과 리턴
        return sum(item['quantity'] for item in self.cart.values())

    # for문을 위한 함수
    def __iter__(self):
        # product_ids는 장바구니에 있는 상품의 정보를 가져오기 위함
        product_ids = self.cart.keys() # 상품 번호 목록을 가져와 product_ids에 저장
        products = Product.objects.filter(id__in=product_ids) # product_ids에 해당하는 상품만 상품 데이터베이스에서 가져와 필터링해 products 변수에 저장한다.

        # 상품 정보를 모두 하나씩 가져오기 위한 반복문
        for product in products:
            # 세션에 키 값들은 문자로 넣는다.
            self.cart[str(product.id)]['product'] = product

        # 장바구니에 있는 모든 상품을 가져오기 위한 반복문
        for item in self.cart.values():
            # total_price = price * quantity 즉, 총 금액 = 가격 * 각 상품수량
            item['total_price'] = item['price'] * item['quantity']
            # price = 숫자형 price 즉 가격을 숫자형으로 바꿔 저장한다는 뜻이다.
            item['price'] = Decimal(item['price'])

            yield item # 제너레이터 반환, item에 저장된 여러 상품들을 필요할때마다 바로바로 객체를 생성해 반환한다.

    # 장바구니 담기, 상품 정보 업데이트 여부 확인
    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)# 상품 번호를 문자열로 변경해 product_id에 저장
        if product_id not in self.cart: # 만약 상품 번호가 내 카트에 없다면
            # 내 카트의 해당 상품 번호 = 수량은 0으로, 가격은 상품 가격으로 변경한다.
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)}

        if is_update: # 만약 업데이트가 되지 않았다면 즉, 수량에 변화가 없다면
            self.cart[product_id]['quantity'] = quantity # 내 카트의 해당 상품 수량 = 변화없음
        else: # 업데이트가 되었다면 즉, 수량에 변화가 있다면
            self.cart[product_id]['quantity'] += quantity # 내 카트의 해당 상품 수량에 업데이트 될 수량을 더한다.
        self.save() # 현재 상태를 저장한다.

    # 장바구니 저장하기
    def save(self):
        self.session[settings.CART_ID] = self.cart # settings.py의 CART_ID변수로 세션에 장바구니의 현재 상태를 저장한다.
        self.session.modified = True # 세션이 변경되었음을 의미한다.

    # 장바구니에서 삭제하기
    def remove(self, product):
        product_id = str(product.id) # 상품 번호를 product_id에 문자열로 저장한다.
        if product_id in self.cart: # 문자열인 상품번호에 해당하는 상품이 현재 카트에 있다면
            del(self.cart[product_id]) # 해당하는 상품을 삭제하고
            self.save() # 현재 상태를 저장한다.

    # 장바구니 비우기
    def clear(self, request):
        request.session[settings.CART_ID] = {}
        request.session.modified = True

    # 장바구니 상품의 총 금액
    def get_product_total(self):
        # 장바구니에 저장되어있는 상품의 가격 x 수량을 합해 반환한다.
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())