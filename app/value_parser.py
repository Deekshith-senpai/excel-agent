def parse_value(value):
    if value is None:
        return None

    value = str(value).strip()

    if value.upper() in ["N/A", "NA", ""]:
        return None

    if "%" in value:
        try:
            return float(value.replace("%", "")) / 100
        except:
            return None

    value = value.replace(",", "")

    if value.upper() == "YES":
        return 1.0

    try:
        return float(value)
    except:
        return None