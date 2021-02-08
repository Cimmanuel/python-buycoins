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

# get_payments = {
#     "data": {
#         "getPayments": {
#             "edges": [
#                 {
#                     "node": {
#                         "id": "UG9zdE9yZGVyLTg5MDM4MzI4LTc5MzItNGUxMS1hZWZjLTkwYjg4ZTFhY2JjOA==",
#                         "cryptocurrency": "bitcoin",
#                         "coinAmount": "0.01060841",
#                         "side": "sell",
#                         "status": "active",
#                         "createdAt": 1612789170,
#                         "pricePerCoin": "20757600.0",
#                         "priceType": "dynamic",
#                         "staticPrice": None,
#                         "dynamicExchangeRate": "480",
#                     }
#                 }
#             ]
#         }
#     }
# }
