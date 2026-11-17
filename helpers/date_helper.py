from datetime import datetime, timedelta

def get_date_in(days):
    """Возвращает дату через N дней в формате ДД.ММ.ГГГГ"""
    return (datetime.now() + timedelta(days=days)).strftime("%d.%m.%Y")