from abc import ABC, abstractmethod


class EmissionRequestRepository(ABC):

    @abstractmethod
    async def add(self, emission_request):
        ...