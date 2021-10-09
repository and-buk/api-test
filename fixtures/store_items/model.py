from typing import List
import attr


@attr.s
class ItemsResponse:
    items: List[dict] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(dict),
            iterable_validator=attr.validators.instance_of(list),
        ),
    )

