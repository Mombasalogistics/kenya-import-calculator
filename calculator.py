# ================================================
# PROJECT:  Kenya Car Import Duty Calculator
# AUTHOR:   Fredrick Mbindyo
# COMPANY:  Mombasa Logistics Tools
# COPYRIGHT: 2026 Fredrick Mbindyo
# ================================================

car_prices = {
    "1": {"name": "Toyota Harrier 2019",    "fob": 850000},
    "2": {"name": "Toyota Prado 2018",      "fob": 3200000},
    "3": {"name": "Toyota RAV4 2019",       "fob": 1200000},
    "4": {"name": "Land Rover Defender",    "fob": 9500000},
    "5": {"name": "Mazda CX5 2019",         "fob": 950000},
    "6": {"name": "Subaru Forester 2018",   "fob": 750000},
    "7": {"name": "Mercedes GLE 2018",      "fob": 7500000},
    "8": {"name": "BMW X5 2018",            "fob": 6800000},
}

def calculate_taxes(car_name, fob, freight, insurance):
    cif         = fob + freight + insurance
    import_duty = cif * 0.35
    excise_duty = (cif + import_duty) * 0.25
    vat         = (cif + import_duty + excise_duty) * 0.16
    idf         = cif * 0.025
    rdl         = cif * 0.02
    road        = cif * 0.0025
    fixed       = 4380
    total_tax   = import_duty + excise_duty + vat + idf + rdl + road + fixed
    landed      = cif + total_tax
    grand_total = landed + 63000

    return {
        "car_name":    car_name,
        "fob":         fob,
        "freight":     freight,
        "insurance":   insurance,
        "cif":         round(cif),
        "import_duty": round(import_duty),
        "excise_duty": round(excise_duty),
        "vat":         round(vat),
        "idf":         round(idf),
        "rdl":         round(rdl),
        "road":        round(road),
        "fixed":       fixed,
        "total_tax":   round(total_tax),
        "landed":      round(landed),
        "grand_total": round(grand_total),
    }
