from __future__ import annotations, division

from functools import partial
from typing import Any, Callable, Optional, Union

class BaseUnit:
    def __init__(
        self,
        name:str,
        symbol:str
    )->None:
        self._name = name
        self._symbol = symbol

class BaseDimension:
    def __init__(
        self,
        name:str,
        symbol:str,
    )->None:
        self.name = name
        self.symbol = symbol

class BaseMeasure:
    def __init__(
        self,
        mark:Optional[str]=None,
        name:Optional[str]=None,
        expression:Optional[Callable]=None,
    )->None:
        self._mark = mark
        self._name = name
        self._expression = expression

    @property
    def mark(self)->str:
        if self._mark is not None: return self._mark
        else: return 'und'

    @property
    def name(self)->str:
        if self._name is not None: return self._name
        else: return 'und'

    @property
    def value(self)->float:
        return self.expression()

    @property
    def expression(self)->partial:
        if self._expression is not None: return self._expression
        else: return partial(lambda: 1.)
    
    def __mul__(self, other:Union[BaseMeasure, float])->BaseMeasure:
        if type(other) is BaseMeasure:
            mark = f'{self.mark}*{other.mark}'
            name = f'{self.name} {other.name}'
            expression = partial(lambda a, b: a.expression() * b.expression(), self, other)
            return BaseMeasure(mark=mark, name=name, expression=expression)
        elif type(other) is float:
            mark = f'{other}{self.mark}'
            name = f'{other} {self.name}'
            expression = partial(lambda a, b: a.expression() * b, self, other)
            return BaseMeasure(mark=mark, name=name, expression=expression)
        else:
            raise TypeError

    def __pow__(self, other:Union[BaseMeasure, float])->BaseMeasure:
        if type(other) is BaseMeasure:
            mark = f'{self.mark}**{other.mark}'
            name = f'{self.name} в степени {other.name}'
            expression = partial(lambda a, b: a.expression() ** b.expression(), self, other)
            return BaseMeasure(mark=mark, name=name, expression=expression)
        elif type(other) is float:
            mark = f'{self.mark}^{other}'
            name = f'{self.name} в {other} степени'
            expression = partial(lambda a, b: a.expression() ** b, self, other)
            return BaseMeasure(mark=mark, name=name, expression=expression)
        else:
            raise TypeError

    def __truediv__(self, other:Union[BaseMeasure, float])->BaseMeasure:
        if type(other) is BaseMeasure:
            mark = f'({self.mark})/({other.mark})'
            name = f'{self.name} делить на {other.name}'
            expression = partial(lambda a, b: a.expression() / b.expression(), self, other)
            return BaseMeasure(mark=mark, name=name, expression=expression)
        elif type(other) is float:
            mark = f'({self.mark})/({other})'
            name = f'{self.name} делить на {other}'
            expression = partial(lambda a, b: a.expression() / b, self, other)
            return BaseMeasure(mark=mark, name=name, expression=expression)
        else:
            raise TypeError