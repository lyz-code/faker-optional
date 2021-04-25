"""Define the Fake providers."""

from datetime import date, datetime, time
from random import SystemRandom
from typing import Any, Dict, List, Optional, Set, Tuple

from faker.generator import Generator
from faker.providers import BaseProvider
from faker.providers.date_time import Provider as DateProvider
from faker.providers.lorem.en_US import Provider as LoremProvider
from faker.providers.person import Provider as PersonProvider
from faker.providers.python import Provider as PyProvider


# ignore: Cannot subclass BaseProvider it has type Any. I don't know how to solve it
class OptionalProvider(BaseProvider):  # type: ignore
    """Faker Provider to simulate Optional data."""

    def __init__(self, generator: Generator) -> None:
        """Declare the other faker providers."""
        super().__init__(generator)
        self.python = PyProvider(generator)
        self.date = DateProvider(generator)
        self.lorem = LoremProvider(generator)
        self.person = PersonProvider(generator)

    @classmethod
    def _optional_value(cls, value: Any, ratio: float = 0.5) -> Optional[Any]:
        """Return half of the times the value, None the other."""
        if SystemRandom().random() > ratio:
            return None
        else:
            return value

    def optional_int(self, ratio: float = 0.5, **kwargs: Any) -> Optional[int]:
        """Return an optional integer."""
        return self._optional_value(self.python.pyint(**kwargs))

    def optional_bool(self, ratio: float = 0.5, **kwargs: Any) -> Optional[bool]:
        """Return an optional bool."""
        return self._optional_value(self.python.pybool(**kwargs), ratio)

    def optional_str(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional random string of upper and lowercase letters."""
        return self._optional_value(self.python.pystr(**kwargs), ratio)

    def optional_float(self, ratio: float = 0.5, **kwargs: Any) -> Optional[float]:
        """Return an optional float number."""
        return self._optional_value(self.python.pyfloat(**kwargs), ratio)

    def optional_set(self, ratio: float = 0.5, **kwargs: Any) -> Optional[Set[Any]]:
        """Return an optional set."""
        return self._optional_value(self.python.pyset(**kwargs), ratio)

    def optional_list(self, ratio: float = 0.5, **kwargs: Any) -> Optional[List[Any]]:
        """Return an optional list."""
        return self._optional_value(self.python.pylist(**kwargs), ratio)

    def optional_dict(
        self, ratio: float = 0.5, **kwargs: Any
    ) -> Optional[Dict[Any, Any]]:
        """Return an optional dictionary."""
        return self._optional_value(self.python.pydict(**kwargs), ratio)

    def optional_tuple(self, ratio: float = 0.5, **kwargs: Any) -> Optional[Tuple[Any]]:
        """Return an optional tuple."""
        return self._optional_value(self.python.pytuple(**kwargs), ratio)

    def optional_datetime(
        self, ratio: float = 0.5, **kwargs: Any
    ) -> Optional[datetime]:
        """Return an optional datetime."""
        return self._optional_value(self.date.date_time(**kwargs), ratio)

    def optional_date(self, ratio: float = 0.5, **kwargs: Any) -> Optional[date]:
        """Return an optional date."""
        return self._optional_value(self.date.date(**kwargs), ratio)

    def optional_time(self, ratio: float = 0.5, **kwargs: Any) -> Optional[time]:
        """Return an optional time."""
        return self._optional_value(self.date.time(**kwargs), ratio)

    def optional_word(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional word."""
        return self._optional_value(self.lorem.word(**kwargs), ratio)

    def optional_words(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional word."""
        return self._optional_value(self.lorem.words(**kwargs), ratio)

    def optional_sentence(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional sentence."""
        return self._optional_value(self.lorem.sentence(**kwargs), ratio)

    def optional_sentences(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional sentence."""
        return self._optional_value(self.lorem.sentences(**kwargs), ratio)

    def optional_paragraph(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional paragraph."""
        return self._optional_value(self.lorem.paragraph(**kwargs), ratio)

    def optional_paragraphs(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional paragraph."""
        return self._optional_value(self.lorem.paragraphs(**kwargs), ratio)

    def optional_text(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional text."""
        return self._optional_value(self.lorem.text(**kwargs), ratio)

    def optional_texts(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional text."""
        return self._optional_value(self.lorem.texts(**kwargs), ratio)

    def optional_name(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional name."""
        return self._optional_value(self.person.name(**kwargs), ratio)

    def optional_first_name(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional first_name."""
        return self._optional_value(self.person.first_name(**kwargs), ratio)

    def optional_last_name(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional last_name."""
        return self._optional_value(self.person.last_name(**kwargs), ratio)

    def optional_name_female(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional name_female."""
        return self._optional_value(self.person.name_female(**kwargs), ratio)

    def optional_name_male(self, ratio: float = 0.5, **kwargs: Any) -> Optional[str]:
        """Return an optional name_male."""
        return self._optional_value(self.person.name_male(**kwargs), ratio)

    def optional_name_nonbinary(
        self, ratio: float = 0.5, **kwargs: Any
    ) -> Optional[str]:
        """Return an optional name_nonbinary."""
        return self._optional_value(self.person.name_nonbinary(**kwargs), ratio)

    def optional_first_name_female(
        self, ratio: float = 0.5, **kwargs: Any
    ) -> Optional[str]:
        """Return an optional first_name_female."""
        return self._optional_value(self.person.first_name_female(**kwargs), ratio)

    def optional_first_name_male(
        self, ratio: float = 0.5, **kwargs: Any
    ) -> Optional[str]:
        """Return an optional first_name_male."""
        return self._optional_value(self.person.first_name_male(**kwargs), ratio)

    def optional_first_name_nonbinary(
        self, ratio: float = 0.5, **kwargs: Any
    ) -> Optional[str]:
        """Return an optional first_name_nonbinary."""
        return self._optional_value(self.person.first_name_nonbinary(**kwargs), ratio)

    def optional_last_name_female(
        self, ratio: float = 0.5, **kwargs: Any
    ) -> Optional[str]:
        """Return an optional last_name_female."""
        return self._optional_value(self.person.last_name_female(**kwargs), ratio)

    def optional_last_name_male(
        self, ratio: float = 0.5, **kwargs: Any
    ) -> Optional[str]:
        """Return an optional last_name_male."""
        return self._optional_value(self.person.last_name_male(**kwargs), ratio)

    def optional_last_name_nonbinary(
        self, ratio: float = 0.5, **kwargs: Any
    ) -> Optional[str]:
        """Return an optional last_name_nonbinary."""
        return self._optional_value(self.person.last_name_nonbinary(**kwargs), ratio)
