#pylint: disable=line-too-long
from src.controllers.interfaces.pet_list_controller_interface import PetListControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class PetListView(ViewInterface):
  def __init__(self, controller: PetListControllerInterface) -> None:
    self.__controller = controller

  def handle(self, http_request: HttpRequest) -> HttpResponse:
    body_response = self.__controller.list_pets()

    return HttpResponse(
      status_code=200,
      body=body_response
    )
