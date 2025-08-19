from dataclasses import dataclass, field

@dataclass
class CourseCardParams:
    index: int = 0  # Индекс карточки в списке курсов
    title: str = ""  # Ожидаемый заголовок курса
    max_score: str = ""  # Ожидаемый максимальный балл
    min_score: str = ""  # Ожидаемый минимальный балл
    estimate_time: str = ""  # Ожидаемое время прохождения
    description: str = field(default="")  # Ожидаемое описание
