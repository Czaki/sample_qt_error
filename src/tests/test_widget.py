from sample_qt_error import MyComboBox


class TestMyComboBox:
    def test_simple(self, qtbot):
        box = MyComboBox()
        box.show()
        qtbot.add_widget(box)
