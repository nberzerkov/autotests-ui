import random
import pytest

PLATFORM = "Linux"

@pytest.mark.flaky(reruns=3, reruns_delay=2) # Макс. 3 перезапуска, с задержкой в две секунды
def test_reruns() -> None:
    assert random.choice([True, False])

@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestRerunss:
    def test_rerun_1(self) -> None:
        assert random.choice([True, False])

    def test_rerun_2(self) -> None:
        assert random.choice([True, False])

@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == 'Linux')
def test_rerun_with_condition() -> None:
    assert random.choice([True, False])