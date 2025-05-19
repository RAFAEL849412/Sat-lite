import json

def init():
    # Exemplo de JSON extraído do seu script
    data = {
        "modules": ["Bootloader"],
        "function": {
            "name": "handlePayload",
            "parameters": {
                "consistency": {
                    "rev": 1010031100,
                    "compMap": {
                        "Dock": {
                            "r": ["U7LpmoG", "J1F5ETJ", "6tTjOTm", "II93DPe", "GrqIbBd", "bZ75lyp", "ITu32E2", "coXAcdj", "+Fu52I4", "kGty6xl", "qdu9zGJ", "Q7j27S5"],
                            "be": 1
                        },
                        "WebSpeedInteractionsTypedLogger": {
                            "r": ["kGty6xl", "5YBxsA6", "kWyeNZx", "ZZMgPUO", "II93DPe"],
                            "be": 1
                        },
                        "AsyncRequest": {
                            "r": ["8bxxRsD", "6tTjOTm", "II93DPe", "kGty6xl", "GrqIbBd"],
                            "rds": {
                                "m": ["FbtLogging", "IntlQtEventFalcoEvent"]
                            },
                            "be": 1
                        },
                        "DOM": {
                            "r": ["II93DPe", "kGty6xl", "GrqIbBd"],
                            "be": 1
                        },
                        "Form": {
                            "r": ["II93DPe", "ZVejPaf", "kGty6xl", "GrqIbBd"],
                            "be": 1
                        },
                        "FormSubmit": {
                            "r": ["8bxxRsD", "6tTjOTm", "II93DPe", "2MYQsw8", "ZVejPaf", "kGty6xl", "GrqIbBd"],
                            "rds": {
                                "m": ["FbtLogging", "IntlQtEventFalcoEvent"]
                            },
                            "be": 1
                        },
                        "Input": {
                            "r": ["ZVejPaf"],
                            "be": 1
                        },
                        "Toggler": {
                            "r": ["6tTjOTm", "II93DPe", "GrqIbBd", "bZ75lyp", "ITu32E2", "coXAcdj", "+Fu52I4", "kGty6xl", "qdu9zGJ"],
                            "be": 1
                        },
                        "Tooltip": {
                            "r": ["R5w1rCJ", "8bxxRsD", "J1F5ETJ", "6tTjOTm", "II93DPe", "GrqIbBd", "bZ75lyp", "DcLQ9Pg", "RJqnX18", "/AN8Bt5", "+Fu52I4", "kGty6xl", "81EcBFr", "qdu9zGJ", "Q7j27S5", "Aiay[...]" ],
                            "rds": {
                                "m": ["FbtLogging", "IntlQtEventFalcoEvent", "PageTransitions", "Animation"]
                            },
                            "be": 1
                        },
                        "URI": {
                            "r": [],
                            "be": 1
                        },
                        "trackReferrer": {
                            "r": [],
                            "be": 1
                        },
                        "PhotoTagApproval": {
                            "r": ["aNJNbhK", "II93DPe", "+850GKX", "kGty6xl", "GrqIbBd"],
                            "be": 1
                        },
                        "PhotoSnowlift": {
                            "r": ["UtssFLi", "R5w1rCJ", "JC8SFUa", "bY8rQGh", "GdOSzrC", "U7LpmoG", "WPZeT3l", "yFtLw7s", "4+OLCrF", "Cp8j+Tj", "8bxxRsD", "0Bj1L9r", "W71ZZuY", "matyWMX", "Lfg2XHL", "pZuC[...]" ],
                            "rds": {
                                "m": ["Animation", "FbtLogging", "IntlQtEventFalcoEvent", "PageTransitions"]
                            },
                            "be": 1
                        },
                        "PhotoTagger": {
                            "r": ["R5w1rCJ", "WPZeT3l", "4+OLCrF", "8bxxRsD", "0Bj1L9r", "pZuCvpU", "J1F5ETJ", "aNJNbhK", "6tTjOTm", "GGAMGU9", "lYXceyr", "II93DPe", "rwHqT12", "G0Y2AR3", "mD0x5VU", "GrqI[...]" ],
                            "rds": {
                                "m": ["FbtLogging", "IntlQtEventFalcoEvent", "PageTransitions", "Animation"]
                            },
                            "be": 1
                        },
                        "PhotoTags": {
                            "r": ["aNJNbhK", "II93DPe", "+850GKX", "kGty6xl", "qdu9zGJ", "GrqIbBd"],
                            "be": 1
                        },
                        "TagTokenizer": {
                            "r": ["+ryvGjy", "Cp8j+Tj", "GGAMGU9", "II93DPe", "GrqIbBd", "ZVejPaf", "ol8D+V0", "ja/Mjsm", "h3c2ZGT", "+850GKX", "+Fu52I4", "kGty6xl", "qdu9zGJ", "LXWb9bQ"],
                            "rds": {
                                "m": ["FbtLogging", "IntlQtEventFalcoEvent"],
                                "r": ["8bxxRsD"]
                            },
                            "be": 1
                        },
                        "AsyncDialog": {
                            "r": ["UtssFLi", "R5w1rCJ", "WPZeT3l", "4+OLCrF", "8bxxRsD", "0Bj1L9r", "Ynnl66x", "J1F5ETJ", "KZruzbc", "6tTjOTm", "iIftanq", "Xk+4IV6", "II93DPe", "G0Y2AR3", "GrqIbBd", "bZ75[...]" ],
                            "rds": {
                                "m": ["FbtLogging", "IntlQtEventFalcoEvent"]
                            },
                            "be": 1
                        },
                        "Hovercard": {
                            "r": ["R5w1rCJ", "WPZeT3l", "8bxxRsD", "0Bj1L9r", "pZuCvpU", "J1F5ETJ", "6tTjOTm", "GGAMGU9", "lYXceyr", "II93DPe", "G0Y2AR3", "mD0x5VU", "GrqIbBd", "bZ75lyp", "ITu32E2", "DcLQ[...]" ],
                            "rds": {
                                "m": ["FbtLogging", "IntlQtEventFalcoEvent", "PageTransitions", "Animation"]
                            },
                            "be": 1
                        },
                        "XSalesPromoWWWDetailsDialogAsyncController": {
                            "r": ["pZuCvpU", "KTJXyzv"],
                            "be": 1
                        },
                        "XOfferController": {
                            "r": ["pZuCvpU", "xsFg75a"],
                            "be": 1
                        },
                        "PerfXSharedFields": {
                            "r": ["MuhE2hb", "kGty6xl"],
                            "be": 1
                        },
                        "Dialog": {
                            "r": ["8bxxRsD", "0Bj1L9r", "J1F5ETJ", "6tTjOTm", "II93DPe", "GrqIbBd", "bZ75lyp", "ITu32E2", "3Ni7ctL", "jn9feXf", "ZVejPaf", "+Fu52I4", "kGty6xl", "qdu9zGJ", "Q7j27S5", "R5w1[...]" ],
                            "rds": {
                                "m": ["FbtLogging", "IntlQtEventFalcoEvent", "Animation", "PageTransitions"]
                            },
                            "be": 1
                        },
                        "ExceptionDialog": {
                            "r": ["UtssFLi", "R5w1rCJ", "WPZeT3l", "Cp8j+Tj", "8bxxRsD", "0Bj1L9r", "Ynnl66x", "J1F5ETJ", "KZruzbc", "R7mqa9A", "6tTjOTm", "iIftanq", "Xk+4IV6", "II93DPe", "G0Y2AR3", "GrqI[...]" ],
                            "rds": {
                                "m": ["FbtLogging", "IntlQtEventFalcoEvent"]
                            },
                            "be": 1
                        },
                        "QuickSandSolver": {
                            "r": ["SKLfEIC", "SWx3yNv", "8bxxRsD", "6tTjOTm", "II93DPe", "ZVejPaf", "62yCEfA", "kGty6xl", "x22Oby4", "8ELCBwH", "GrqIbBd"],
                            "rds": {
                                "m": ["FbtLogging", "IntlQtEventFalcoEvent"]
                            },
                            "be": 1
                        },
                        "ConfirmationDialog": {
                            "r": ["II93DPe", "ZVejPaf", "oE4DofT", "kGty6xl", "qdu9zGJ", "GrqIbBd"],
                            "be": 1
                        },
                        "MWADeveloperReauthBarrier": {
                            "r": ["17Grp2h", "QyoftxH", "H/5lfuF", "II93DPe", "kGty6xl", "QIamfde"],
                            "be": 1
                        }
                    }
                }
            }
        }
    }

    def listar_componentes(comp_map):
        for componente, detalhes in comp_map.items():
            recursos = detalhes.get("r", [])
            print(f"Componente: {componente}")
            print(f"  Recursos: {', '.join(recursos)}")
            if "rds" in detalhes:
                print(f"  RDS: {json.dumps(detalhes['rds'])}")
            print(f"  BE: {detalhes.get('be')}")
            print("-" * 30)

    comp_map = data["function"]["parameters"]["consistency"]["compMap"]
    listar_componentes(comp_map)
