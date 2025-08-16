from dataclasses import dataclass

@dataclass
class CheckVisibleCourseCardParams:
    index: int  # Индекс карточки в списке курсов
    title: str  # Ожидаемый заголовок курса
    max_score: int  # Ожидаемый максимальный балл
    min_score: int  # Ожидаемый минимальный балл
    estimate_time: str  # Ожидаемое время прохождения
