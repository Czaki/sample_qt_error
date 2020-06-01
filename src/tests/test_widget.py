from sample_qt_error.my_combo_box import MyComboBox
import pytest

@pytest.fixture(scope='session')
def qapp_args():
    return ["-display ' '"]

class TestMyComboBox:
    def test_simple(self, qtbot):
        box = MyComboBox()
        box.show()
        qtbot.add_widget(box)
        box.addItems(["A", "B", "C"])
        assert box.count() == 3
