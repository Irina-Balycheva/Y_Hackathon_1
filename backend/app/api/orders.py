from fastapi import APIRouter, Depends

from app.core.orders.operations import OrdersOperations


orders_router = APIRouter(
    prefix='/orders',
    tags=['Orders']
)


@orders_router.get(
    '/{orderkey}/predict',
    responses={
        400: {'description': 'Incorrect orderkey or another data'},
        503: {'description': 'YM server unaviable.'},
    }
)
async def predict_package_by_orderkey(
    orderkey: str,
    operations: OrdersOperations = Depends(),
):
    """ Предсказать упаковку(и) для заказа. """
    await operations.get_info_about_order(orderkey)

    return 1