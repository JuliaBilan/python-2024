class TimeSignature:
    def __init__(self, description):
        self.description = description

    def get_description(self):
        return self.description


class SimpleDupleMetric(TimeSignature):
    def __init__(self):
        super().__init__("2/4: Проста дводольна метрика")


class CompoundDupleMetric(TimeSignature):
    def __init__(self):
        super().__init__("4/8: Дводольна метрика з восьмими нотами")


class TripleMetric(TimeSignature):
    def __init__(self):
        super().__init__("3/8: Тридольна метрика з восьмими нотами")


class CommonTime(TimeSignature):
    def __init__(self):
        super().__init__("4/4: Чотири четверті")


class Waltz(TimeSignature):
    def __init__(self):
        super().__init__("3/4: Тридольна метрика, часто використовується в вальсах")


class ComplexDupleMetric(TimeSignature):
    def __init__(self):
        super().__init__("6/8: Складна дводольна метрика")


sonata_time_signatures = [TripleMetric(), CommonTime()]
polka_time_signatures = [SimpleDupleMetric(), CompoundDupleMetric()]

print("Соната (Sonata) музичні розміри:")
for signature in sonata_time_signatures:
    print(signature.get_description())

print("\nПолька (Polka) музичні розміри:")
for signature in polka_time_signatures:
    print(signature.get_description())
