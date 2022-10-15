import unittest
from main import Topics, Uni, Rubik, Stream


class Test_Topics(unittest.TestCase):
    def setUp(self):
        self.topic = Topics()

    def test_choose_topic1(self):
        self.assertEqual(self.topic.choose_topic(1), "Стриминговый сервис")

    def test_choose_topic2(self):
        self.assertEqual(self.topic.choose_topic(2), "Университет")

    def test_choose_topic3(self):
        self.assertEqual(self.topic.choose_topic(3), "Кубик Рубика")


class TestRubik(unittest.TestCase):
    def setUp(self):
        self.rubik = Rubik()

    def test_rubik_method1(self):
        self.assertEqual(self.rubik.rubik_method("нет", "", ""), "Досадно:( Тогда лучше о другом поговорить, хах")

    def test_rubik_method2(self):
        self.assertEqual(self.rubik.rubik_method("да", "да", ""), "Чувак, ты крут))")

    def test_rubik_method3(self):
        self.assertEqual(self.rubik.rubik_method("да", "нет", "да"),
                         "Успехов там) Спортивные ручки будут Классно поговорили, спасибо)")

    def test_rubik_method4(self):
        self.assertEqual(self.rubik.rubik_method("да", "нет", "нет"),
                         "Тогда у тебя просто хорошее хобби) Молодец! Классно поговорили, спасибо)")


class TestStream(unittest.TestCase):
    def setUp(self):
        self.stream = Stream()

    def test_stream_method1(self):
        self.assertEqual(self.stream.stream_method("кино", "нет", "", "", "",), "Отлично! Вместе посмотрим тогда)")

    def test_stream_method2(self):
        self.assertEqual(self.stream.stream_method("кино", "да", "классный", "", "",), "Так и знал) Точно гляну")

    def test_stream_method3(self):
        self.assertEqual(self.stream.stream_method("кино", "да", "пойдет", "", "",), "Ох, надеюсь, получше все-таки")

    def test_stream_method4(self):
        self.assertEqual(self.stream.stream_method("кино", "да", "ужас", "", "",), "Мда уж, DC скатились, досадно")

    def test_stream_method5(self):
        self.assertEqual(self.stream.stream_method("сериалы", "", "", "ривердейл", ""),
                         "Друг, нам не о чем говорить, аххахахаа!")

    def test_stream_method6(self):
        self.assertEqual(self.stream.stream_method("сериалы", "", "", "элита", "да"),
                         "Ждем новые тогда) Классно поговорили, спасибо)")

    def test_stream_method7(self):
        self.assertEqual(self.stream.stream_method("сериалы", "", "", "элита", "нет"),
                         "Давай, догоняй меня)) Классно поговорили, спасибо)")


class TestUni(unittest.TestCase):
    def setUp(self):
        self.uni = Uni()

    def test_uni_method1(self):
        self.assertEqual(self.uni.uni_method("ранхигс", "", "", ""), "ПОКА))))")

    def test_uni_method2(self):
        self.assertEqual(self.uni.uni_method("мирэа", "нет", "", ""), "Fuck, кто же мне тогда принтер починит ...")

    def test_uni_method3(self):
        self.assertEqual(self.uni.uni_method("мирэа", "да", "нет", ""), "Неправильно ))))))")

    def test_uni_method4(self):
        self.assertEqual(self.uni.uni_method("мирэа", "да", "да", "да"),  "ХАХАХАХАХАХ")


if __name__ == '__main__':
    unittest.main()
