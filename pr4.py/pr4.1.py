def handler_2_4():
    return "2/4: Проста дводольна метрика"

def handler_4_8():
    return "4/8: Дводольна метрика з восьмими нотами"

def handler_3_8():
    return "3/8: Тридольна метрика з восьмими нотами"

def handler_4_4():
    return "4/4: Чотири четверті"

def handler_3_4():
    return "3/4: Тридольна метрика, часто використовується в вальсах"

def handler_6_8():
    return "6/8: Складна дводольна метрика"

sonata_time_signatures = [handler_3_8, handler_4_4]
polka_time_signatures = [handler_2_4, handler_4_8]

print("Соната (Sonata) музичні розміри:")
for handler in sonata_time_signatures:
    print(handler())

print("Полька (Polka) музичні розміри:")
for handler in polka_time_signatures:
    print(handler())
