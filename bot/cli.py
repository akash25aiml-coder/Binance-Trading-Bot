import argparse
import logging

# Configure logging to show INFO level messages in the console
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def place_order(symbol, side, type_, quantity, price, stop_price=None):
    """
    Place an order with the given parameters.
    Always returns a response dictionary (success or error).
    """
    try:
        if type_.upper() == "MARKET":
            response = {"symbol": symbol, "side": side, "type": type_, "quantity": float(quantity), "status": "success"}
        elif type_.upper() == "LIMIT":
            response = {"symbol": symbol, "side": side, "type": type_, "quantity": float(quantity), "price": float(price), "status": "success"}
        elif type_.upper() == "STOPLIMIT":
            response = {"symbol": symbol, "side": side, "type": type_, "quantity": float(quantity), "price": float(price), "stop_price": float(stop_price), "status": "success"}
        else:
            response = {"error": f"Unsupported order type: {type_}"}

        logger.info(f"Order placed successfully: {response}")
        return response

    except Exception as e:
        response = {"error": str(e)}
        logger.error(f"Order failed: {response}")
        return response

def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")
    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="Order side (BUY/SELL)")
    parser.add_argument("--type", required=True, help="Order type (LIMIT/MARKET/STOPLIMIT)")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Order price (required for LIMIT/STOPLIMIT orders)")
    parser.add_argument("--stop_price", type=float, help="Stop price (required for STOPLIMIT orders)")

    args = parser.parse_args()

    response = place_order(args.symbol, args.side, args.type, args.quantity, args.price, args.stop_price)
    print(response)  # ensures visible output in terminal

if __name__ == "__main__":
    main()
