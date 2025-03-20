#pylint: disable=invalid-name
from abc import ABC, abstractmethod
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class ViewInterface(ABC):
  @abstractmethod
  def handle(self, httpRequest: HttpRequest) -> HttpResponse:
    pass
