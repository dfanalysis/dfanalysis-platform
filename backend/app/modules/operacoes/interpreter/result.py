from pydantic import BaseModel

from app.modules.operacoes.interpreter.analysis import (
    OperationalAnalysis,
)
from app.modules.operacoes.interpreter.schemas import (
    BusinessExtraction,
)


class InterpreterResult(BaseModel):
    """
    Resultado final produzido pelo módulo
    Communication Interpreter.
    """

    extraction: BusinessExtraction

    analysis: OperationalAnalysis