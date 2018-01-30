from abc import ABCMeta, abstractmethod


class FuncInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def show(self): raise NotImplementedError
