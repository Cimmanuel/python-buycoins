# Query responses

get_balance = {
    "data": {
        "getBalances": [
            {
                "id": "QWNjb3VudC0=",
                "cryptocurrency": "bitcoin",
                "confirmedBalance": "0.0",
            }
        ]
    }
}

get_balances = {
    "data": {
        "getBalances": [
            {
                "id": "QWNjb3VudC0=",
                "cryptocurrency": "bitcoin",
                "confirmedBalance": "0.0",
            },
            {
                "id": "QWNjb3VudC0=",
                "cryptocurrency": "usd_tether",
                "confirmedBalance": "0.0",
            },
            {
                "id": "QWNjb3VudC0=",
                "cryptocurrency": "naira_token",
                "confirmedBalance": "0.0",
            },
            {
                "id": "QWNjb3VudC0=",
                "cryptocurrency": "ethereum",
                "confirmedBalance": "0.0",
            },
            {
                "id": "QWNjb3VudC0=",
                "cryptocurrency": "litecoin",
                "confirmedBalance": "0.0",
            },
            {
                "id": "QWNjb3VudC0=",
                "cryptocurrency": "usd_coin",
                "confirmedBalance": "0.0",
            },
        ]
    }
}

get_bank_accounts = {
    "data": {
        "getBankAccounts": [
            {
                "id": "QmFua0FjY291bnQtNjlkZGM2MjEtYzM0My00Mzg1LTlkMDYtY2VkNTM2MWY1Yjkz",
                "bankName": "ALAT by WEMA",
                "accountName": "kolapo ayesebotan",
                "accountNumber": "0235959654",
                "accountType": "withdrawal",
                "accountReference": None,
            }
        ]
    }
}

get_estimated_network_fee_default = {
    "data": {
        "getEstimatedNetworkFee": {
            "total": "0.03036",
            "estimatedFee": "0.00036",
        }
    }
}

get_estimated_network_fee_ethereum = {
    "data": {
        "getEstimatedNetworkFee": {"total": "0.04", "estimatedFee": "0.01"}
    }
}

# The data below was truncated
get_market_book_default = {
    "data": {
        "getMarketBook": {
            "dynamicPriceExpiry": 1612808872,
            "orders": {
                "edges": [
                    {
                        "node": {
                            "id": "UG9zdE9yZGVyLTcxY2JmZjAxLTk2NTEtNGQzOC1hMGIyLWE2YzRkMDUzNWVkMA==",
                            "cryptocurrency": "bitcoin",
                            "coinAmount": "0.013797",
                            "side": "buy",
                            "status": "active",
                            "createdAt": 1612808624,
                            "pricePerCoin": "19501000.0",
                            "priceType": "static",
                            "staticPrice": "1950100000",
                            "dynamicExchangeRate": None,
                        }
                    },
                    {
                        "node": {
                            "id": "UG9zdE9yZGVyLTM5ODg2ZTNlLTJmZDQtNDgxNy05ODRjLWNlMTFlYmIwMzhlMw==",
                            "cryptocurrency": "bitcoin",
                            "coinAmount": "0.00653659",
                            "side": "sell",
                            "status": "active",
                            "createdAt": 1612800454,
                            "pricePerCoin": "20500000.0",
                            "priceType": "static",
                            "staticPrice": "2050000000",
                            "dynamicExchangeRate": None,
                        }
                    },
                ]
            },
        }
    }
}

# The data below was truncated
get_market_book_usd_tether = {
    "data": {
        "getMarketBook": {
            "dynamicPriceExpiry": 1612810492,
            "orders": {
                "edges": [
                    {
                        "node": {
                            "id": "UG9zdE9yZGVyLWZmYTliOTdiLThmZjUtNDE4Mi05ZDJjLWM4ZWM5MzNlMTliZg==",
                            "cryptocurrency": "usd_tether",
                            "coinAmount": "100.0",
                            "side": "buy",
                            "status": "active",
                            "createdAt": 1611770385,
                            "pricePerCoin": "460.0",
                            "priceType": "static",
                            "staticPrice": "46000",
                            "dynamicExchangeRate": None,
                        }
                    },
                    {
                        "node": {
                            "id": "UG9zdE9yZGVyLWI5ZWJkYWNmLTQ1MjYtNDYxYS1hYzFlLTljZTZlNTRmOWFkOA==",
                            "cryptocurrency": "usd_tether",
                            "coinAmount": "234.0",
                            "side": "sell",
                            "status": "active",
                            "createdAt": 1612413166,
                            "pricePerCoin": "499.0",
                            "priceType": "static",
                            "staticPrice": "49900",
                            "dynamicExchangeRate": None,
                        }
                    },
                ]
            },
        }
    }
}

