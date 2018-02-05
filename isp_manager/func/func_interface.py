from abc import ABCMeta, abstractmethod


class FuncInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_additional(self, additional): raise NotImplementedError

    @abstractmethod
    def get_func(self): raise NotImplementedError

    @abstractmethod
    def get_elid(self): raise NotImplementedError

    @abstractmethod
    def get_plid(self): raise NotImplementedError

    @abstractmethod
    def get_additional(self): raise NotImplementedError

    @abstractmethod
    def get_issaveaction(self): raise NotImplementedError
