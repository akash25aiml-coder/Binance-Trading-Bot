def place_order(symbol, side, type_, quantity, price, stop_price=None):
    try:
        if type_.upper() == "MARKET":
            response = {
                "symbol": symbol,
                "side": side,
                "type": type_,
                "quantity": quantity,
                "status": "success"
            }

        elif type_.upper() == "LIMIT":
            response = {
                "symbol": symbol,
                "side": side,
                "type": type_,
                "quantity": quantity,
                "price": price,
                "status": "success"
            }

        elif type_.upper() == "STOPLIMIT":
            response = {
                "symbol": symbol,
                "side": side,
                "type": type_,
                "quantity": quantity,
                "price": price,
                "stop_price": stop_price,
                "status": "success"
            }

        else:
            response = {"error": f"Unsupported order type: {type_}"}

        logger.info(f"Order placed: {response}")
        return response

    except Exception as e:
        response = {"error": str(e)}
        logger.error(f"Order failed: {response}")
        return response
