def convert_from_seconds(s):
    """Put your docstring here
    """
    days = s // (24 * 60 * 60)  # Het aantal dagen
    s = s % (24 * 60 * 60)  # Het restant
    hours = s // (60*60)
    s = s % (60*60)
    minutes = s // 60
    s = s % (60)
    seconds = 1
    s = s% (1)
    return [days, hours, minutes, seconds]

