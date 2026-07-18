from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.modules.fiscal.enums import StatusSolicitacao
from app.modules.fiscal.solicitacoes.application.create_request import (
    CreateEmissionRequest,
)
from app.modules.fiscal.solicitacoes.application.get_request import (
    GetEmissionRequest,
)
from app.modules.fiscal.solicitacoes.application.list_requests import (
    ListEmissionRequests,
)
from app.modules.fiscal.solicitacoes.exceptions import (
    CompetenciaInvalidaError,
    DescricaoServicoInvalidaError,
    EmpresaInativaError,
    EmpresaNaoEncontradaError,
    IdempotencyConflictError,
    SolicitacaoEmissaoError,
    ValorServicoInvalidoError,
)
from app.modules.fiscal.solicitacoes.schemas import (
    SolicitacaoEmissaoCreate,
    SolicitacaoEmissaoResponse,
)


router = APIRouter(
    prefix="/fiscal/solicitacoes",
    tags=["Fiscal - Solicitações de emissão"],
)

DatabaseSession = Annotated[Session, Depends(get_db)]


@router.post(
    "",
    response_model=SolicitacaoEmissaoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar solicitação de emissão",
    description=(
        "Cria uma nova solicitação de emissão de NFS-e. "
        "Quando uma chave de idempotência for informada, ela não poderá "
        "ser reutilizada."
    ),
)
def create_emission_request(
    payload: SolicitacaoEmissaoCreate,
    db: DatabaseSession,
) -> SolicitacaoEmissaoResponse:
    use_case = CreateEmissionRequest(db)

    try:
        solicitacao, _created = use_case.execute(payload)

        return SolicitacaoEmissaoResponse.model_validate(solicitacao)

    except EmpresaNaoEncontradaError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc) or "Empresa informada não foi encontrada.",
        ) from exc

    except EmpresaInativaError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc) or "A empresa informada está inativa ou excluída.",
        ) from exc

    except IdempotencyConflictError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc) or "A chave de idempotência já foi utilizada.",
        ) from exc

    except (
        CompetenciaInvalidaError,
        ValorServicoInvalidoError,
        DescricaoServicoInvalidaError,
    ) as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc) or "Os dados da solicitação são inválidos.",
        ) from exc

    except SolicitacaoEmissaoError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc) or "Não foi possível criar a solicitação.",
        ) from exc


@router.get(
    "",
    response_model=list[SolicitacaoEmissaoResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar solicitações de emissão",
    description=(
        "Lista as solicitações de emissão pertencentes a uma empresa. "
        "Opcionalmente, permite filtrar pelo status atual."
    ),
)
def list_emission_requests(
    db: DatabaseSession,
    empresa_id: Annotated[
        UUID,
        Query(
            description="Identificador da empresa proprietária das solicitações.",
        ),
    ],
    request_status: Annotated[
        StatusSolicitacao | None,
        Query(
            alias="status",
            description="Status utilizado para filtrar as solicitações.",
        ),
    ] = None,
) -> list[SolicitacaoEmissaoResponse]:
    use_case = ListEmissionRequests(db)

    solicitacoes = use_case.execute(
        empresa_id=empresa_id,
        status=request_status,
    )

    return [
        SolicitacaoEmissaoResponse.model_validate(solicitacao)
        for solicitacao in solicitacoes
    ]


@router.get(
    "/{solicitacao_id}",
    response_model=SolicitacaoEmissaoResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar solicitação de emissão",
    description="Recupera uma solicitação de emissão pelo identificador.",
)
def get_emission_request(
    solicitacao_id: UUID,
    db: DatabaseSession,
) -> SolicitacaoEmissaoResponse:
    use_case = GetEmissionRequest(db)

    solicitacao = use_case.execute(solicitacao_id)

    if solicitacao is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Solicitação de emissão não encontrada.",
        )

    return SolicitacaoEmissaoResponse.model_validate(solicitacao)