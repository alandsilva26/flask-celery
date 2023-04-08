from dependency_injector.containers import Container, DeclarativeContainer
from dependency_injector.providers import Singleton

from .services.math_service import MathService

class Container(DeclarativeContainer):
    pass