from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(
                stock=stock,
                product=position['product'],
                quantity=position['quantity'],
                price=position['price']
            )
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)

        for position in positions:
            StockProduct.objects.filter(stock=stock).update_or_create(
                product=position['product'],
                defaults={
                    'stock': stock,
                    'product': position['product'],
                    'quantity': position['quantity'],
                    'price': position['price']
                }
            )
        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock
