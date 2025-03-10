#led_repo_interface
from abc import ABC, abstractmethod

class LedInterface(ABC):
    @abstractmethod
    def led_on(self):
        pass
    @abstractmethod
    def led_off(self):
        pass