get_orders = {
    "data": {
        "getOrders": {
            "dynamicPriceExpiry": 1612811512,
            "orders": {
                "edges": [
                    {
                        "node": {
                            "id": "UG9zdE9yZGVyLWEzYTAwNzQxLTJhMWUtNGJkMi1iZWFkLWE2ZWU0MzQ1ZmI2Yw==",
                            "cryptocurrency": "bitcoin",
                            "coinAmount": "0.005",
                            "side": "buy",
                            "status": "active",
                            "createdAt": 1605000847,
                            "pricePerCoin": "10900.09",
                            "priceType": "static",
                            "staticPrice": "1090009",
                            "dynamicExchangeRate": None,
                        }
                    }
                ]
            },
        }
    }
}

get_payments = {
    "data": {
        "getPayments": {
            "edges": [
                {
                    "node": {
                        "id": "UG9zdE9yZGVyLTg5MDM4MzI4LTc5MzItNGUxMS1hZWZjLTkwYjg4ZTFhY2JjOA==",
                        "fee": "0.0046",
                        "amount": "10000.00",
                        "createdAt": 1605000847,
                        "reference": "38d5d9018bde98e88058746788d72e936d158f5ad753073f4763dc1d4aa5a48e",
                        "status": "success",
                        "totalAmount": "10000.004600",
                        "type": "deposit",
                    }
                }
            ]
        }
    }
}

get_price = {
    "data": {
        "getPrices": [
            {
                "id": "QnV5Y29pbnNQcmljZS0yOWFmZWY4MS1mZjI5LTQwYTQtYmQ3Zi1iOTgzMTA3NmU5NDg=",
                "status": "active",
                "cryptocurrency": "ethereum",
                "minBuy": "0.02",
                "minSell": "0.02",
                "maxBuy": "48.07685652",
                "maxSell": "0",
                "minCoinAmount": "0.02",
                "expiresAt": 1612847332,
                "buyPricePerCoin": "816107.8759",
                "sellPricePerCoin": "799786.8945",
            }
        ]
    }
}

get_prices = {
    "data": {
        "getPrices": [
            {
                "id": "QnV5Y29pbnNQcmljZS01OTkwYTQ0NC1hYjY4LTQxM2MtODUzZC04OWJhYzRhMWNjZjE=",
                "status": "active",
                "cryptocurrency": "bitcoin",
                "minBuy": "0.001",
                "minSell": "0.001",
                "maxBuy": "1.78700697",
                "maxSell": "1.20119207",
                "minCoinAmount": "0.001",
                "expiresAt": 1612847212,
                "buyPricePerCoin": "21956210.523",
                "sellPricePerCoin": "21521388.24",
            },
            {
                "id": "QnV5Y29pbnNQcmljZS05MjQwNmQ0Zi00MmJlLTQ2MjEtOTY1Ny1mYTM0OGZkNmI2NDE=",
                "status": "active",
                "cryptocurrency": "ethereum",
                "minBuy": "0.02",
                "minSell": "0.02",
                "maxBuy": "48.12180182",
                "maxSell": "0",
                "minCoinAmount": "0.02",
                "expiresAt": 1612847212,
                "buyPricePerCoin": "815345.6391",
                "sellPricePerCoin": "799154.344",
            },
            {
                "id": "QnV5Y29pbnNQcmljZS04NDMyZmI2OS1iMzAyLTQ2YzQtYjFjZC1kZTM2MjNhMTFiYmU=",
                "status": "active",
                "cryptocurrency": "litecoin",
                "minBuy": "0.1",
                "minSell": "0.1",
                "maxBuy": "489.37725284",
                "maxSell": "134.73978949",
                "minCoinAmount": "0.1",
                "expiresAt": 1612847213,
                "buyPricePerCoin": "80175.1635",
                "sellPricePerCoin": "78560.0343",
            },
            {
                "id": "QnV5Y29pbnNQcmljZS05OGI0NTE5ZC05NTJlLTRkNGMtODk1OC03MWI2MjRlZmZlMjc=",
                "status": "active",
                "cryptocurrency": "usd_coin",
                "minBuy": "5",
                "minSell": "5",
                "maxBuy": "83903.73",
                "maxSell": "495437.574734",
                "minCoinAmount": "5",
                "expiresAt": 1612847213,
                "buyPricePerCoin": "467.63",
                "sellPricePerCoin": "458.3206",
            },
        ]
    }
}


# Mutation responses

