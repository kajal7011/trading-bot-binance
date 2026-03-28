from bot.client import get_client
from .logging_config import get_logger

client = get_client()
logger = get_logger()

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )
        else:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"Order success: {order}")
        return order

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        return {"error": str(e)}