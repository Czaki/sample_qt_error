from sample_qt_error.my_combo_box import MyComboBox


class TestMyComboBox:
    def test_simple(self, qtbot):
        box = MyComboBox()
        box.show()
        qtbot.add_widget(box)
        box.addItems(["A", "B", "C"])
        assert box.count() == 3
