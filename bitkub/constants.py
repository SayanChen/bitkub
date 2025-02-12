ENDPOINTS = {
    "API_ROOT": "https://api.bitkub.com",
    
    "STATUS_PATH": "/api/status",
    "MARKET_SYMBOLS_PATH": "/api/market/symbols",
    "MARKET_TICKER_PATH": "/api/market/ticker?sym={sym}",
    "MARKET_TRADES_PATH": "/api/market/trades?sym={sym}&lmt={lmt}",
    "MARKET_BIDS_PATH": "/api/market/bids?sym={sym}&lmt={lmt}",
    "MARKET_ASKS_PATH": "/api/market/asks?sym={sym}&lmt={lmt}",
    "MARKET_BOOKS_PATH": "/api/market/books?sym={sym}&lmt={lmt}",
    "MARKET_DEPTH_PATH": "/api/market/depth?sym={sym}&lmt={lmt}",
    "MARKET_TRADING_VIEW_PATH": "/tradingview/history?symbol={sym}&resolution={int}&from={frm}&to={to}",
    "SERVERTIME_PATH": "/api/v3/servertime",

    "USER_TRADING_CREDITS": "/api/v3/user/trading-credits",
    "USER_LIMITS": "/api/v3/user/limits",
    
    "MARKET_WALLET": "/api/v3/market/wallet",
    "MARKET_BALANCES": "/api/v3/market/balances",
    "MARKET_PLACE_BID": "/api/v3/market/place-bid",
    "MARKET_PLACE_ASK": "/api/v3/market/place-ask",
    "MARKET_CANCEL_ORDER": "/api/v3/market/cancel-order",
    "MARKET_WSTOKEN": "/api/v3/market/wstoken",
    "MARKET_MY_OPEN_ORDERS": "/api/v3/market/my-open-orders",
    "MARKET_MY_ORDER_HISTORY": "/api/v3/market/my-order-history",
    "MARKET_ORDER_INFO": "/api/v3/market/order-info",
    
    "CRYPTO_INTERNAL_WITHDRAW": "/api/v3/crypto/internal-withdraw",
    "CRYPTO_ADDRESSES": "/api/v3/crypto/addresses?p={p}&lmt={lmt}",
    "CRYPTO_WITHDRAW": "/api/v3/crypto/withdraw",
    "CRYPTO_DEPOSIT_HISTORY": "/api/v3/crypto/deposit-history?p={p}&lmt={lmt}",
    "CRYPTO_WITHDRAW_HISTORY": "/api/v3/crypto/withdraw-history?p={p}&lmt={lmt}",
    "CRYPTO_GENERATE_ADDRESS": "/api/v3/crypto/generate-address?sym={sym}",
    
    "FIAT_ACCOUNTS": "/api/v3/fiat/accounts?p={p}&lmt={lmt}",
    "FIAT_WITHDRAW": "/api/v3/fiat/withdraw",
    "FIAT_DEPOSIT_HISTORY": "/api/v3/fiat/deposit-history?p={p}&lmt={lmt}",
    "FIAT_WITHDRAW_HISTORY": "/api/v3/fiat/withdraw-history",
    
}
