from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem, Product
from .serializers import CartSerializer, CartItemSerializer


def get_or_create_cart(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.save()  # creates session_key
    cart, _ = Cart.objects.get_or_create(
        user=request.user if request.user.is_authenticated else None,
        session_key=None if request.user.is_authenticated else request.session.session_key
    )
    return cart


@api_view(['GET'])
def get_cart(request):
    cart = get_or_create_cart(request)
    serializer = CartSerializer(cart)
    return Response(serializer.data)


@api_view(['POST'])
def add_to_cart(request):
    cart = get_or_create_cart(request)
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += quantity
    else:
        item.quantity = quantity
    item.save()

    return Response({'message': 'Item added to cart'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_cart_item(request):
    cart = get_or_create_cart(request)
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))

    try:
        item = CartItem.objects.get(cart=cart, product_id=product_id)
        item.quantity = quantity
        item.save()
        return Response({'message': 'Quantity updated'}, status=status.HTTP_200_OK)
    except CartItem.DoesNotExist:
        return Response({'error': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def remove_from_cart(request):
    cart = get_or_create_cart(request)
    product_id = request.data.get('product_id')

    try:
        item = CartItem.objects.get(cart=cart, product_id=product_id)
        item.delete()
        return Response({'message': 'Item removed'}, status=status.HTTP_200_OK)
    except CartItem.DoesNotExist:
        return Response({'error': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)