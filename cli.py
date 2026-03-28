print("CLI started...")

import argparse
from bot.orders import place_order
from bot.validators import validate_input

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_input(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    order = place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    print("\n===== ORDER RESULT =====")
    print(order)

except Exception as e:
    print(f"Error: {str(e)}")